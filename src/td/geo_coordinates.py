from __future__ import annotations
from typing import TypedDict, Union
from .structured_value import StructuredValue
from .postal_address import PostalAddress
from .country import Country


class _GeoPoint(TypedDict, total=False):
    """
    A class representing a point in geographic coordinates.
    This is used internally to represent latitude and longitude.
    """
    latitude: Union[float, str]
    longitude: Union[float, str]


class GeoCoordinates(StructuredValue, _GeoPoint, TypedDict, total=False):
    """
    A class representing schema.org's GeoCoordinates.
    The geographic coordinates of a place or event.
    See: https://schema.org/GeoCoordinates
    """
    address: Union[str, PostalAddress]
    addressCountry: Union[str, Country]
    postalCode: str
    elevation: Union[float, str]
