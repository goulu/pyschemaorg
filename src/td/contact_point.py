from __future__ import annotations
from typing import TypedDict, Union, List, TYPE_CHECKING
from enum import Enum
from .structured_value import StructuredValue

if TYPE_CHECKING:
    from .place import Place
    from .geo_shape import GeoShape
    from .administrative_area import AdministrativeArea
    from .data_type import Text
    from .language import Language
    from .opening_hours_specification import OpeningHoursSpecification
    from .product import Product


class ContactPointOption(Enum):
    """
    An enumeration of options for a ContactPoint as defined by schema.org.
    See: https://schema.org/ContactPointOption
    """
    TOLL_FREE = "https://schema.org/TollFree"
    HEARING_IMPAIRED_SUPPORTED = "https://schema.org/HearingImpairedSupported"


class ContactPoint(StructuredValue, TypedDict, total=False):
    """
    A class representing schema.org's ContactPoint.
    See: https://schema.org/ContactPoint
    """
    # The geographic area where a service or offered item is provided.
    areaServed: Union[Place, GeoShape, AdministrativeArea, Text]
    # Languages in which a service is available.
    availableLanguage: Union[Text, Language]
    # An option available on this contact point (e.g. toll-free number).
    contactOption: Union[ContactPointOption, List[ContactPointOption]]
    # A person or organization can have different contact points, for different purposes.
    contactType: str
    # Email address for the contact point.
    email: str
    # The fax number.
    faxNumber: str
    # The hours during which this contact point is available.
    hoursAvailable: OpeningHoursSpecification
    # The product or service supported by this contact point.
    productSupported: Union[str, Product]
    # The telephone number.
    telephone: str
