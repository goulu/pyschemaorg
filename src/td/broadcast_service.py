from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict, Union, List
from .service import Service

if TYPE_CHECKING:
    from .organization import Organization
    from .broadcast_channel import BroadcastChannel


class BroadcastService(Service, TypedDict, total=False):
    """
    A class representing schema.org's BroadcastService.
    See: https://schema.org/BroadcastService
    """
    # The media network(s) whose content is broadcast on this station.
    broadcastAffiliateOf: Organization
    # The name displayed in the channel guide.
    broadcastDisplayName: str
    # The timezone in which the broadcast service is based.
    broadcastTimezone: str
    # The organization owning or operating the broadcast service.
    broadcaster: Organization
    # A broadcast channel of the service.
    hasBroadcastChannel: BroadcastChannel
    # Languages in which the service is available.
    inLanguage: Union[str, List[str]]
    # Parent broadcast service.
    parentService: BroadcastService
    # Video format used.
    videoFormat: str
