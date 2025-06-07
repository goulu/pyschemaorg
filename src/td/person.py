from typing import Optional, Union, List

from .business import Demand, Offer, OwnershipInfo, Product
from .values import QuantitativeValue
from .thing import Thing
from .place import Place, PostalAddress, ContactPoint
from .organization import Organization
from .creative_work import CreativeWork, InteractionCounter
from .event import Event


class Person(Thing, total=False):
    """
    A class representing .org's Person.
    See: https://.org/Person
    """
    additionalName: Optional[Union[str, List[str]]]
    address: Optional[Union[str, PostalAddress, Place,
                            List[Union[str, PostalAddress, Place]]]]
    affiliation: Optional[Union[Organization, List[Organization]]]
    alumniOf: Optional[Union[Organization, List[Organization]]]
    award: Optional[Union[str, List[str]]]
    birthDate: Optional[str]
    birthPlace: Optional[Place]
    brand: Optional[Union[Organization, List[Organization]]]
    children: Optional[Union['Person', List['Person']]]
    colleague: Optional[Union['Person', Organization,
                              List[Union['Person', Organization]]]]
    contactPoint: Optional[Union[ContactPoint, List[ContactPoint]]]
    deathDate: Optional[str]
    deathPlace: Optional[Place]
    duns: Optional[str]
    email: Optional[str]
    familyName: Optional[str]
    faxNumber: Optional[str]
    follows: Optional[Union['Person', List['Person']]]
    funder: Optional[Union[Organization, List[Organization]]]
    gender: Optional[str]
    givenName: Optional[str]
    globalLocationNumber: Optional[str]
    hasOccupation: Optional[str]
    hasOfferCatalog: Optional[str]
    hasPOS: Optional[Place]
    height: Optional[Union[str, 'QuantitativeValue']]
    homeLocation: Optional[Place]
    honorificPrefix: Optional[str]
    honorificSuffix: Optional[str]
    interactionStatistic: Optional['InteractionCounter']
    isicV4: Optional[str]
    jobTitle: Optional[str]
    knows: Optional[Union['Person', List['Person']]]
    knowsAbout: Optional[Union[str, List[str]]]
    knowsLanguage: Optional[Union[str, List[str]]]
    makesOffer: Optional['Offer']
    memberOf: Optional[Union[Organization, List[Organization]]]
    naics: Optional[str]
    nationality: Optional[str]
    netWorth: Optional[Union[str, 'QuantitativeValue']]
    owns: Optional[Union['Product', 'OwnershipInfo',
                         List[Union['Product', 'OwnershipInfo']]]]
    parent: Optional[Union['Person', List['Person']]]
    performerIn: Optional[Union[Event, List[Event]]]
    publishingPrinciples: Optional[Union[str, CreativeWork]]
    relatedTo: Optional[Union['Person', List['Person']]]
    seeks: Optional['Demand']
    sibling: Optional[Union['Person', List['Person']]]
    sponsor: Optional[Union[Organization, List[Organization]]]
    spouse: Optional['Person']
    taxID: Optional[str]
    telephone: Optional[str]
    vatID: Optional[str]
    weight: Optional[Union[str, 'QuantitativeValue']]
    workLocation: Optional[Place]
    worksFor: Optional[Union[Organization, List[Organization]]]
