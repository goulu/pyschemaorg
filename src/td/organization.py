from __future__ import annotations
from typing import Union, List
from .thing import Thing


class Organization(Thing, total=False):
    """
    A class representing schema.org's Organization.
    See: https://schema.org/Organization
    """
    address: Union[str, 'PostalAddress', 'Place',
                   List[Union[str, 'PostalAddress', 'Place']]]
    aggregateRating: 'AggregateRating'
    alumni: Union['Person', List['Person']]
    areaServed: Union[str, 'Place', List[Union[str, 'Place']]]
    award: Union[str, List[str]]
    brand: Union['Brand', List['Brand']]
    contactPoint: Union['ContactPoint', List['ContactPoint']]
    department: 'Organization'
    dissolutionDate: str
    duns: str
    email: str
    employee: Union['Person', List['Person']]
    event: Union['Event', List['Event']]
    faxNumber: str
    founder: Union['Person', List['Person']]
    foundingDate: str
    foundingLocation: 'Place'
    funder: Union['Person', 'Organization',
                  List[Union['Person', 'Organization']]]
    globalLocationNumber: str
    hasOfferCatalog: 'Offer'
    hasPOS: 'Place'
    isicV4: str
    legalName: str
    leiCode: str
    location: Union[str, 'Place', List[Union[str, 'Place']]]
    logo: Union[str, 'ImageObject']
    makesOffer: Union['Offer', List['Offer']]
    member: Union['Person', 'Organization',
                  List[Union['Person', 'Organization']]]
    memberOf: Union['Organization', List['Organization']]
    naics: str
    numberOfEmployees: 'QuantitativeValue'
    owns: Union['Product', 'OwnershipInfo',
                List[Union['Product', 'OwnershipInfo']]]
    parentOrganization: 'Organization'
    review: Union['Review', List['Review']]
    seeks: 'Demand'
    sponsor: Union['Person', 'Organization',
                   List[Union['Person', 'Organization']]]
    subOrganization: 'Organization'
    taxID: str
    telephone: str
    vatID: str


class PerformingGroup(Organization, total=False):
    """
    A class representing schema.org's PerformingGroup.
    See: https://schema.org/PerformingGroup
    """
    pass
