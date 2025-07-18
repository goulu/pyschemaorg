from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict, Union, List

from .data_type import URL, Text
if TYPE_CHECKING:
    from .creative_work import CreativeWork
    from .event import Event
    from .action import Action

    from .property_value import PropertyValue
    from .image_object import ImageObject


class BaseTypedDict(TypedDict, total=False):
    """Base for schema.org types, including common JSON-LD fields."""
    id: str  # Represents @id
    context: Union[str, dict]  # Represents @context
    type: Union[str, List[str]]  # Represents @type


class Thing(BaseTypedDict, TypedDict, total=False):
    """
    A base class representing schema.org's Thing.
    See: https://schema.org/Thing
    """
    name: Text  # The name of the item.
    description: Text  # A description of the item.
    url: URL  # URL of the item.
    # URL of a reference Web page that unambiguously indicates the items identity.
    sameAs: URL
    # The identifier property represents any kind of identifier for any kind of Thing.
    identifier: Union[Text, URL, PropertyValue]
    # An image of the item. This can be a URL or a fully described ImageObject.
    image: Union[URL, ImageObject]
    alternateName: Text  # An alias for the item.
    # A short description of the item used to disambiguate from other, similar items.
    disambiguatingDescription: Text
    # A CreativeWork or Event about this Thing.
    subjectOf: Union[CreativeWork, Event]
    # Indicates a page (or other CreativeWork) for which this thing is the main entity being described.
    mainEntityOfPage: Union[URL, CreativeWork]
    # An additional type for the item, typically used for adding more specific types from external vocabularies.
    additionalType: Union[Text, URL]
    # Indicates a potential Action, which describes an idealized action in which this thing would play an object role.
    potentialAction: Action


class Intangible(Thing, TypedDict, total=False):
    """
    A class representing schema.org's Intangible.
    See: https://schema.org/Intangible
    """
    pass  # A utility class that serves as the parent for intangible things.


class _Supersedable(Intangible, TypedDict, total=False):
    """
    base class for classes below. not in .org
    """
    supersededBy: Union[Enumeration, Class, Property]


class Enumeration(_Supersedable, TypedDict, total=False):
    """
    Derived from https://.org/Enumeration
    """
    pass


class Class(_Supersedable, TypedDict, total=False):
    """
    Derived from https://.org/Class
    """
    pass


class Property(_Supersedable, total=False):
    """
    Derived from https://.org/Property
    """
    domainIncludes: Class
    rangeIncludes: Class
    inverseOf: Property
