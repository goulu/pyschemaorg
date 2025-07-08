from __future__ import annotations
from typing import TypedDict, Union

from .structured_value import StructuredValue
from .software_application import SoftwareApplication
from .web_site import WebSite
from .action import Action


class InteractionCounter(StructuredValue, TypedDict, total=False):
    """
    A class representing schema.org's InteractionCounter.
    A summary of how users have interacted with this CreativeWork.
    See: https://schema.org/InteractionCounter
    """
    interactionService: Union[WebSite, SoftwareApplication]
    interactionType: Action
    userInteractionCount: int
