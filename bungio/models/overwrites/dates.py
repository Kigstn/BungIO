import attr

from bungio.models.bungie.dates import DateRange


@attr.define
class DateRangeOverwrite(DateRange):
    pass
