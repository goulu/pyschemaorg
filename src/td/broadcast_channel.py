from __future__ import annotations
from typing import TYPE_CHECKING, Union, List
from .thing import Intangible

if TYPE_CHECKING:
    from .broadcast_frequency_specification import BroadcastFrequencySpecification
    from .broadcast_service import BroadcastService


class BroadcastChannel(Intangible, total=False):
    """
    A class representing schema.org's BroadcastChannel.
    See: https://schema.org/BroadcastChannel

    broadcastChannelId: The unique identifier for the broadcast channel.
    See: https://schema.org/broadcastChannelId
    broadcastFrequency: The frequency used for over-the-air broadcasts.
    See: https://schema.org/broadcastFrequency
    broadcastServiceTier: The service tier of the channel.
    See: https://schema.org/broadcastServiceTier
    genre: Genre of the creative work, broadcast, or channel.
    See: https://schema.org/genre
    inBroadcastLineup: The lineup in which the channel appears.
    See: https://schema.org/inBroadcastLineup
    providesBroadcastService: The broadcast service provided by the channel.
    See: https://schema.org/providesBroadcastService
    """
    broadcastChannelId: str
    broadcastFrequency: Union[str, 'BroadcastFrequencySpecification']
    broadcastServiceTier: str
    genre: Union[str, List[str]]
    inBroadcastLineup: str
    providesBroadcastService: 'BroadcastService'
