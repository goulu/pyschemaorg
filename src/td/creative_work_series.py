from __future__ import annotations
from typing import Union
from .creative_work import CreativeWork
from .data_type import DateTime


class CreativeWorkSeries(CreativeWork, total=False):
    """
    A class representing schema.org's CreativeWorkSeries.
    See: https://schema.org/CreativeWorkSeries
    """
    endDate: Union[str, 'DateTime']
    issn: str
    startDate: Union[str, 'DateTime']
