from __future__ import annotations
from datetime import date, datetime
from typing import Union, List
from .thing import Intangible, Text
from .values import StructuredValue, PropertyValue


class VirtualLocation(Intangible, total=False):
    """
    A class representing schema.org's VirtualLocation.
    See: https://schema.org/VirtualLocation
    """
    pass


class Language(Intangible, total=False):
    """
    A class representing schema.org's Language.
    See: https://schema.org/Language
    """
    pass


class ContactPoint(StructuredValue, total=False):
    """
    A class representing schema.org's ContactPoint.
    See: https://schema.org/ContactPoint
    """
    # The geographic area where a service or offered item is provided.
    areaServed: Union['Place', 'GeoShape', 'AdministrativeArea', Text]

    # A language someone may use with or at the item.
    availableLanguage: Union[Text, 'Language',]
    # An option available on this contact point (e.g. toll-free number, hearing-impaired support).
    contactOption: Union[str, List[str]]
    # A person or organization can have different contact points, for different purposes.
    contactType: str
    email: str  # Email address for correspondence.
    faxNumber: str  # The fax number.
    # The hours during which this contact point is available.
    hoursAvailable: 'OpeningHoursSpecification'
    # The product or service supported by this contact point.
    productSupported: Union[str, 'Product']
    telephone: str  # The telephone number.


class PostalAddress(ContactPoint, total=False):
    """
    A class representing schema.org's PostalAddress.
    See: https://schema.org/PostalAddress
    """
    # The country. For example, USA. You can also provide the two-letter ISO 3166-1 alpha-2 country code.
    addressCountry: Union[str, 'Country']
    addressLocality: str  # The locality. For example, Mountain View.
    addressRegion: str  # The region. For example, CA.
    # The extended address. For example, Suite 100.
    extendedAddress: str
    # The post office box number for PO box addresses.
    postOfficeBoxNumber: str
    postalCode: str  # The postal code. For example, 94043.
    # The street address. For example, 1600 Amphitheatre Pkwy.
    streetAddress: str


class GeoCoordinates(StructuredValue, total=False):
    """
    A class representing schema.org's GeoCoordinates.
    The geographic coordinates of a place or event.
    See: https://schema.org/GeoCoordinates
    """
    address: Union[str, 'PostalAddress']  # Physical address of the item.
    # The country. For example, USA. You can also provide the two-letter ISO 3166-1 alpha-2 country code.
    addressCountry: Union[str, 'Country']
    # The elevation of a location (WGS 84). Values may be positive or negative, representing height above or below sea level.
    elevation: Union[float, str]
    # The latitude of a location. For example 37.42242 (WGS 84).
    latitude: Union[float, str]
    # The longitude of a location. For example -122.08585 (WGS 84).
    longitude: Union[float, str]
    postalCode: str  # The postal code. For example, 94043.


class LocationFeatureSpecification(PropertyValue, total=False):
    """
    A class representing schema.org's LocationFeatureSpecification.
    Specifies a location feature by providing a structured value representing a feature of an accommodation as a property-value pair.
    See: https://schema.org/LocationFeatureSpecification
    """
    # The hours during which this service or contact is available.
    hoursAvailable: 'OpeningHoursSpecification'
    # The date when the item becomes valid.
    validFrom: Union[date, datetime]
    # The date after when the item is not valid.
    validThrough: Union[date, datetime]


# Place: https://.org/Place
class Place(StructuredValue, total=False):
    """
    A class representing schema.org's Place.
    See: https://schema.org/Place
    """
    address: Union[str, 'PostalAddress']  # Physical address of the item.
    # The overall rating, based on a collection of reviews or ratings, of the item.
    aggregateRating: 'AggregateRating'
    # An amenity feature (e.g. a characteristic or service) of the Accommodation.
    amenityFeature: 'LocationFeatureSpecification'
    # A short textual code (also called "store code") that uniquely identifies a place of business.
    branchCode: str
    # The basic containment relation between places.
    containedIn: 'Place'
    # The basic containment relation between places.
    containedInPlace: 'Place'
    # The basic containment relation between places.
    containsPlace: Union['Place', List['Place']]
    # Upcoming or past event associated with this place, organization, or action.
    event: 'Event'
    faxNumber: str  # The fax number.
    # The geo coordinates of the place.
    geo: Union['GeoCoordinates', 'GeoShape']
    # Represents a relationship between two geometries (or the places they represent), relating a containing geometry to a contained geometry.
    geoContains: 'Place'
    # Represents a relationship between two geometries (or the places they represent), relating a geometry to another that covers it.
    geoCoveredBy: 'Place'
    # Represents a relationship between two geometries (or the places they represent), relating a geometry to another that it covers.
    geoCovers: 'Place'
    # Represents a relationship between two geometries (or the places they represent), relating a geometry to another that crosses it.
    geoCrosses: 'Place'
    # Represents spatial relations in which two geometries (or the places they represent) are topologically disjoint.
    geoDisjoint: 'Place'
    # Represents spatial relations in which two geometries (or the places they represent) are topologically equal.
    geoEquals: 'Place'
    # Represents spatial relations in which two geometries (or the places they represent) have at least one point in common.
    geoIntersects: 'Place'
    # Represents spatial relations in which two geometries (or the places they represent) overlap.
    geoOverlaps: 'Place'
    # Represents spatial relations in which two geometries (or the places they represent) touch.
    geoTouches: 'Place'
    # Represents spatial relations in which two geometries (or the places they represent) are within each other.
    geoWithin: 'Place'
    # The Global Location Number (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place.
    globalLocationNumber: str
    hasMap: Union[str, 'Map']  # A URL to a map of the place.
    # A flag to signal that the item, event, or place is accessible for free.
    isAccessibleForFree: bool
    # The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.
    isicV4: str
    logo: Union[str, 'ImageObject']  # An associated logo.
    # The total number of individuals that may attend an event or venue.
    maximumAttendeeCapacity: int
    # The opening hours of a certain place.
    openingHoursSpecification: Union['OpeningHoursSpecification',
                                     List['OpeningHoursSpecification']]
    # A photograph of this place.
    photo: Union['ImageObject', 'Photograph']
    # A flag to signal that the Place is open to public visitors.
    publicAccess: bool
    review: Union['Review', List['Review']]  # A review of the item.
    slogan: str  # A slogan or motto associated with the item.
    # Indicates whether it is allowed to smoke in the place, e.g. in the restaurant, hotel or hotel room.
    smokingAllowed: bool
    # The special opening hours of a certain place.
    specialOpeningHoursSpecification: 'OpeningHoursSpecification'
    telephone: str  # The telephone number.
    # A page providing information on how to book a tour of some Place.
    tourBookingPage: str


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
    audienceType: str
    # The geographic area associated with the audience.
    geographicArea: 'AdministrativeArea'
