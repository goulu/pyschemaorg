
from datetime import datetime
from typing import List, Optional, Union
from .thing import Intangible


class Schedule(Intangible, total=False):
    """
    A class representing .org's Schedule.
    See: https://.org/Schedule
    """
    byDay: Optional[Union[str, List[str]]]
    byMonth: Optional[Union[int, List[int]]]
    byMonthDay: Optional[Union[int, List[int]]]
    byMonthWeek: Optional[Union[int, List[int]]]
    duration: Optional[str]
    endDate: Optional[Union[datetime, str]]
    exceptDate: Optional[Union[datetime, str, List[Union[datetime, str]]]]
    repeatCount: Optional[int]
    repeatFrequency: Optional[str]
    repeatInterval: Optional[int]
    scheduleTimezone: Optional[str]
    startDate: Optional[Union[datetime, str]]
