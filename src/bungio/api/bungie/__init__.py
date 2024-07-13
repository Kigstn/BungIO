from bungio.api.bungie.app import AppRouteInterface
from bungio.api.bungie.user import UserRouteInterface
from bungio.api.bungie.content import ContentRouteInterface
from bungio.api.bungie.forum import ForumRouteInterface
from bungio.api.bungie.group_v2 import GroupV2RouteInterface
from bungio.api.bungie.tokens import TokensRouteInterface
from bungio.api.bungie.community_content import CommunityContentRouteInterface
from bungio.api.bungie.trending import TrendingRouteInterface
from bungio.api.bungie.fireteam import FireteamRouteInterface
from bungio.api.bungie.fireteam_finder import FireteamFinderRouteInterface
from bungio.api.bungie.social import SocialRouteInterface
from bungio.api.bungie.get_available_locales import GetAvailableLocalesRouteInterface
from bungio.api.bungie.settings import SettingsRouteInterface
from bungio.api.bungie.user_system_overrides import UserSystemOverridesRouteInterface
from bungio.api.bungie.global_alerts import GlobalAlertsRouteInterface


class AllRouteInterfaces(
    AppRouteInterface,
    UserRouteInterface,
    ContentRouteInterface,
    ForumRouteInterface,
    GroupV2RouteInterface,
    TokensRouteInterface,
    CommunityContentRouteInterface,
    TrendingRouteInterface,
    FireteamRouteInterface,
    FireteamFinderRouteInterface,
    SocialRouteInterface,
    GetAvailableLocalesRouteInterface,
    SettingsRouteInterface,
    UserSystemOverridesRouteInterface,
    GlobalAlertsRouteInterface,
):
    pass
