import attr

from bungio.api.bungie.app import AppRouteInterface


@attr.define
class AppRouteInterfaceOverwrite(AppRouteInterface):
    pass
