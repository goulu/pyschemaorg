from typing import TypedDict, Optional, List, Union

from .action import Action

from .media_object import ImageObject
from .creative_work import CreativeWork
from .event import Event
from .values import PropertyValue

URL = str
Text = str


class BaseTypedDict(TypedDict, total=False):
    """Base for .org types, including common JSON-LD fields."""
    context: Union[str, dict]  # Represents @context
    id: str       # Represents @id
    type: Union[str, List[str]]  # Represents @type


class Thing(BaseTypedDict, total=False):
    """
    A base class representing .org's Thing.
    See: https://.org/Thing
    """
    name: Optional[Text]  # The name of the item.
    description: Optional[Text]  # A description of the item.
    url: Optional[URL]  # URL of the item.
    # URL of a reference Web page that unambiguously indicates the item's identity.
    sameAs: Optional[URL]
    # The identifier property represents any kind of identifier for any kind of Thing.
    identifier: Optional[Union[Text, URL, 'PropertyValue']]
    # An image of the item. This can be a URL or a fully described ImageObject.
    image: Optional[Union[URL, ImageObject]]
    alternateName: Optional[Text]  # An alias for the item.
    # A short description of the item used to disambiguate from other, similar items.
    disambiguatingDescription: Optional[Text]
    # A CreativeWork or Event about this Thing.
    subjectOf: Optional[Union['CreativeWork', 'Event']]
    # Indicates a page (or other CreativeWork) for which this thing is the main entity being described.
    mainEntityOfPage: Optional[Union[URL, 'CreativeWork']]
    # An additional type for the item, typically used for adding more specific types from external vocabularies.
    additionalType: Optional[Union[Text, URL]]
    # Indicates a potential Action, which describes an idealized action in which this thing would play an 'object' role.
    potentialAction: Optional['Action']


class Intangible(Thing, total=False):
    """
    A class representing .org's Intangible.
    See: https://.org/Intangible
    """
    pass  # A utility class that serves as the parent for intangible things.
