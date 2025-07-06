from __future__ import annotations
from .event import Event


class MusicEvent(Event, total=False):
    """
    A class representing schema.org's MusicEvent.
    See: https://schema.org/MusicEvent
    """
    # No additional fields; inherits all from Event.
