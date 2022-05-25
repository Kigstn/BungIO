from bungio.http.routes.app import AppRequests
from bungio.http.routes.community_content import CommunityContentRequests
from bungio.http.routes.content import ContentRequests
from bungio.http.routes.destiny2 import Destiny2Requests
from bungio.http.routes.fireteam import FireteamRequests
from bungio.http.routes.forum import ForumRequests
from bungio.http.routes.get_available_locales import GetAvailableLocalesRequests
from bungio.http.routes.global_alerts import GlobalAlertsRequests
from bungio.http.routes.group_v2 import GroupV2Requests
from bungio.http.routes.settings import SettingsRequests
from bungio.http.routes.social import SocialRequests
from bungio.http.routes.tokens import TokensRequests
from bungio.http.routes.trending import TrendingRequests
from bungio.http.routes.user import UserRequests
from bungio.http.routes.user_system_overrides import UserSystemOverridesRequests


class AllRequests(
    AppRequests,
    UserRequests,
    ContentRequests,
    ForumRequests,
    GroupV2Requests,
    TokensRequests,
    Destiny2Requests,
    CommunityContentRequests,
    TrendingRequests,
    FireteamRequests,
    SocialRequests,
    GetAvailableLocalesRequests,
    SettingsRequests,
    UserSystemOverridesRequests,
    GlobalAlertsRequests,
):
    pass
