from __future__ import annotations
from typing import Union
from .values import StructuredValue
from .enums import DayOfWeek  # Assuming DayOfWeek is defined in enums module

Date = str  # https://schema.org/Date A date value in ISO 8601 date format.
# https://schema.org/Time A point in time recurring on multiple days in the form hh:mm:ss[Z|(+|-)hh:mm] (see XML schema for details).
Time = str
# https://schema.org/DateTime A combination of date and time of day in the form[-]CCYY-MM-DDThh: mm: ss[Z | (+ | -)hh:mm](see Chapter 5.4 of ISO 8601).
DateTime = str
# https://schema.org/Duration Quantity: Duration (use ISO 8601 duration format).
Duration = str


class OpeningHoursSpecification(StructuredValue, total=False):
    """
    A class representing schema.org's OpeningHoursSpecification.
    See: https://schema.org/OpeningHoursSpecification
    """
    # The closing hour of the place or service on the given day(s) of the week.
    closes: Time
    # The day of the week for which these opening hours are valid.
    dayOfWeek: DayOfWeek
    # The opening hour of the place or service on the given day(s) of the week.
    opens: Time
    # The date when the item becomes valid.
    validFrom: Union[Date, DateTime]
    # The date after when the item is not valid.
    validThrough: Union[Date, DateTime]
