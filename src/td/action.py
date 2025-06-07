from datetime import datetime
from typing import Optional, Union

from .creative_work import SoftwareApplication
from .thing import URL, Thing, Text
from .organization import Organization
from .person import Person
from .place import Place, PostalAddress, VirtualLocation

import enum


class EntryPoint(Thing, total=False):
    """
    A class representing .org's EntryPoint.
    An entry point, within some Web-based protocol.
    See: https://.org/EntryPoint
    """
    actionApplication: Optional['SoftwareApplication']  # An application that can complete the request.
    # The high level platform(s) where the Action can be performed for the given URL.
    # To specify a specific application or operating system instance, use actionApplication.
    actionPlatform: Optional[Union[Text, URL]]
    # The supported content type(s) for an EntryPoint response.
    contentType: Optional[Text]
    # The supported encoding type(s) for an EntryPoint response.
    encodingType: Optional[Text]
    # An HTTP method that specifies the appropriate HTTP method for a request to an HTTP EntryPoint.
    # Values are capitalized strings as used in HTTP.
    httpMethod: Optional[Text]
    # An url template (RFC6570) that will be used to construct the target of the execution of the action.
    urlTemplate: Optional[Text]


class ActionStatusType(enum.Enum):
    ACTIVE = "ActiveActionStatus"
    COMPLETED = "CompletedActionStatus"
    FAILED = "FailedActionStatus"
    POTENTIAL = "PotentialActionStatus"


class Action(Thing, total=False):
    """
    A class representing .org's Action.
    See: https://.org/Action
    """
    actionStatus: Optional[ActionStatusType]  # Indicates the current disposition of the Action.
    # The direct performer or driver of the action (animate or inanimate).
    agent: Optional[Union[Person, Organization]]
    endTime: Optional[datetime]  # The end time of something.
    # For failed actions, more information on the cause of the failure.
    error: Optional['Thing']
    # The object that helped the agent perform the action.
    instrument: Optional['Thing']
    # The location of for example where the event is happening, an organization is located, or where an action takes place.
    location: Optional[Union[Place, Text, PostalAddress, VirtualLocation]]
    # The object upon which the action is carried out, whose state is kept intact or changed.
    object: Optional['Thing']
    # Other co-agents that participated in the action indirectly.
    participant: Optional[Union[Person, Organization]]
    result: Optional['Thing']  # The result produced in the action.
    startTime: Optional[datetime]  # The start time of something.
    # Indicates a target EntryPoint for an Action.
    target: Optional[EntryPoint]
