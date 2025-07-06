from __future__ import annotations
from typing import TypedDict, Union, Tuple, List, TYPE_CHECKING
from .data_type import Text

from .structured_value import StructuredValue
if TYPE_CHECKING:
    from .geo_coordinates import _GeoPoint
    from .postal_address import PostalAddress
    from .country import Country
    from .place import Place


class _GeoBox(TypedDict, total=False):
    # extension to make reading from WikiData easier
    north: Union[float, str]
    south: Union[float, str]
    east: Union[float, str]
    west: Union[float, str]


# GeoShape: https://schema.org/GeoShape
class GeoShape(StructuredValue, TypedDict, total=False):
    """
    A class representing schema.org's GeoShape.
    See: https://schema.sorg/GeoShape
    """
    # Physical address of the item.
    address: Union[str, PostalAddress]  # Physical address of the item.
    # The country. For example, the country where the person is located or a product is available.
    addressCountry: Union[str, Country]
    # A box is the area enclosed by the rectangle formed by two points. The first point is the lower
    # corner, the second point is the upper corner. A box is expressed as two points separated by a
    # space character.
    box: Union[_GeoBox, Tuple[_GeoPoint, _GeoPoint], Text]
    # A circle is the area enclosed by a circle centered on a point with a given radius. A circle is
    # expressed as a pair followed by a radius in meters.
    circle: Union[Tuple[_GeoPoint, float], Text]
    # A line is a point-to-point path consisting of two or more points. A line is expressed as a
    # series of two or more point pairs.
    line: Union[Tuple[_GeoPoint, _GeoPoint], Text]
    # A polygon is the area enclosed by a point-to-point path for which the starting and ending points
    # are the same. A polygon is expressed as a series of four or more space delimited points where
    # the first and final points are identical.
    polygon: Union[List[_GeoPoint], Text]
    # The postal code. For example, 94043.
    postalCode: str  # The postal code.
    # The geo relationship between this place and another place.
    geoEquals: 'Place'
    # The geo relationship between this place and another place.
    geoDisjoint: 'Place'
    # The geo relationship between this place and another place.
    geoIntersects: 'Place'
    # The geo relationship between this place and another place.
    geoTouches: 'Place'
    # The geo relationship between this place and another place.
    geoCrosses: 'Place'
    # The geo relationship between this place and another place.
    geoWithin: 'Place'
    # The geo relationship between this place and another place.
    geoContains: 'Place'
    # The geo relationship between this place and another place.
    geoCoveredBy: 'Place'
    # The geo relationship between this place and another place.
    geoCovers: 'Place'
    # The geo relationship between this place and another place.
    geoOverlaps: 'Place'
