from __future__ import annotations
from datetime import datetime
from typing import Union

from .creative_work import SoftwareApplication
from .thing import URL, Thing, Text
from .organization import Organization
from .person import Person
from .place import Place, PostalAddress, VirtualLocation

import enum


class EntryPoint(Thing, total=False):
    """
    A class representing schema.org's EntryPoint.
    An entry point, within some Web-based protocol.
    See: https://schema.org/EntryPoint
    """
    actionApplication: SoftwareApplication  # An application that can complete the request.
    # The high level platform(s) where the Action can be performed for the given URL.
    # To specify a specific application or operating system instance, use actionApplication.
    actionPlatform: Union[Text, URL]
    # The supported content type(s) for an EntryPoint response.
    contentType: Text
    # The supported encoding type(s) for an EntryPoint response.
    encodingType: Text
    # An HTTP method that specifies the appropriate HTTP method for a request to an HTTP EntryPoint.
    # Values are capitalized strings as used in HTTP.
    httpMethod: Text
    # An url template (RFC6570) that will be used to construct the target of the execution of the action.
    urlTemplate: Text


class ActionStatusType(enum.Enum):
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
    endTime: datetime  # The end time of something.
    # For failed actions, more information on the cause of the failure.
    error: Thing
    # The object that helped the agent perform the action.
    instrument: Thing
    # The location of for example where the event is happening, an organization is located, or where an action takes place.
    location: Union[Place, Text,
                    PostalAddress, VirtualLocation]
    # The object upon which the action is carried out, whose state is kept intact or changed.
    object: Thing
    # Other co-agents that participated in the action indirectly.
    participant: Union[Person, Organization]
    result: Thing  # The result produced in the action.
    startTime: datetime  # The start time of something.

    # Indicates a target EntryPoint for an Action.
    target: EntryPoint
