from __future__ import annotations
from typing import TypedDict, Union, List, TYPE_CHECKING
from .thing import Thing

if TYPE_CHECKING:
    from .aggregate_rating import AggregateRating
    from .brand import Brand
    from .contact_point import ContactPoint
    from .country import Country
    from .demand import Demand
    from .offer import Offer
    from .person import Person
    from .place import Place
    from .postal_address import PostalAddress
    from .product import Product
    from .review import Review
    from .service import Service


# Organization: https://schema.org/Organization
class Organization(Thing, TypedDict, total=False):
    """
    A class representing schema.org's Organization.
    See: https://schema.org/Organization
    """
    # The overall rating, based on a collection of reviews or ratings, of the item.
    aggregateRating: AggregateRating
    # An organization identifier that uniquely identifies a legal entity as defined in ISO 17442.
    leiCode: str
    # The brand(s) associated with a product or service, or the brand(s) maintained by an organization
    # or business person.
    brand: Union[Brand, List[Brand]]
    # A contact point for a person or organization.
    contactPoint: Union[ContactPoint, List[ContactPoint]]
    # The country. For example, the country where the person is located or a product is available.
    country: Country
    # The date that this organization was dissolved.
    dissolutionDate: str
    # The Dun & Bradstreet DUNS number for identifying an organization or business person.
    duns: str
    # Email address.
    email: str
    # Someone working for this organization.
    employee: Union[Person, List[Person]]
    # Upcoming or past event associated with this place, organization, or action.
    event: Union[Thing, List[Thing]]
    # The fax number.
    faxNumber: str
    # A person who founded this organization.
    founder: Union[Person, List[Person]]
    # The date that this organization was founded.
    foundingDate: str
    # The place where the organization was founded.
    foundingLocation: Place
    # The Global Location Number (GLN, sometimes also referred to as International Location Number or
    # ILN) of the respective organization, person, or place.
    globalLocationNumber: str
    # The International Standard of Industrial Classification of All Economic Activities (ISIC),
    # Revision 4 code for a particular organization, business person, or place.
    isicV4: str
    # The official name of the organization, e.g. the registered company name.
    legalName: str
    # The location of the organization.
    location: Union[Place, PostalAddress, str]
    # An associated logo.
    logo: Union[str, Thing]
    # The number of employees in an organization.
    numberOfEmployees: int
    # The offer catalog provided by this organization.
    makesOffer: Union[Offer, List[Offer]]
    # The parent organization of an organization.
    parentOrganization: 'Organization'
    # The products produced by the organization.
    produces: Union[Product, List[Product]]
    # A review of the item.
    review: Union[Review, List[Review]]
    # A pointer to products or services offered by the organization or person.
    seeks: Union[Demand, List[Demand]]
    # A slogan or motto associated with the item.
    slogan: str
    # The Tax / Fiscal ID of the organization or person.
    taxID: str
    # The telephone number.
    telephone: str
    # The Value-added Tax ID of the organization or person.
    vatID: str
    # The year the organization was founded.
    foundingYear: int
    # The services provided by the organization.
    service: Union[Service, List[Service]]
