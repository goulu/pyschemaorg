from __future__ import annotations
from typing import Union, List
from .thing import Thing


class Person(Thing, total=False):
    """
    A class representing schema.org's Person.
    See: https://schema.org/Person
    """
    additionalName: Union[str, List[str]]
    address: Union[str, 'PostalAddress', 'Place',
                   List[Union[str, 'PostalAddress', 'Place']]]
    affiliation: Union['Organization', List['Organization']]
    alumniOf: Union['Organization', List['Organization']]
    award: Union[str, List[str]]
    birthDate: str
    birthPlace: 'Place'
    brand: Union['Organization', List['Organization']]
    children: Union['Person', List['Person']]
    colleague: Union['Person', 'Organization',
                     List[Union['Person', 'Organization']]]
    contactPoint: Union['ContactPoint', List['ContactPoint']]
    deathDate: str
    deathPlace: 'Place'
    duns: str
    email: str
    familyName: str
    faxNumber: str
    follows: Union['Person', List['Person']]
    funder: Union['Organization', List['Organization']]
    gender: str
    givenName: str
    globalLocationNumber: str
    hasOccupation: str
    hasOfferCatalog: str
    hasPOS: 'Place'
    height: Union[str, 'QuantitativeValue']
    homeLocation: 'Place'
    honorificPrefix: str
    honorificSuffix: str
    interactionStatistic: 'InteractionCounter'
    isicV4: str
    jobTitle: str
    knows: Union['Person', List['Person']]
    knowsAbout: Union[str, List[str]]
    knowsLanguage: Union[str, List[str]]
    makesOffer: 'Offer'
    memberOf: Union['Organization', List['Organization']]
    naics: str
    nationality: str
    netWorth: Union[str, 'QuantitativeValue']
    owns: Union['Product', 'OwnershipInfo',
                List[Union['Product', 'OwnershipInfo']]]
    parent: Union['Person', List['Person']]
    performerIn: Union['Event', List['Event']]
    publishingPrinciples: Union[str, 'CreativeWork']
    relatedTo: Union['Person', List['Person']]
    seeks: 'Demand'
    sibling: Union['Person', List['Person']]
    sponsor: Union['Organization', List['Organization']]
    spouse: 'Person'
    taxID: str
    telephone: str
    vatID: str
    weight: Union[str, 'QuantitativeValue']
    workLocation: 'Place'
    worksFor: Union['Organization', List['Organization']]
