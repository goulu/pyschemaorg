from __future__ import annotations
from typing import Optional, Union
from datetime import date, time, datetime, timedelta
from .values import StructuredValue
from .enums import DayOfWeek  # Assuming DayOfWeek is defined in enums module

Date = date
Time = time
DateTime = datetime
Duration = timedelta


class OpeningHoursSpecification(StructuredValue, total=False):
    """
    A class representing schema.org's OpeningHoursSpecification.
    See: https://schema.org/OpeningHoursSpecification
    """
    # The closing hour of the place or service on the given day(s) of the week.
    closes: Optional[time]
    # The day of the week for which these opening hours are valid.
    dayOfWeek: Optional[DayOfWeek]
    # The opening hour of the place or service on the given day(s) of the week.
    opens: Optional[time]
    # The date when the item becomes valid.
    validFrom: Optional[Union[date, datetime]]
    # The date after when the item is not valid.
    validThrough: Optional[Union[date, datetime]]
