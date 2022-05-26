import os
import re

import requests

from bungio.definitions import ROOT_DIR


def main():
    base_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bungio/http/routes")

    resp = requests.get(url="https://raw.githubusercontent.com/Bungie-net/api/master/openapi.json")
    api_schema = resp.json()

    topics = {}
    for path, data in api_schema["paths"].items():
        topic = path.split("/")[1]
        if topic not in topics:
            topics[topic] = {}
        topics[topic][path] = data

    names = {}
    for topic, routes in topics.items():
        text = f"""import datetime
from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class {topic}Requests:
    request: Callable[..., Coroutine]
    """

        for path, data in routes.items():
            text += generate_function(path, data)
        file_path = os.path.join(base_path, f"{capital_case_to_snake_case(topic)}.py")
        with open(file_path, "w") as file:
            file.write(text)

        relative_path = os.path.relpath(file_path, ROOT_DIR).replace(".py", "").replace(os.sep, ".")
        names[f"{topic}Requests"] = relative_path

        docs_path = os.path.join(
            ROOT_DIR, f"docs/src/API Reference/HTTP/Bungie Routes/{capital_case_to_snake_case(topic)}.md"
        )
        with open(docs_path, "w") as file:
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
    with open(os.path.join(base_path, "__init__.py"), "w") as file:
        file.write(init_text)

    os.system(f"""black "{base_path}\"""")


def generate_function(path: str, data: dict) -> str:
    text = f"""
    async def {capital_case_to_snake_case(data["summary"].split(".")[1])}(self"""

    method = "get" if "get" in data else "post"

    security = None
    if "security" in data[method]:
        security = f"""Required oauth2 scopes: {", ".join(data[method]["security"][0]["oauth2"])}"""

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

        if "format" not in param["schema"]:
            arg_format = param["schema"]["type"]
        else:
            arg_format = param["schema"]["format"]

        match arg_format:
            case "int32" | "int64" | "byte" | "uint32":
                arg_type = "int"
            case "string":
                arg_type = "str"
            case "boolean":
                arg_type = "bool"
            case "date-time":
                arg_type = "datetime.datetime"
            case "array":
                arg_type = "list[int]"
            case _:
                raise ValueError(arg_format)

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

    for param in params:
        text += f""", {param["name"]}: {param["type"]}"""

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

    for param in params:
        text += f"""
            {param["name"]}: {param["description"]}"""

    # todo what errors do they raise

    text += f"""

        Returns:
            The json response
        \"\"\"

        return await self.request(Route(path=f"{path}", method="{method.upper()}\""""

    for param in params:
        if param["in"] != "path":
            text += f""", {param["name"]}={param["name"]}"""

    text += """))

    """

    return text


def capital_case_to_snake_case(string: str) -> str:
    string = f"{string[0].upper()}{string[1:]}"
    return "_".join(re.findall("[A-Z][^A-Z]*", string)).lower()


main()
