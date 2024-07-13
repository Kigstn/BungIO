from bungio.http.routes.app import AppRouteHttpRequests
from bungio.http.routes.user import UserRouteHttpRequests
from bungio.http.routes.content import ContentRouteHttpRequests
from bungio.http.routes.forum import ForumRouteHttpRequests
from bungio.http.routes.group_v2 import GroupV2RouteHttpRequests
from bungio.http.routes.tokens import TokensRouteHttpRequests
from bungio.http.routes.destiny2 import Destiny2RouteHttpRequests
from bungio.http.routes.community_content import CommunityContentRouteHttpRequests
from bungio.http.routes.trending import TrendingRouteHttpRequests
from bungio.http.routes.fireteam import FireteamRouteHttpRequests
from bungio.http.routes.fireteam_finder import FireteamFinderRouteHttpRequests
from bungio.http.routes.social import SocialRouteHttpRequests
from bungio.http.routes.get_available_locales import GetAvailableLocalesRouteHttpRequests
from bungio.http.routes.settings import SettingsRouteHttpRequests
from bungio.http.routes.user_system_overrides import UserSystemOverridesRouteHttpRequests
from bungio.http.routes.global_alerts import GlobalAlertsRouteHttpRequests


class AllRouteHttpRequests(
    AppRouteHttpRequests,
    UserRouteHttpRequests,
    ContentRouteHttpRequests,
    ForumRouteHttpRequests,
    GroupV2RouteHttpRequests,
    TokensRouteHttpRequests,
    Destiny2RouteHttpRequests,
    CommunityContentRouteHttpRequests,
    TrendingRouteHttpRequests,
    FireteamRouteHttpRequests,
    FireteamFinderRouteHttpRequests,
    SocialRouteHttpRequests,
    GetAvailableLocalesRouteHttpRequests,
    SettingsRouteHttpRequests,
    UserSystemOverridesRouteHttpRequests,
    GlobalAlertsRouteHttpRequests,
):
    pass
