from __future__ import annotations
from typing import Union

from .data_type import Date, Time, DateTime
from .enums import DayOfWeek  # Assuming DayOfWeek is defined in enums module
from .structured_value import StructuredValue


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
