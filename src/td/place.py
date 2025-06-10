from __future__ import annotations
from datetime import date, datetime
from typing import Optional, Union, List
from .thing import Intangible, Text
from .values import StructuredValue, PropertyValue


class VirtualLocation(Intangible, total=False):
    """
    A class representing schema.org's Intangible.
    See: https://schema.org/VirtualLocation
    """
    pass


class Language(Intangible, total=False):
    """
    A class representing schema.org's Intangible.
    See: https://schema.org/Language
    """
    pass


class ContactPoint(StructuredValue, total=False):
    """
    A class representing schema.org's ContactPoint.
    See: https://schema.org/ContactPoint
    """
    # The geographic area where a service or offered item is provided.
    areaServed: Optional[Union[Place,
                               GeoShape, AdministrativeArea, Text]]

    # A language someone may use with or at the item.
    availableLanguage: Optional[Union[Text, Language,]]
    # An option available on this contact point (e.g. toll-free number, hearing-impaired support).
    contactOption: Optional[Union[str, List[str]]]
    # A person or organization can have different contact points, for different purposes.
    contactType: Optional[str]
    email: Optional[str]  # Email address for correspondence.
    faxNumber: Optional[str]  # The fax number.
    # The hours during which this contact point is available.
    hoursAvailable: Optional[OpeningHoursSpecification]
    # The product or service supported by this contact point.
    productSupported: Optional[Union[str, Product]]
    telephone: Optional[str]  # The telephone number.


# PostalAddress: https://.org/PostalAddress
class PostalAddress(ContactPoint, total=False):
    """
    A class representing schema.org's PostalAddress.
    See: https://schema.org/PostalAddress
    """
    addressCountry: Optional[Union[str, Country]
                             # The country. For example, USA. You can also provide the two-letter ISO 3166-1 alpha-2 country code.
                             ]
    addressLocality: Optional[str]  # The locality. For example, Mountain View.
    addressRegion: Optional[str]  # The region. For example, CA.
    # The extended address. For example, Suite 100.
    extendedAddress: Optional[str]
    # The post office box number for PO box addresses.
    postOfficeBoxNumber: Optional[str]
    postalCode: Optional[str]  # The postal code. For example, 94043.
    # The street address. For example, 1600 Amphitheatre Pkwy.
    streetAddress: Optional[str]


class GeoCoordinates(StructuredValue, total=False):
    """
    A class representing schema.org's GeoCoordinates.
    The geographic coordinates of a place or event.
    See: https://schema.org/GeoCoordinates
    """
    address: Optional[Union[str, PostalAddress]
                      ]  # Physical address of the item.
    # The country. For example, USA. You can also provide the two-letter ISO 3166-1 alpha-2 country code.
    addressCountry: Optional[Union[str, Country]]
    # The elevation of a location (WGS 84). Values may be positive or negative, representing height above or below sea level.
    elevation: Optional[Union[float, str]]
    # The latitude of a location. For example 37.42242 (WGS 84).
    latitude: Optional[Union[float, str]]
    # The longitude of a location. For example -122.08585 (WGS 84).
    longitude: Optional[Union[float, str]]
    postalCode: Optional[str]  # The postal code. For example, 94043.


class LocationFeatureSpecification(PropertyValue, total=False):
    """
    A class representing schema.org's LocationFeatureSpecification.
    Specifies a location feature by providing a structured value representing a feature of an accommodation as a property-value pair.
    See: https://schema.org/LocationFeatureSpecification
    """
    # The hours during which this service or contact is available.
    hoursAvailable: Optional[OpeningHoursSpecification]
    # The date when the item becomes valid.
    validFrom: Optional[Union[date, datetime]]
    # The date after when the item is not valid.
    validThrough: Optional[Union[date, datetime]]


# Place: https://.org/Place
class Place(StructuredValue, total=False):
    """
    A class representing schema.org's Place.
    See: https://schema.org/Place
    """
    address: Optional[Union[str, PostalAddress]
                      ]  # Physical address of the item.
    # The overall rating, based on a collection of reviews or ratings, of the item.
    aggregateRating: Optional[AggregateRating]
    # An amenity feature (e.g. a characteristic or service) of the Accommodation.
    amenityFeature: Optional[LocationFeatureSpecification]
    # A short textual code (also called "store code") that uniquely identifies a place of business.
    branchCode: Optional[str]
    # The basic containment relation between places.
    containedIn: Optional[Place]
    # The basic containment relation between places.
    containedInPlace: Optional[Place]
    # The basic containment relation between places.
    containsPlace: Optional[Union[Place, List[Place]]]
    # Upcoming or past event associated with this place, organization, or action.
    event: Optional[Event]
    faxNumber: Optional[str]  # The fax number.
    # The geo coordinates of the place.
    geo: Optional[Union[GeoCoordinates, GeoShape]]
    # Represents a relationship between two geometries (or the places they represent), relating a containing geometry to a contained geometry.
    geoContains: Optional[Place]
    # Represents a relationship between two geometries (or the places they represent), relating a geometry to another that covers it.
    geoCoveredBy: Optional[Place]
    # Represents a relationship between two geometries (or the places they represent), relating a geometry to another that it covers.
    geoCovers: Optional[Place]
    # Represents a relationship between two geometries (or the places they represent), relating a geometry to another that crosses it.
    geoCrosses: Optional[Place]
    # Represents spatial relations in which two geometries (or the places they represent) are topologically disjoint.
    geoDisjoint: Optional[Place]
    # Represents spatial relations in which two geometries (or the places they represent) are topologically equal.
    geoEquals: Optional[Place]
    # Represents spatial relations in which two geometries (or the places they represent) have at least one point in common.
    geoIntersects: Optional[Place]
    # Represents spatial relations in which two geometries (or the places they represent) overlap.
    geoOverlaps: Optional[Place]
    # Represents spatial relations in which two geometries (or the places they represent) touch.
    geoTouches: Optional[Place]
    # Represents spatial relations in which two geometries (or the places they represent) are within each other.
    geoWithin: Optional[Place]
    # The Global Location Number (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place.
    globalLocationNumber: Optional[str]
    hasMap: Optional[Union[str, Map]]  # A URL to a map of the place.
    # A flag to signal that the item, event, or place is accessible for free.
    isAccessibleForFree: Optional[bool]
    # The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.
    isicV4: Optional[str]
    logo: Optional[Union[str, ImageObject]]  # An associated logo.
    # The total number of individuals that may attend an event or venue.
    maximumAttendeeCapacity: Optional[int]
    # The opening hours of a certain place.
    openingHoursSpecification: Optional[Union[OpeningHoursSpecification,
                                              List[OpeningHoursSpecification]]]
    # A photograph of this place.
    photo: Optional[Union[ImageObject, Photograph]]
    # A flag to signal that the Place is open to public visitors.
    publicAccess: Optional[bool]
    review: Optional[Union[Review, List[Review]]]  # A review of the item.
    slogan: Optional[str]  # A slogan or motto associated with the item.
    # Indicates whether it is allowed to smoke in the place, e.g. in the restaurant, hotel or hotel room.
    smokingAllowed: Optional[bool]
    # The special opening hours of a certain place.
    specialOpeningHoursSpecification: Optional[OpeningHoursSpecification]
    telephone: Optional[str]  # The telephone number.
    # A page providing information on how to book a tour of some Place.
    tourBookingPage: Optional[str]


# AdministrativeArea: https://.org/AdministrativeArea
class AdministrativeArea(Place, total=False):
    """
    A class representing schema.org's AdministrativeArea.
    See: https://schema.org/AdministrativeArea
    """
    pass  # An administrative area is a type of Place.


# Country: https://.org/Country
class Country(AdministrativeArea, total=False):
    """
    A class representing schema.org's Country.
    See: https://schema.org/Country
    """
    pass  # A country is a type of AdministrativeArea.


# Audience: https://.org/Audience
class Audience(StructuredValue, total=False):
    """
    A class representing schema.org's Audience.
    See: https://schema.org/Audience
    """
    audienceType: Optional[
        # The target group associated with a given audience (e.g. veterans, car owners, musicians, etc.).
        str]
    # The geographic area associated with the audience.
    geographicArea: Optional[AdministrativeArea]


# GeoShape: https://.org/GeoShape
class GeoShape(StructuredValue, total=False):
    """
    A class representing schema.org's GeoShape.
    See: https://schema.org/GeoShape
    """
    address: Optional[Union[str, PostalAddress]
                      ]  # Physical address of the item.
    # The country. For example, USA. You can also provide the two-letter ISO 3166-1 alpha-2 country code.
    addressCountry: Optional[Union[str, Country]]
    # A box is the area enclosed by the rectangle formed by two points.
    box: Optional[str]
    # A circle is the area enclosed by a circle defined by a center point and a radius.
    circle: Optional[str]
    elevation: Optional[Union[str, float]]  # The elevation of a location.
    # A line is a point-to-point path consisting of two or more points.
    line: Optional[str]
    # A polygon is the area enclosed by a point-to-point path for which the starting and ending points are the same.
    polygon: Optional[str]
    postalCode: Optional[str]  # The postal code.
