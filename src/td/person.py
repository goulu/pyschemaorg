from __future__ import annotations
from typing import Union, List, TYPE_CHECKING

from .thing import Thing
from .data_type import Text, Date
if TYPE_CHECKING:
    from .postal_address import PostalAddress
    from .place import Place
    from .organization import Organization
    from .contact_point import ContactPoint
    from .quantitative_value import QuantitativeValue
    from .interaction_counter import InteractionCounter
    from .offer import Offer
    from .product import Product
    from .ownership_info import OwnershipInfo
    from .event import Event
    from .creative_work import CreativeWork
    from .demand import Demand
    from .brand import Brand


class Person(Thing, total=False):
    """
    A class representing schema.org's Person.
    See: https://schema.org/Person
    """
    additionalName: Text  # An additional name for a Person, can be used for a middle name.
    # Physical address of the item.
    address: Union[Text, PostalAddress, Place]
    # An organization that this person is affiliated with.
    affiliation: Organization
    # An organization that the person is an alumni of.
    alumniOf: Organization
    award: Text  # An award won by or for this item.
    birthDate: Date  # Date of birth.
    birthPlace: Place  # The place where the person was born.
    # The brand(s) associated with a person.
    brand: Union[Brand, Organization]
    children: Union[Person, List[Person]]  # A child of the person.
    # A colleague of the person.
    colleague: Union[Person, Organization, List[Union[Person, Organization]]]
    # A contact point for a person or organization.
    contactPoint: Union[ContactPoint, List[ContactPoint]]
    deathDate: str  # Date of death.
    deathPlace: Place  # The place where the person died.
    # The Dun & Bradstreet DUNS number for identifying an organization or business person.
    duns: str
    email: str  # Email address.
    familyName: str  # Family name. In the U.S., the last name of a person.
    faxNumber: str  # The fax number.
    # The most generic uni-directional social relation.
    follows: Union[Person, List[Person]]
    # A person or organization that supports (sponsors) something through some kind of financial contribution.
    funder: Union[Organization, List[Organization]]
    gender: str  # Gender of the person.
    givenName: str  # Given name. In the U.S., the first name of a person.
    # The Global Location Number (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place.
    globalLocationNumber: str
    hasOccupation: str  # The Person's occupation.
    # Indicates an OfferCatalog listing for this Organization, Person, or Service.
    hasOfferCatalog: str
    hasPOS: Place  # Points-of-Sale operated by the organization or person.
    height: Union[str, QuantitativeValue]  # The height of the item.
    homeLocation: Place  # A contact location for a person's residence.
    # An honorific prefix preceding a Person's name such as Dr/Mrs/Mr.
    honorificPrefix: str
    # An honorific suffix following a Person's name such as M.D./PhD.
    honorificSuffix: str
    # The number of interactions for the CreativeWork using the WebSite or SoftwareApplication.
    interactionStatistic: InteractionCounter
    # The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization or business person.
    isicV4: str
    # The job title of the person (for example, Financial Manager).
    jobTitle: str
    # The most generic bi-directional social/work relation.
    knows: Union[Person, List[Person]]
    # Of a Person, and less typically of an Organization, to indicate a topic that is known about.
    knowsAbout: Union[str, List[str]]
    # Of a Person, and less typically of an Organization, to indicate a language known.
    knowsLanguage: Union[str, List[str]]
    # A pointer to products or services offered by the organization or person.
    makesOffer: Offer
    # An organization (or program membership) to which this person belongs.
    memberOf: Union[Organization, List[Organization]]
    # The North American Industry Classification System (NAICS) code for a particular organization or business person.
    naics: str
    nationality: str  # Nationality of the person.
    # The total financial value of the person as calculated by subtracting assets from liabilities.
    netWorth: Union[str, QuantitativeValue]
    # Products owned by the person or organization.
    owns: Union[Product, OwnershipInfo, List[Union[Product, OwnershipInfo]]]
    parent: Union[Person, List[Person]]  # A parent of this person.
    # Event that this person is a performer or participant in.
    performerIn: Union[Event, List[Event]]
    # The publishing principles applied to the CreativeWork.
    publishingPrinciples: Union[str, CreativeWork]
    # The most generic familial relation.
    relatedTo: Union[Person, List[Person]]
    # A pointer to products or services sought by the organization or person (demand).
    seeks: Demand
    sibling: Union[Person, List[Person]]  # A sibling of the person.
    # A person or organization that supports a thing through a pledge, promise, or financial contribution.
    sponsor: Union[Organization, List[Organization]]
    spouse: Person  # The person's spouse.
    taxID: str  # The Tax / Fiscal ID of the organization or person.
    telephone: str  # The telephone number.
    vatID: str  # The Value-added Tax ID of the organization or person.
    weight: Union[str, QuantitativeValue]  # The weight of the item.
    workLocation: Place  # A contact location for a person's place of work.
    # Organizations that the person works for.
    worksFor: Union[Organization, List[Organization]]
