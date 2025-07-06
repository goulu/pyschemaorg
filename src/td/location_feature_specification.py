from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict, Union

from .data_type import Date, DateTime
from .property_value import PropertyValue
if TYPE_CHECKING:
    from .opening_hours_specification import OpeningHoursSpecification


class LocationFeatureSpecification(PropertyValue, TypedDict, total=False):
    """
    A class representing schema.org's LocationFeatureSpecification.
    Specifies a location feature by providing a structured value representing a feature 
    of an accommodation as a property-value pair.
    See: https://schema.org/LocationFeatureSpecification
    """
    hoursAvailable: OpeningHoursSpecification
    validFrom: Union[Date, DateTime]
    validThrough: Union[Date, DateTime]
