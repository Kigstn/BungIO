import os
import re
from typing import Optional

import requests

from bungio.definitions import ROOT_DIR


def main():
    resp = requests.get(url="https://raw.githubusercontent.com/Bungie-net/api/master/openapi.json")
    api_schema = resp.json()

    generate_models(api_schema)
    generate_manifest_info(api_schema)

    # paths
    base_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bungio/http/routes")
    topics = {}
    for path, data in api_schema["paths"].items():
        topic = path.split("/")[1]
        if topic not in topics:
            topics[topic] = {}
        topics[topic][path] = data

    names = {}
    for topic, routes in topics.items():
        text = f"""import datetime
from typing import Callable, Coroutine, Optional, Any

from bungio.http.route import Route
from bungio.models.auth import AuthData


class {topic}Requests:
    request: Callable[..., Coroutine]
    """

        for path, data in routes.items():
            text += generate_function(path, data, api_schema)
        file_path = os.path.join(base_path, f"{capital_case_to_snake_case(topic)}.py")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)

        relative_path = os.path.relpath(file_path, ROOT_DIR).replace(".py", "").replace(os.sep, ".")
        names[f"{topic}Requests"] = relative_path

        docs_path = os.path.join(
            ROOT_DIR, f"docs/src/API Reference/HTTP/Bungie Routes/{capital_case_to_snake_case(topic)}.md"
        )
        with open(docs_path, "w", encoding="utf-8") as file:
            file.write(
                f"""# {topic} Routes

::: bungio.http.routes.{capital_case_to_snake_case(topic)}
"""
            )

    init_text = ""
    for name, path in names.items():
        init_text += f"from {path} import {name}\n"

    init_text += f"""

class AllRequests({", ".join(list(names))}):
    pass
"""
    with open(os.path.join(base_path, "__init__.py"), "w", encoding="utf-8") as file:
        file.write(init_text)

    os.system(f"""black "{base_path}\"""")


def generate_function(path: str, data: dict, full_data: dict) -> str:
    # make the class text
    text = f"""
    async def {capital_case_to_snake_case(data["summary"].split(".")[1])}(self"""

    method = "get" if "get" in data else "post"

    security = None
    if "security" in data[method]:
        security = f"""Required oauth2 scopes: {", ".join(data[method]["security"][0]["oauth2"])}"""

    # json body info
    body = []
    if "requestBody" in data[method]:
        schema_data = data[method]["requestBody"]["content"]["application/json"]["schema"]
        if "$ref" in schema_data:
            schema_name = schema_data["$ref"]
            schema_name = schema_name.split("/")[-1]
            schema_data = full_data["components"]["schemas"][schema_name]["properties"]

            for name, value in schema_data.items():
                arg_type = convert_to_typing(value)
                body.append(
                    {
                        "name": capital_case_to_snake_case(name),
                        "og_name": name,
                        "description": value.get("description", "Not specified."),
                        "type": arg_type,
                    }
                )

        else:
            arg_type = convert_to_typing(schema_data)
            body.append(
                {
                    "name": "body_data",
                    "description": schema_data.get("description", "Not specified."),
                    "type": arg_type,
                }
            )

    # path / query params
    params = []
    for param in data[method]["parameters"]:
        new_name = capital_case_to_snake_case(param["name"])
        if (string := f"""{{{param["name"]}}}""") in path:
            path = path.replace(string, f"""{{{new_name}}}""")

        info = {
            "name": new_name,
            "description": param["description"] or "Not specified.",
            "in": param["in"],
        }

        arg_type = convert_to_typing(param["schema"])

        if info["in"] == "query":
            arg_type = f"Optional[{arg_type}] = None"
        info["type"] = arg_type

        params.append(info)

    security_info = {
        "name": "auth",
    }
    if security:
        security_info["description"] = "Authentication information."
        security_info["type"] = "AuthData"
        security_info["in"] = "pb"
    else:
        security_info[
            "description"
        ] = "Authentication information. Required when users with a private profile are queried."
        security_info["type"] = "Optional[AuthData] = None"
        security_info["in"] = "query"
    params.append(security_info)

    params = sorted(params, key=lambda x: x["in"])

    for item in body + params:  # noqa
        text += f""", {item["name"]}: {item["type"]}"""

    text += f""") -> dict:
        \"\"\"
        {data["description"]}
        """

    if security:
        text += f"""
        Warning: Requires Authentication.
            {security}
        """

    text += """
        Args:"""

    for item in body + params:  # noqa
        text += f"""
            {item["name"]}: {item["description"]}"""

    text += f"""

        Raises:
            NotFound: 404 request
            BadRequest: 400 request
            InvalidAuthentication: If authentication is invalid
            TimeoutException: If no connection could be made
            BungieDead: Servers are down
            AuthenticationTooSlow: The authentication key has expired
            BungieException: Relaying the bungie error

        Returns:
            The json response
        \"\"\"

        """

    if body:
        if len(body) == 1 and "og_name" not in body[0]:
            text += f"""data = {body[0]["name"]}
            """

        else:
            text += "data = {"
            for item in body:
                text += f"""
                \"{item["og_name"]}": {item["name"]},"""

            text += """
            }
            """

    text += f"""
        return await self.request(Route(path=f"{path}", method="{method.upper()}\""""

    if body:
        text += ", data=data"

    for param in params:
        if param["in"] != "path":
            text += f""", {param["name"]}={param["name"]}"""

    text += """))

    """

    return text


def convert_to_typing(
    data: dict, return_class_names: bool = False, path: Optional[str] = None, file_imports: Optional[set] = None
) -> str:
    if "$ref" in data:
        if return_class_names:
            import_path, import_name = get_import_name_from_ref(data["$ref"])
            if file_imports and path and import_path != path:
                file_imports.add(f"    from bungio.models.bungie.{path} import {import_name}")
            return f'"{import_name}"'
        else:
            return "Any"

    if "format" not in data:
        arg_format = data["type"]
    else:
        arg_format = data["format"]

    match arg_format:
        case "int16" | "int32" | "int64" | "byte" | "uint32":
            arg_type = "int"
        case "double" | "float":
            arg_type = "float"
        case "string":
            arg_type = "str"
        case "boolean":
            arg_type = "bool"
        case "date-time":
            arg_type = "datetime.datetime"
        case "array":
            arg_type = f"""list[{convert_to_typing(data["items"], return_class_names=return_class_names, file_imports=file_imports, path=path)}]"""
        case "object":
            arg_type = "Any"
        case _:
            raise ValueError(arg_format)

    return arg_type


def capital_case_to_snake_case(string: str) -> str:
    string = f"{string[0].upper()}{string[1:]}"
    return "_".join(re.findall("[A-Z][^A-Z]*", string)).lower()


def get_import_name_from_ref(string: str) -> tuple[str, str]:
    """Like #/components/responses/User.GeneralUser"""
    strings = string.split("/")[-1].split(".")

    path = ".".join([s.lower() for s in strings[:-1]])
    import_name = strings[-1]

    return path, import_name


def generate_manifest_info(api_schema: dict):
    pass
    # todo
    # base_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bungio/models/manifest")
    #
    # resp = requests.get(url="https://www.bungie.net/Platform/Destiny2/Manifest")
    # manifest = list(resp.json()["Response"]["jsonWorldComponentContentPaths"]["en"])
    #
    #
    # print(1)
    #
    # # todo docs


def generate_models(api_schema: dict):
    base_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bungio/models/bungie")
    docs_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "docs/src/API Reference/Models/Bungie API Models"
    )

    by_path: dict[str, list[dict]] = {}
    for name, schema in api_schema["components"]["schemas"].items():
        path, import_name = get_import_name_from_ref(name)
        if path == "":
            path = "misc"
        if path not in by_path:
            by_path[path] = []
        by_path[path].append({"name": import_name, **schema})

    for path, models in by_path.items():
        text = """import attr
import datetime

from typing import Optional, Any, TYPE_CHECKING

from bungio.models.base import BaseModel, BaseEnum

{imports}"""

        file_imports = set()
        for model in models:
            model_text = generate_model(api_schema, model, path, file_imports)
            text += f"""
{model_text}
            """

        formatted_imports = "\n".join(list(file_imports))
        if file_imports:
            formatted_imports = f"""
if TYPE_CHECKING:
    {formatted_imports}"""
        text = text.format(imports=formatted_imports)
        file_path = os.path.join(base_path, f"""{path.replace(".", "/")}.py""")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)

        # todo write the init files

        file_path = os.path.join(docs_path, f"""{path.replace(".", "/")}.md""")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(
                f"""# {path.split(".")[-1].capitalize()} API Models

::: bungio.models.bungie.{path}
"""
            )
    os.system(f"""black "{base_path}\"""")


def generate_model(api_schema: dict, model: dict, path: str, file_imports: set) -> str:
    """
    Returns:
        text, list of required imports
    """
    text = ""

    # enums
    if data := model.get("x-enum-values", None):
        text = f"""
class {model["name"]}(BaseEnum):
    \"\"\"
    {model.get("description", "Not specified.")}
    \"\"\"
"""
        for item in data:
            text += f"""
    {capital_case_to_snake_case(item["identifier"]).upper()} = {item["numericValue"]}
    \"\"\"{item.get("description", "Not specified.")} \"\"\""""

    # classes
    elif model["type"] == "object":
        if "properties" not in model:
            return ""

        text = f"""
@attr.define
class {model["name"]}(BaseModel):
    \"\"\"
    {model.get("description", "Not specified.")}

    Attributes:"""

        for name, data in model["properties"].items():
            text += f"""
        {capital_case_to_snake_case(name)}: {data.get("description", "Not specified.")}"""

        text += """
    \"\"\"
"""

        for name, data in model["properties"].items():
            text += f"""
    {capital_case_to_snake_case(name)}: {convert_to_typing(data, return_class_names=True, file_imports=file_imports, path=path)} = attr.field()"""

    # arrays
    elif model["type"] == "array":
        return ""

    else:
        raise ValueError(model)

    return text


main()
