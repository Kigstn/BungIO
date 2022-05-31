# do not touch, very clunky black magic
import importlib
import os
import re
from typing import Optional

import requests

from bungio.definitions import ROOT_DIR


def main():
    resp = requests.get(url="https://raw.githubusercontent.com/Bungie-net/api/master/openapi.json")
    api_schema = resp.json()

    generate_models(api_schema)

    generate_functions(
        api_schema,
        folder_path="bungio/http/routes",
        docs_path="docs/src/API Reference/HTTP/Bungie Routes",
        create_raw_http=True,
    )

    generate_functions(
        api_schema,
        folder_path="bungio/api/bungie",
        docs_path="docs/src/API Reference/Bungie Interface",
        create_raw_http=False,
    )


def generate_functions(api_schema: dict, folder_path: str, docs_path: str, create_raw_http: bool = True):
    # paths
    base_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), folder_path)
    topics = {}
    for path, data in api_schema["paths"].items():
        topic = path.split("/")[1]
        if topic not in topics:
            topics[topic] = {}
        topics[topic][path] = data

    names = {}
    for topic, routes in topics.items():
        file_imports = set()

        if create_raw_http:
            name = f"{topic}RouteHttpRequests"
            text = f"""import datetime
from typing import Callable, Coroutine, Optional, Any

from bungio.http.route import Route
from bungio.models.auth import AuthData


class {name}:
    request: Callable[..., Coroutine]
    """

        else:
            name = f"{topic}RouteInterface"
            text = f"""import datetime
import attr
from typing import Optional, Any

from bungio.models.base import BaseModel
from bungio.models.auth import AuthData

%imports%

@attr.define
class {name}(BaseModel):
    """

        for path, data in routes.items():
            text += generate_function(
                path, data, api_schema, create_raw_http=create_raw_http, file_imports=file_imports
            )

        if not create_raw_http:
            text = text.replace("%imports%", "\n".join(file_imports))

        file_path = os.path.join(base_path, f"{capital_case_to_snake_case(topic)}.py")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)

        relative_path = os.path.relpath(file_path, ROOT_DIR).replace(".py", "").replace(os.sep, ".")
        names[name] = relative_path

        actual_docs_path = os.path.join(ROOT_DIR, f"{docs_path}/{capital_case_to_snake_case(topic)}.md")
        if create_raw_http:
            docs_name = f"{topic} HTTP Routes"
        else:
            docs_name = f"{topic} Routes"

            # is there an overwrite?
            overwrite_path = os.path.join(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), folder_path).replace("bungie", "overwrites"),
                f"{capital_case_to_snake_case(topic)}.py",
            )
            if os.path.exists(overwrite_path):
                relative_path = os.path.relpath(overwrite_path, ROOT_DIR).replace(".py", "").replace(os.sep, ".")

        with open(actual_docs_path, "w", encoding="utf-8") as file:
            file.write(
                f"""# {docs_name}

::: {relative_path}
"""
            )

    if create_raw_http:
        init_text = ""
        for name, path in names.items():
            init_text += f"from {path} import {name}\n"

        init_text += f"""

class AllRouteHttpRequests({", ".join(list(names))}):
    pass
        """
        with open(os.path.join(base_path, "__init__.py"), "w", encoding="utf-8") as file:
            file.write(init_text)

    else:
        init_text = ""
        overwrite_init_text = ""

        init_name = []
        overwrite_names = []
        for name, path in names.items():
            # overwrite exists?
            try:
                overwrite_import_path = path.replace("bungie", "overwrites")
                importlib.import_module(overwrite_import_path, name)  # todo test
                overwrite_init_text += f"from {overwrite_import_path} import {name}\n"
                overwrite_names.append(name)
            except ModuleNotFoundError:
                init_text += f"from {path} import {name}\n"
                init_name.append(name)

        init_text += f"""

class AllRouteInterfaces({", ".join(init_name)}):
    pass
        """
        with open(os.path.join(base_path, "__init__.py"), "w", encoding="utf-8") as file:
            file.write(init_text)

            overwrite_init_text += f"""

class AllRouteInterfacesOverwrites({", ".join(overwrite_names)}):
    pass
        """
        overwrite_path = os.path.join(base_path.removesuffix("bungie"), "overwrites/__init__.py")
        with open(overwrite_path, "w", encoding="utf-8") as file:
            file.write(overwrite_init_text)

    os.system(f"""autoflake --ignore-init-module-imports --remove-all-unused-imports -i -r "{base_path}\"""")
    os.system(f"""black "{base_path}\"""")
    os.system(f"""git add "{base_path}\"""")


def generate_function(path: str, data: dict, full_data: dict, file_imports: set, create_raw_http: bool) -> str:
    # make the class text
    func_name = capital_case_to_snake_case(data["summary"].split(".")[1])
    text = f"""
    async def {func_name}(self"""

    method = "get" if "get" in data else "post"

    security = None
    if "security" in data[method]:
        security = f"""Required oauth2 scopes: {", ".join(data[method]["security"][0]["oauth2"])}"""

    # json body info
    body = []
    if "requestBody" in data[method]:
        schema_data = data[method]["requestBody"]["content"]["application/json"]["schema"]

        if create_raw_http:
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
                            "description": clean_desc(value),
                            "type": arg_type,
                        }
                    )

            else:
                arg_type = convert_to_typing(schema_data)
                body.append(
                    {
                        "name": "body_data",
                        "description": clean_desc(schema_data),
                        "type": arg_type,
                    }
                )
        else:
            if "$ref" in schema_data:
                import_path, _, arg_type, clean_model_name = add_to_import_paths(
                    file_imports=file_imports,
                    schema_dict=schema_data,
                    overwrite_path="bungio.models.overwrites",
                    regular_path="bungio.models.bungie",
                )
            else:
                arg_type = convert_to_typing(schema_data)

            body.append({"name": "data", "description": "The required data for this request.", "type": arg_type})

    # path / query params
    params = []
    for param in data[method]["parameters"]:
        new_name = capital_case_to_snake_case(param["name"])
        if (string := f"""{{{param["name"]}}}""") in path:
            path = path.replace(string, f"""{{{new_name}}}""")

        info = {
            "name": new_name,
            "description": clean_desc(param),
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
        security_info["in"] = "pb"  # we sort by alphabet, so this is after "page" and before "query"
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

    if create_raw_http:
        return_model = "dict"
    else:
        return_schema = data[method]["responses"]["200"]["$ref"]
        return_info = full_data["components"]["responses"][return_schema.split("/")[-1]]["content"]["application/json"][
            "schema"
        ]["properties"]["Response"]

        # try to get the overwrite path if that exists and add that to the imports
        return_import_path, actual_return_import_path, return_model, clean_return_model = add_to_import_paths(
            file_imports=file_imports,
            schema_dict=return_info,
            overwrite_path="bungio.models.overwrites",
            regular_path="bungio.models.bungie",
        )

    text += f""") -> {return_model}:
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

    if create_raw_http:
        text += """

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
    else:
        text += f"""

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        \"\"\"

        """

    if create_raw_http:
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

    else:
        request_params = []
        for param in params:
            request_params.append(f"""{param["name"]}={param["name"]}""")
        if body:
            request_params.append("**data.to_dict()")

        text += f"""
        response = await self._client.http.{func_name}({", ".join(request_params)})
        """
        if return_import_path:  # noqa
            if "list" not in return_model:
                text += f"""return {return_model}.from_dict(data=response, client=self._client)

                """
            else:
                text += f"""return [{clean_return_model}.from_dict(data=entry, client=self._client) for entry in response["Result"]]

                """
        else:
            text += f"""return response["Result"]

            """

    return text


def convert_to_typing(
    data: dict, return_class_names: bool = False, path: Optional[str] = None, file_imports: Optional[set] = None
) -> str:
    if new_data := data.get("allOf", None):
        assert isinstance(new_data, list)
        assert len(new_data) == 1
        return convert_to_typing(
            data=new_data[0], return_class_names=return_class_names, path=path, file_imports=file_imports
        )

    if new_data := data.get("$ref", None):
        if return_class_names:
            _, import_name = get_import_name_from_ref(new_data)
            if isinstance(file_imports, set):
                file_imports.add(f"    from bungio.models import {import_name}")
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

    import_path = ".".join([s.lower() for s in strings[:-1]]).removesuffix(".")
    import_name = strings[-1]

    if import_path == "":
        import_path = "misc"

    return import_path, import_name


def generate_models(api_schema: dict):
    base_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bungio/models/bungie")
    docs_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "docs/src/API Reference/Models/Bungie API Models"
    )

    by_path: dict[str, list[dict]] = {}
    for name, schema in api_schema["components"]["schemas"].items():
        path, import_name = get_import_name_from_ref(name)
        if path not in by_path:
            by_path[path] = []
        by_path[path].append({"name": import_name, **schema})

    # do folders first, because some files are also folders -> they need to go in the init
    by_path = {k: v for k, v in sorted(by_path.items(), key=lambda x: x[0].count("."), reverse=True)}

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
        file_path = os.path.join(base_path, path.replace(".", "/"))

        # put files that are also folders in init file
        if os.path.isdir(file_path):
            file_path = os.path.join(file_path, "__init__.py")
        else:
            file_path = f"{file_path}.py"

        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)

    # generate the docs
    for path, models in by_path.items():
        os_path = path.replace(".", "/")

        # is this in a folder as well, aka is the info in an __init__.py file
        import_name = f"bungio.models.overwrites.{path}"
        to_import = []
        if not os.path.isdir(os.path.join(base_path, os_path)):
            file_path = os.path.join(docs_path, f"{os_path}.md")
        else:
            file_path = os.path.join(docs_path, f"""{os_path}/{path.split(".")[-1]}.md""")
            import_name = f"{import_name}.__init__"

            # set the import names
            for model in models:
                to_import.append(model["name"])

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        doc_text = f"""# {path.split(".")[-1].capitalize()} API Models

"""

        # do the overwrites exist
        try:
            importlib.import_module(import_name)
            doc_text += f"""::: {import_name.removesuffix(".__init__")}
    options:
        show_if_no_docstring: true"""
            if to_import:
                doc_text += """
        members:"""
                for name in to_import:
                    doc_text += f"""
            - {name}"""

        except ModuleNotFoundError:
            pass
        doc_text += f"""
::: {import_name.replace("overwrites", "bungie").removesuffix(".__init__")}"""
        if to_import:
            doc_text += """
    options:
        members:"""
            for name in to_import:
                doc_text += f"""
            - {name}"""
        doc_text += """
"""

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(doc_text)

    # write init files
    init_text = ""
    overwrite_init_text = ""

    for path, items in by_path.items():
        for data in items:
            init_path = f"bungio.models.bungie.{path}"
            name = data["name"]

            if "[]" in name:
                continue

            # overwrite exists?
            try:
                overwrite_import_path = init_path.replace("bungie", "overwrites")
                imp = importlib.import_module(overwrite_import_path)
                if not hasattr(imp, name):
                    raise ModuleNotFoundError
                overwrite_init_text += f"from {overwrite_import_path} import {name}\n"
            except ModuleNotFoundError:
                try:
                    imp = importlib.import_module(init_path)
                    if not hasattr(imp, name):
                        raise ModuleNotFoundError
                    init_text += f"from {init_path} import {name}\n"
                except ModuleNotFoundError:
                    pass

    init_path = os.path.join(base_path, "__init__.py")
    with open(init_path, "w", encoding="utf-8") as file:
        file.write(init_text)

    overwrite_path = os.path.join(base_path.removesuffix("bungie"), "overwrites/__init__.py")
    with open(overwrite_path, "w", encoding="utf-8") as file:
        file.write(overwrite_init_text)

    # create empty inits, needed for docs collection
    for subdir, _, _ in os.walk(base_path):
        if "__" not in subdir:
            init_path = os.path.join(subdir, "__init__.py")
            if not os.path.exists(init_path):
                with open(init_path, "w", encoding="utf-8") as file:
                    file.write("")

    os.system(f"""autoflake --ignore-init-module-imports --remove-all-unused-imports -i -r "{base_path}\"""")
    os.system(f"""black "{base_path}\"""")
    os.system(f"""git add "{base_path}\"""")


def generate_model(api_schema: dict, model: dict, path: str, file_imports: set) -> str:
    """
    Returns:
        text
    """

    required_imports = []

    # enums
    if data := model.get("x-enum-values", None):
        text = f"""
class {model["name"]}(BaseEnum):
    \"\"\"
    {clean_desc(model)}
    \"\"\"
"""
        for item in data:
            text += f"""
    {capital_case_to_snake_case(item["identifier"]).upper()} = {item["numericValue"]}
    \"\"\"{clean_desc(item)} \"\"\""""

    # classes
    elif model["type"] == "object":
        if "properties" not in model:
            return ""

        text = f"""
@attr.define
class {model["name"]}(BaseModel):
    \"\"\"
    {clean_desc(model)}

    Attributes:"""

        for name, data in model["properties"].items():
            text += f"""
        {capital_case_to_snake_case(name)}: {clean_desc(data)}"""

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


def add_to_import_paths(
    file_imports: set, schema_dict: dict, overwrite_path: str, regular_path: str
) -> tuple[str, str, str, str]:
    if "$ref" not in schema_dict:
        schema_type = schema_dict.get("type", None)
        if schema_type == "array":
            import_path, actual_import_path, model_name, clean_model_name = add_to_import_paths(
                file_imports=file_imports,
                schema_dict=schema_dict["items"],
                overwrite_path=overwrite_path,
                regular_path=regular_path,
            )
            model_name = f"list[{model_name}]"
        else:
            import_path, actual_import_path, = (
                "",
                "",
            )
            model_name = clean_model_name = convert_to_typing(schema_dict, return_class_names=True)

    else:
        import_path, model_name = get_import_name_from_ref(schema_dict["$ref"])
        clean_model_name = model_name

        actual_import_path = f"{overwrite_path}.{import_path}"
        import_path = "bungio.models"

        # does the model exist
        try:
            imp = importlib.import_module(import_path)
            if not hasattr(imp, model_name):
                raise ModuleNotFoundError
            file_imports.add(f"from {import_path} import {model_name}")

        # there are some models without any definition, like ClanBannerSource
        except ModuleNotFoundError:
            import_path, actual_import_path, model_name, clean_model_name = "", "", "dict", "dict"

    return import_path, actual_import_path, model_name, clean_model_name


def clean_desc(data: dict) -> str:
    text = data.get("description", "_No description given by bungie_")
    return text.replace("\n", " ").replace("\r", "")


main()

# todo inherited overwrite classes do not display as docs correctly -> https://mkdocstrings.github.io/handlers/overview/#selection-options (inherited members)
# todo docs for BaseType and BaseEnum
# todo options: members: [] does not work -> config/config.md
# todo interface funcs that need enums should actually import them -> BungieMembershipType
