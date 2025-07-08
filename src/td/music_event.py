from __future__ import annotations
from typing import TypedDict
from .event import Event


class MusicEvent(Event, TypedDict, total=False):
    """
    A class representing schema.org's MusicEvent.
    See: https://schema.org/MusicEvent
    """
    pass
