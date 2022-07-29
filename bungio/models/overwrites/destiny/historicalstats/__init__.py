from typing import TYPE_CHECKING, Optional

from bungio.models.base import custom_define
from bungio.models.bungie.destiny import historicalstats

if TYPE_CHECKING:
    from bungio.models import AuthData, DestinyPostGameCarnageReportData


@custom_define()
class DestinyHistoricalStatsPeriodGroup(historicalstats.OverwrittenDestinyHistoricalStatsPeriodGroup):
    """
    _No description given by bungie._

    None
    Attributes:
        activity_details: If the period group is for a specific activity, this property will be set.
        period: Period for the group. If the stat periodType is day, then this will have a specific day. If the type is monthly, then this value will be the first day of the applicable month. This value is not set when the periodType is 'all time'.
        values: Collection of stats for the period.
    """

    async def get_post_game_carnage_report(
        self, auth: Optional["AuthData"] = None
    ) -> "DestinyPostGameCarnageReportData":
        """
        Gets the available post game carnage report for this activity.

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """
        return await self._client.api.get_post_game_carnage_report(
            activity_id=self.activity_details.instance_id, auth=auth
        )
