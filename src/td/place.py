from __future__ import annotations
from typing import TypedDict, Union, List, TYPE_CHECKING
from .structured_value import StructuredValue

if TYPE_CHECKING:
    from .aggregate_rating import AggregateRating
    from .location_feature_specification import LocationFeatureSpecification
    from .event import Event
    from .geo_coordinates import GeoCoordinates
    from .geo_shape import GeoShape
    from .map import Map
    from .image_object import ImageObject
    from .photograph import Photograph
    from .opening_hours_specification import OpeningHoursSpecification
    from .review import Review


# Place: https://schema.org/Place
class Place(StructuredValue, TypedDict, total=False):
    """
    A class representing schema.org's Place.
    See: https://schema.org/Place
    """
    # The overall rating, based on a collection of reviews or ratings, of the item.
    aggregateRating: AggregateRating
    # An amenity feature (e.g. a characteristic or service) of the Accommodation.
    amenityFeature: LocationFeatureSpecification
    # A short textual code (also called "store code") that uniquely identifies a place of business.
    branchCode: str
    # The basic containment relation between places.
    containedIn: Place
    # The basic containment relation between places.
    containedInPlace: Place
    # The basic containment relation between places.
    containsPlace: Union[Place, List[Place]]
    # Upcoming or past event associated with this place, organization, or action.
    event: Event
    # The fax number.
    faxNumber: str
    # The geo coordinates of the place.
    geo: Union[GeoCoordinates, GeoShape]
    # Represents a relationship between two geometries (or the places they represent), relating a
    # containing geometry to a contained geometry.
    geoContains: Place
    # Represents a relationship between two geometries (or the places they represent), relating a
    # geometry to another that covers it.
    geoCoveredBy: Place
    # Represents a relationship between two geometries (or the places they represent), relating a
    # geometry to another that it covers.
    geoCovers: Place
    # Represents a relationship between two geometries (or the places they represent), relating a
    # geometry to another that crosses it.
    geoCrosses: Place
    # Represents spatial relations in which two geometries (or the places they represent) are
    # topologically disjoint.
    geoDisjoint: Place
    # Represents spatial relations in which two geometries (or the places they represent) are
    # topologically equal.
    geoEquals: Place
    # Represents spatial relations in which two geometries (or the places they represent) have at
    # least one point in common.
    geoIntersects: Place
    # Represents spatial relations in which two geometries (or the places they represent) overlap.
    geoOverlaps: Place
    # Represents spatial relations in which two geometries (or the places they represent) touch.
    geoTouches: Place
    # Represents spatial relations in which two geometries (or the places they represent) are within
    # each other.
    geoWithin: Place
    # The Global Location Number (GLN, sometimes also referred to as International Location Number or
    # ILN) of the respective organization, person, or place.
    globalLocationNumber: str
    # A URL to a map of the place.
    hasMap: Union[str, Map]
    # A flag to signal that the item, event, or place is accessible for free.
    isAccessibleForFree: bool
    # The International Standard of Industrial Classification of All Economic Activities (ISIC),
    # Revision 4 code for a particular organization, business person, or place.
    isicV4: str
    # An associated logo.
    logo: Union[str, ImageObject]
    # The total number of individuals that may attend an event or venue.
    maximumAttendeeCapacity: int
    # The opening hours of a certain place.
    openingHoursSpecification: Union[OpeningHoursSpecification,
                                     List[OpeningHoursSpecification]]
    # A photograph of this place.
    photo: Union[ImageObject, Photograph]
    # A flag to signal that the Place is open to public visitors.
    publicAccess: bool
    # A review of the item.
    review: Union[Review, List[Review]]
    # A slogan or motto associated with the item.
    slogan: str
    # Indicates whether it is allowed to smoke in the place, e.g. in the restaurant, hotel or hotel
    # room.
    smokingAllowed: bool
    # The special opening hours of a certain place.
    specialOpeningHoursSpecification: OpeningHoursSpecification
    # The telephone number.
    telephone: str
    # A page providing information on how to book a tour of some Place.
    tourBookingPage: str
