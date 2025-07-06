from __future__ import annotations
from typing import Union, TYPE_CHECKING
from .thing import Thing
from .data_type import DateTime
from enum import Enum

if TYPE_CHECKING:
    from .person import Person
    from .organization import Organization
    from .place import Place
    from .postal_address import PostalAddress
    from .virtual_location import VirtualLocation
    from .entry_point import EntryPoint
    # Text is just str, so no import needed


class ActionStatusType(Enum):
    ACTIVE = "ActiveActionStatus"
    COMPLETED = "CompletedActionStatus"
    FAILED = "FailedActionStatus"
    POTENTIAL = "PotentialActionStatus"


class Action(Thing, total=False):
    """
    A class representing schema.org's Action.
    See: https://schema.org/Action
    """
    actionStatus: ActionStatusType  # Indicates the current disposition of the Action.
    # The direct performer or driver of the action (animate or inanimate).
    agent: Union[Person, Organization]
    endTime: DateTime  # The end time of something.
    # For failed actions, more information on the cause of the failure.
    error: Thing
    # The object that helped the agent perform the action.
    instrument: Thing
    # The location of for example where the event is happening, an organization is located, or where an
    # action takes place.
    location: Union[Place, str, PostalAddress, VirtualLocation]
    # The object upon which the action is carried out, whose state is kept intact or changed.
    object: Thing
    # Other co-agents that participated in the action indirectly.
    participant: Union[Person, Organization]
    result: Thing  # The result produced in the action.
    startTime: DateTime  # The start time of something.
    # Indicates a target EntryPoint for an Action.
    target: EntryPoint
