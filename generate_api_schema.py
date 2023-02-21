# do not touch, very clunky black magic
import copy
import importlib
import os
import re
from collections import namedtuple
from typing import Optional

import requests

from bungio.definitions import ROOT_DIR

Typing = namedtuple("Typing", "name manifest enum_type int64")

mixin_params = {
    "DestinyCharacterMixin": [
        "character_id",
        "membership_id",
        "membership_type",
    ],
    "DestinyUserMixin": [
        "membership_id",
        "membership_type",
    ],
    "DestinyClanMixin": [
        "group_id",
    ],
}
mixins: dict[str, dict[str, list[str] | set]] = {}


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
        mixins=mixins,
    )

    generate_mixins(folder_path="bungio/models/mixins")

    # regen models to include mixins
    generate_models(api_schema)


def generate_mixins(folder_path: str):
    base_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), folder_path)

    for name, data in mixins.items():
        path_name = name.removeprefix("Destiny").removesuffix("Mixin").lower()
        file_path = os.path.join(base_path, f"{path_name}.py")

        skip_line = False
        with open(file_path, "r", encoding="utf-8") as file:
            text = ""
            for line in file.readlines():
                if not skip_line:
                    text += line
                if "AUTOMATIC IMPORTS START" in line:
                    text += "%imports%\n"
                    skip_line = True
                elif "AUTOMATIC IMPORTS END" in line:
                    text += line
                    skip_line = False
                elif "DO NOT CHANGE ANY CODE BELOW" in line:
                    break
            text += "\n".join(data["functions"])
            text = text.replace("%imports%", "\n".join(data["imports"]))
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)

    os.system(f"""black "{base_path}\"""")
    os.system(f"""git add "{base_path}\"""")


def generate_functions(
    api_schema: dict,
    folder_path: str,
    docs_path: str,
    create_raw_http: bool = True,
    mixins: Optional[dict] = None,
):
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
            text = f"""from datetime import datetime
from typing import Callable, Coroutine, Optional, Any, Union

from bungio.http.route import Route
from bungio.models.auth import AuthData


class {name}:
    request: Callable[..., Coroutine]
    """

        else:
            name = f"{topic}RouteInterface"
            text = f"""# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import Optional, Any, Union

from bungio.models.base import ClientMixin, custom_define, custom_field
from bungio.models.auth import AuthData
from bungio.utils import AllowAsyncIteration

%imports%

@custom_define()
class {name}(ClientMixin):
    """

        for path, data in routes.items():
            text += generate_function(
                path,
                data,
                api_schema,
                create_raw_http=create_raw_http,
                file_imports=file_imports,
                mixins=mixins,
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
                importlib.import_module(overwrite_import_path, name)
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


def generate_function(
    path: str,
    data: dict,
    full_data: dict,
    file_imports: set,
    create_raw_http: bool,
    mixins: Optional[dict] = None,
) -> str:
    # make the class text
    func_name = capital_case_to_snake_case(data["summary"].split(".")[1])
    text = f"""
    async def {func_name}(self"""
    mixin_text = text
    mixin_imports = set()

    method = "get" if "get" in data else "post"

    security = None
    if "security" in data[method]:
        security = f"""Required oauth2 scopes: {", ".join(data[method]["security"][0]["oauth2"])}"""

    # json body info
    body = []
    m_body = []
    if "requestBody" in data[method]:
        schema_data = data[method]["requestBody"]["content"]["application/json"]["schema"]

        if create_raw_http:
            if "$ref" in schema_data:
                schema_name = schema_data["$ref"]
                schema_name = schema_name.split("/")[-1]
                schema_data = full_data["components"]["schemas"][schema_name]["properties"]

                for name, value in schema_data.items():
                    arg_type = convert_to_typing(value).name
                    body.append(
                        {
                            "name": capital_case_to_snake_case(name),
                            "og_name": name,
                            "description": clean_desc(value),
                            "type": arg_type,
                            "append": "",
                        }
                    )

            else:
                arg_type = convert_to_typing(schema_data).name
                body.append(
                    {
                        "name": "body_data",
                        "description": clean_desc(schema_data),
                        "type": arg_type,
                        "append": "",
                    }
                )
        else:
            arg_type = convert_to_typing(data=schema_data, return_class_names=True, file_imports=file_imports).name
            m_arg_type = convert_to_typing(
                data=schema_data, return_class_names=True, type_checking_imports=True, mixin_imports=mixin_imports
            ).name

            body.append({"name": "data", "description": "The required data for this request.", "type": arg_type})
            m_body.append({"name": "data", "description": "The required data for this request.", "type": m_arg_type})

    # path / query params
    params = []
    m_params = []
    for param in data[method]["parameters"]:
        new_name = capital_case_to_snake_case(param["name"])
        if (string := f"""{{{param["name"]}}}""") in path:
            path = path.replace(string, f"""{{{new_name}}}""")

        info = {
            "name": new_name,
            "description": clean_desc(param),
            "in": param["in"],
            "format": "{name}",
        }

        if create_raw_http:
            arg_type = convert_to_typing(param["schema"])
            arg_type = arg_type.name if not arg_type.enum_type else "int"
            m_arg_type = None
        else:
            arg_type = convert_to_typing(param["schema"], return_class_names=True, file_imports=file_imports).name
            m_arg_type = convert_to_typing(
                param["schema"], return_class_names=True, type_checking_imports=True, mixin_imports=mixin_imports
            ).name

            is_optional = info["in"] == "query"
            is_list = False
            clean_arg_type = arg_type
            if "Optional[" in arg_type:
                clean_arg_type = clean_arg_type.removesuffix("]").removeprefix("Optional[")
                is_optional = True

            if "list[" in arg_type:
                clean_arg_type = clean_arg_type.removesuffix("]").removeprefix("list[")
                is_list = True

            if "Union[" in arg_type and "Union[int, str]" not in arg_type:
                clean_arg_type = clean_arg_type.removesuffix(", int]").removeprefix("Union[")

            if any(clean_arg_type in imports for imports in file_imports):
                if is_list:
                    info["format"] = """[getattr(x, "value", x) for x in {name}]"""
                else:
                    info["format"] = """getattr({name}, "value", {name})"""

            if is_optional:
                info["format"] = f"""{info["format"]} if {info["name"]} is not None else None"""

        if info["in"] == "query":
            arg_type = f"Optional[{arg_type}] = None"
        m_info = copy.copy(info)
        info["type"] = arg_type
        m_info["type"] = m_arg_type

        params.append(info)
        m_params.append(m_info)

    security_info = {
        "name": "auth",
        "format": "{name}",
    }
    if security:
        security_info["description"] = "Authentication information."
        security_info["type"] = "AuthData"
        security_info["in"] = "pb"  # we sort by alphabet, so this is after "page" and before "query"
    else:
        security_info[
            "description"
        ] = "Authentication information. Required when users with a private profile are queried, or when Bungie feels like it"
        security_info["type"] = "Optional[AuthData] = None"
        security_info["in"] = "query"
    params.append(security_info)
    params = sorted(params, key=lambda x: x["in"])

    m_security_info = copy.copy(security_info)
    m_security_info["type"] = m_security_info["type"].replace("AuthData", '"AuthData"')
    m_params.append(m_security_info)
    m_params = sorted(m_params, key=lambda x: x["in"])

    # does the mixin need this function
    found_mixin_name = None
    found_mixin_params = {}
    if mixins is not None:
        param_names = [item["name"] for item in body + params]
        for mixin_name, mixin_required in mixin_params.items():
            found_mixin_params = {}
            all_found = []
            for mixin_required_name in mixin_required:
                found = False
                for param_name in param_names:
                    if mixin_required_name in param_name:
                        found_mixin_params[param_name] = mixin_required_name
                        found = True
                        break
                all_found.append(found)
            if all(all_found):
                found_mixin_name = mixin_name
                if found_mixin_name not in mixins:
                    mixins[found_mixin_name] = {"functions": [], "imports": set()}
                break

    for item in body + params:  # noqa
        text += f""", {item["name"]}: {item["type"]}"""
    if create_raw_http:
        text += ", *args, **kwargs"

    for item in m_body + m_params:  # noqa
        if found_mixin_name:
            if item["name"] not in found_mixin_params:
                mixin_text += f""", {item["name"]}: {item["type"]}"""

    if create_raw_http:
        return_model = "dict"
        m_return_model = None
    else:
        return_schema = data[method]["responses"]["200"]["$ref"]
        return_info = full_data["components"]["responses"][return_schema.split("/")[-1]]["content"]["application/json"][
            "schema"
        ]["properties"]["Response"]

        # try to get the overwrite path if that exists and add that to the imports
        return_model = convert_to_typing(
            data=return_info, return_class_names=True, file_imports=file_imports, return_enum_as_union=False
        )
        m_return_model = convert_to_typing(
            data=return_info,
            return_class_names=True,
            type_checking_imports=True,
            mixin_imports=mixin_imports,
            return_enum_as_union=False,
        )

        # catch enums
        if enum_type := return_model.enum_type:
            enum_type = enum_type.replace('"', "")
            return_model = return_model.name.replace(f"""Union[{enum_type}, int]""", enum_type)
        else:
            return_model = return_model.name
        if enum_type := m_return_model.enum_type:
            enum_type = enum_type.replace('"', "")
            m_return_model = m_return_model.name.replace(f"""Union[{enum_type}, int]""", enum_type)
        else:
            m_return_model = m_return_model.name

    text += f""") -> {return_model}:
        \"\"\"
        {data["description"]}
        """
    mixin_text += f""") -> {m_return_model}:
        \"\"\"
        {data["description"]}
        """

    if security:
        t = f"""
        Warning: Requires Authentication.
            {security}
        """
        text += t
        mixin_text += t

    t = """
        Args:"""
    text += t
    mixin_text += t

    for item in body + params:  # noqa
        t = f"""
            {item["name"]}: {item["description"]}"""
        text += t
        if found_mixin_name:
            if item["name"] not in found_mixin_params:
                mixin_text += t

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
        t = f"""

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        \"\"\"

        """
        text += t
        mixin_text += t

        if found_mixin_name:
            p = []
            for item in body + params:  # noqa
                if item["name"] not in found_mixin_params:
                    p.append(f"""{item["name"]}={item["name"]}""")
                else:
                    p.append(f"""{item["name"]}=self._fuzzy_getattr(\"{found_mixin_params[item["name"]]}\")""")

            mixin_text += f"""
        return await self._client.api.{func_name}({", ".join(p)})

                """

            mixins[found_mixin_name]["functions"].append(mixin_text)
            mixins[found_mixin_name]["imports"].update(mixin_imports)

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
            request_params.append(f"""{param["name"]}={param["format"].format(name=param["name"])}""")
        if body:
            request_params.append("**data.to_dict(_return_to_bungie_case=False)")

        text += f"""
        response = await self._client.http.{func_name}({", ".join(request_params)})
        """

        text += f"""return {get_return_value_from_typing(return_model=return_model, params=params)}

        """

    return text


def get_return_value_from_typing(return_model: str, params: list[dict]) -> str:
    return_model = return_model.strip()

    if return_model.startswith("list"):
        clean_return_model = return_model.removesuffix("]").removeprefix("list[")
        res = get_return_value_from_typing(return_model=clean_return_model, params=params)

        res = f'''[{res.replace("data=response", "data=value").replace("""response["Response"]""", "value")} for value in response["Response"]]'''

    elif return_model.startswith("dict") and return_model.endswith("]"):
        clean_return_model = ", ".join(return_model.removesuffix("]").removeprefix("dict[").split(", ")[1:])
        res = get_return_value_from_typing(return_model=clean_return_model, params=params)
        if "key" in res and "value" in res:
            res = res.replace("key", "key2").replace("value", "value2")

        res = f'''{{key: {res.replace("data=response", "data=value").replace("""response["Response"]""", "value")} async for key, value in AllowAsyncIteration(response["Response"].items())}}'''

    else:
        if return_model in ["dict", "int", "str", "Any", "float", "bool"]:
            res = """response["Response"]"""
        elif return_model == "datetime":
            res = """datetime.strptime(response["Response"], "%Y-%m-%dT%H:%M:%S%z")"""
        else:
            extra = ", ".join([f"""{item["name"]}={item["name"]}""" for item in params])
            res = (
                f"""await {return_model}.from_dict(data=response, client=self._client{f", {extra}" if extra else ""})"""
            )

    return res


def convert_to_typing(
    data: dict,
    return_class_names: bool = False,
    file_imports: Optional[set] = None,
    type_checking_imports: bool = False,
    model_imports: bool = False,
    mixin_imports: Optional[set] = None,
    enum_type: Optional[str] = None,
    return_enum_as_union: bool = True,
) -> Typing:
    arg_type = []
    is_list = False
    manifest_name = None
    is_int64 = False

    if new_data := data.get("allOf", None):
        assert isinstance(new_data, list)
        assert len(new_data) == 1
        return convert_to_typing(
            data=new_data[0],
            return_class_names=return_class_names,
            file_imports=file_imports,
            type_checking_imports=type_checking_imports,
            model_imports=model_imports,
            mixin_imports=mixin_imports,
            enum_type=enum_type,
            return_enum_as_union=return_enum_as_union,
        )

    if (dict_data := data.get("x-dictionary-key", None)) and (new_data := data.get("additionalProperties", None)):
        data_type = convert_to_typing(
            data=new_data,
            return_class_names=return_class_names,
            file_imports=file_imports,
            type_checking_imports=type_checking_imports,
            model_imports=model_imports,
            mixin_imports=mixin_imports,
            enum_type=enum_type,
            return_enum_as_union=return_enum_as_union,
        )
        res = convert_to_typing(
            data=dict_data,
            return_class_names=return_class_names,
            file_imports=file_imports,
            type_checking_imports=type_checking_imports,
            model_imports=model_imports,
            mixin_imports=mixin_imports,
            enum_type=enum_type,
            return_enum_as_union=return_enum_as_union,
        )
        return Typing(f"""dict[{res.name}, {data_type.name}]""", data_type.manifest, None, is_int64)

    if new_data := data.get("$ref", None):
        if return_class_names:
            _, import_name = get_import_name_from_ref(new_data)
            import_path = "bungio.models"

            # does the model exist
            try:
                imp = importlib.import_module(import_path)
                if not hasattr(imp, import_name):
                    raise ModuleNotFoundError

                import_text = f"""{"    " if type_checking_imports else ""}from {import_path} import {import_name}"""

                if isinstance(file_imports, set):
                    file_imports.add(import_text)
                if isinstance(mixin_imports, set):
                    mixin_imports.add(import_text)
                if model_imports:
                    import_name = f"models.{import_name}"
                if type_checking_imports:
                    import_name = f'"{import_name}"'

            # there are some models without any definition, like ClanBannerSource
            except ModuleNotFoundError:
                import_name = "dict"

            return Typing(import_name, None, enum_type, is_int64)
        else:
            return Typing("Any", None, enum_type, is_int64)

    if new_data := data.get("x-enum-reference", None):
        ref_arg_type = convert_to_typing(
            data=new_data,
            return_class_names=return_class_names,
            file_imports=file_imports,
            type_checking_imports=type_checking_imports,
            model_imports=model_imports,
            mixin_imports=mixin_imports,
            enum_type=enum_type,
            return_enum_as_union=return_enum_as_union,
        )
        if return_enum_as_union:
            arg_type.append(f"Union[{ref_arg_type.name}, int]")
        else:
            arg_type.append(ref_arg_type.name)
        enum_type = f"""\"{ref_arg_type.name.replace("models.", "").replace('"', "")}\""""

    else:
        if new_data := data.get("x-mapped-definition", None):
            ref_arg_type = convert_to_typing(
                data=new_data,
                return_class_names=return_class_names,
                file_imports=file_imports,
                type_checking_imports=type_checking_imports,
                model_imports=model_imports,
                mixin_imports=mixin_imports,
                enum_type=enum_type,
                return_enum_as_union=return_enum_as_union,
            )
            manifest_name = ref_arg_type.name

        if "format" not in data:
            arg_format = data["type"]
        else:
            arg_format = data["format"]

        match arg_format:
            case "int16" | "int32" | "byte" | "uint32":
                arg_type.append("int")
            case "int64":
                arg_type.append("int")
                is_int64 = True
            case "double" | "float":
                arg_type.append("float")
            case "string":
                arg_type.append("str")
            case "boolean":
                arg_type.append("bool")
            case "date-time":
                arg_type.append("datetime")
            case "array":
                array_type = convert_to_typing(
                    data["items"],
                    return_class_names=return_class_names,
                    file_imports=file_imports,
                    type_checking_imports=type_checking_imports,
                    model_imports=model_imports,
                    mixin_imports=mixin_imports,
                    enum_type=enum_type,
                    return_enum_as_union=return_enum_as_union,
                )
                manifest_name = array_type.manifest
                arg_type.append(array_type.name)
                enum_type = array_type.enum_type
                is_list = True
            case "object":
                arg_type.append("Any")
            case _:
                raise ValueError(arg_format)

    if len(arg_type) == 1:
        return_text = arg_type[0]
    else:
        return_text = f"""Union[{", ".join(arg_type)}]"""
    if is_list:
        return_text = f"list[{return_text}]"
    return Typing(return_text, manifest_name, enum_type, is_int64)


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
        text = f"""# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import Optional, Any, Union, TYPE_CHECKING

from bungio.utils import enum_converter
from bungio.models.base import BaseModel, BaseEnum, BaseFlagEnum, HashObject, ManifestModel, custom_define, custom_field

{"%mixin_imports%" if mixins else ""}
%imports%"""

        file_imports = set()
        mixin_imports = set()
        for model in models:
            model_text = generate_model(api_schema, model, models, path, file_imports, mixin_imports)
            text += f"""
{model_text}
            """

        if mixins:
            text = text.replace("%mixin_imports%", "\n".join(mixin_imports))

        clean_file_imports = set()
        for import_string in file_imports:
            import_name = f"""class {import_string.split("import")[1].strip()}("""
            if import_name not in text:
                clean_file_imports.add(import_string)

        formatted_imports = "\n".join(clean_file_imports)
        if formatted_imports:
            formatted_imports = f"""
if TYPE_CHECKING:
{formatted_imports}"""
        text = text.replace("%imports%", formatted_imports)

        # put files that are also folders in init file
        file_path = os.path.join(base_path, path.replace(".", "/"))
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


def generate_model(
    api_schema: dict, model: dict, models: list[dict], path: str, file_imports: set, mixin_imports: set = None
) -> str:
    # enums
    if data := model.get("x-enum-values", None):
        # bitmask or not
        if model["x-enum-is-bitmask"] is True:
            text = f"""
class {model["name"]}(BaseFlagEnum):"""
        else:
            text = f"""
class {model["name"]}(BaseEnum):"""

        text += f"""
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

        manifest_required = None
        properties = {}
        for name, data in model["properties"].items():
            name = capital_case_to_snake_case(name)
            param_type = convert_to_typing(
                data,
                return_class_names=True,
                file_imports=file_imports,
                type_checking_imports=True,
            )
            data["param_type"] = param_type.name
            data["enum_type"] = param_type.enum_type
            data["description"] = clean_desc(data)
            data["int64"] = param_type.int64

            # write the manifest data as a new attr
            if param_type.manifest:
                new_name = f"manifest_{name}"
                new_data = {
                    "param_type": f"Optional[{param_type.manifest}]",
                    "default": "default=None",
                    "enum_type": None,
                    "description": f"Manifest information for `{capital_case_to_snake_case(name)}`",
                    "int64": False,
                }
                properties[new_name] = new_data

                if not manifest_required:
                    manifest_required = True

            properties[name] = data

        properties = {
            k: v for k, v in sorted(properties.items(), key=lambda x: x[0] if x[1].get("default", None) else f"_{x[0]}")
        }

        if manifest_required:
            manifest_required = """Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)
            """

        # check if mixins can be inherited (if params match)
        mixin_extra = ""
        if mixins:
            for mixin_name, mixin_required in mixin_params.items():
                all_found = []
                for mixin_required_name in mixin_required:
                    found = False
                    for param_name in properties:
                        if mixin_required_name in param_name:
                            found = True
                            break
                    all_found.append(found)
                if all(all_found):
                    mixin_extra = f", {mixin_name}"
                    mixin_imports.add(f"""from bungio.models.mixins import {mixin_name}""")
                    break
        model_name = model["name"]
        try:
            imp = importlib.import_module("bungio.models.overwrites")
            if not hasattr(imp, model_name):
                raise ModuleNotFoundError
            model_name = f"Overwritten{model_name}"
        except ModuleNotFoundError:
            pass

        # does the obj has a hash attr
        hash_extra = "hash" in properties

        text = f"""
@custom_define()
class {model_name}({"BaseModel" if "x-mobile-manifest-name" not in model else "ManifestModel"}{mixin_extra}{", HashObject" if hash_extra else ""}):
    \"\"\"
    {clean_desc(model)}

    {manifest_required}
    Attributes:"""

        for name, data in properties.items():
            text += f"""
        {name}: {data["description"]}"""

        text += """
    \"\"\"
"""
        for name, data in properties.items():
            if name == "hash":
                continue

            field_extras = []
            if data["enum_type"]:
                field_extras.insert(0, f"""converter=enum_converter({data["enum_type"]})""")

            elif "list" in data["param_type"] or "dict" in data["param_type"]:
                list_type = data["param_type"].replace('"', "")
                list_type = re.sub(r"Union\[ *(.+), int\]", r"\1", list_type)
                field_extras.append(
                    f"""metadata={{"type": \"\"\"{list_type}\"\"\"{', "int64": True' if data["int64"] else ""}}}"""
                )

            if data["int64"]:
                field_extras.append(f"""metadata={{"int64": True}}""")

            if default_val := data.get("default", None):
                field_extras.append(default_val)

            field_extras = ", ".join(field_extras)
            text += f"""
    {name}: {data["param_type"]} = custom_field({field_extras})"""

    # arrays
    elif model["type"] == "array":
        return ""

    else:
        raise ValueError(model)

    return text


def clean_desc(data: dict) -> str:
    text = data.get("description", "_No description given by bungie._")
    return text.replace("\n", " ").replace("\r", "").strip()


main()

# todo inherited overwrite classes do not display as docs correctly -> https://mkdocstrings.github.io/handlers/overview/#selection-options (inherited members)
# todo options: members: [] does not work -> config/config.md
