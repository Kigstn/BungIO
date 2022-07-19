from bungio.api.bungie import AllRouteInterfaces
from bungio.api.overwrites import AllRouteInterfacesOverwrites

__all__ = ("ApiClient",)


class ApiClient(AllRouteInterfaces, AllRouteInterfacesOverwrites):
    pass
