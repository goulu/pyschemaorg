from __future__ import annotations
from typing import Optional, Union

from td.date_time import Date, Time, DateTime, Duration
from td.enums import DayOfWeek
from .thing import Intangible, Text


class Schedule(Intangible, total=False):
    # The day of the week for which the opening hours specification is valid.
    byDay: Optional[Union[DayOfWeek, str]]
    # The month of the year for which the opening hours specification is valid.
    byMonth: Optional[int]
    # The day of the month for which the opening hours specification is valid.
    byMonthDay: Optional[int]
    # The week number of the month for which the opening hours specification is valid.
    byMonthWeek: Optional[int]
    # The duration of the item (e.g. a meeting, a music recording, or a movie).
    duration: Optional[Duration]
    # The end date and time of the item (in ISO 8601 date format).
    endDate: Optional[Union[Date, DateTime]]
    # The end time of the item.
    endTime: Optional[Union[Time, DateTime]]
    # Defines a date or dates when the schedule is not active.
    exceptDate: Optional[Union[Date, DateTime]]
    # Defines the number of times a recurring Event will occur.
    repeatCount: Optional[int]
    # Defines the frequency at which Events will occur.
    repeatFrequency: Optional[Union[Duration, Text]]
    # Indicates the timezone for which the time(s) indicated in the Schedule are given.
    scheduleTimezone: Optional[str]
    # The start date and time of the item (in ISO 8601 date format).
    startDate: Optional[Union[Date, DateTime]]
    # The start time of the item.
    startTime: Optional[Union[Time, DateTime]]
