import attr

from bungio.client import Client
from bungio.models.base import BaseModel

client = Client(client_id="1", client_secret="a", token="b")


@attr.define
class A(BaseModel):
    x: int = attr.field()


@attr.define
class B(BaseModel):
    a: A = attr.field()
    z: int = attr.field()


data = {"a": {"x": 5}, "z": 1}
