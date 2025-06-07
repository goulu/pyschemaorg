from typing import Optional, List, Union

from .creative_work import Review
from .media_object import ImageObject
from .values import QuantitativeValue

from .thing import Thing
from .person import Person
from .place import Place, PostalAddress, ContactPoint
from .rating import AggregateRating
from .event import Event
from .business import Offer, Demand, Brand, OwnershipInfo, Product


class Organization(Thing, total=False):
    """
    A class representing .org's Organization.
    See: https://.org/Organization
    """
    address: Optional[Union[str, PostalAddress, Place,
                            List[Union[str, PostalAddress, Place]]]]
    aggregateRating: Optional['AggregateRating']
    alumni: Optional[Union['Person', List['Person']]]
    areaServed: Optional[Union[str, Place, List[Union[str, Place]]]]
    award: Optional[Union[str, List[str]]]
    brand: Optional[Union['Brand', List['Brand']]]
    contactPoint: Optional[Union[ContactPoint, List[ContactPoint]]]
    department: Optional['Organization']
    dissolutionDate: Optional[str]
    duns: Optional[str]
    email: Optional[str]
    employee: Optional[Union['Person', List['Person']]]
    event: Optional[Union['Event', List['Event']]]
    faxNumber: Optional[str]
    founder: Optional[Union['Person', List['Person']]]
    foundingDate: Optional[str]
    foundingLocation: Optional[Place]
    funder: Optional[Union['Person', 'Organization',
                           List[Union['Person', 'Organization']]]]
    globalLocationNumber: Optional[str]
    hasOfferCatalog: Optional['Offer']
    hasPOS: Optional[Place]
    isicV4: Optional[str]
    legalName: Optional[str]
    leiCode: Optional[str]
    location: Optional[Union[str, Place, List[Union[str, Place]]]]
    logo: Optional[Union[str, 'ImageObject']]
    makesOffer: Optional[Union['Offer', List['Offer']]]
    member: Optional[Union['Person', 'Organization',
                           List[Union['Person', 'Organization']]]]
    memberOf: Optional[Union['Organization', List['Organization']]]
    naics: Optional[str]
    numberOfEmployees: Optional['QuantitativeValue']
    owns: Optional[Union[Product, 'OwnershipInfo',
                         List[Union[Product, 'OwnershipInfo']]]]
    parentOrganization: Optional['Organization']
    review: Optional[Union['Review', List['Review']]]
    seeks: Optional['Demand']
    sponsor: Optional[Union['Person', 'Organization',
                            List[Union['Person', 'Organization']]]]
    subOrganization: Optional['Organization']
    taxID: Optional[str]
    telephone: Optional[str]
    vatID: Optional[str]
    # Inherits all fields from Thing


class PerformingGroup(Organization, total=False):
    """
    A class representing .org's PerformingGroup.
    See: https://.org/PerformingGroup
    """
    pass
