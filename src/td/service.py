from __future__ import annotations
from typing import Union, List
from .thing import Intangible, Thing
from .types import ItemList

OfferCatalog = ItemList


class Service(Intangible, total=False):
    """
    A class representing schema.org's Service.
    See: https://schema.org/Service
    """
    aggregateRating: AggregateRating
    areaServed: Union[str, Place, List[Union[str, Place]]]
    audience: Audience
    availableChannel: ServiceChannel
    award: Union[str, List[str]]
    brand: Union[Brand, List[Brand]]
    broker: Union[Organization, Person]
    category: Union[str, Thing, List[Union[str, Thing]]]
    hasOfferCatalog: OfferCatalog
    hoursAvailable: OpeningHoursSpecification
    isSimilarTo: Union[Product, Service]
    isRelatedTo: Union[Product, Service]
    logo: Union[str, ImageObject]
    offers: Offer
    provider: Union[Organization, Person]
    providerMobility: str
    review: Union[Review, List[Review]]
    serviceOutput: Thing
    serviceType: str
    slogan: str
    termsOfService: Union[str, CreativeWork]


class ServiceChannel(Intangible, total=False):
    """
    A class representing schema.org's ServiceChannel.
    See: https://schema.org/ServiceChannel
    """
    availableLanguage: Union[str, List[str]]
    processingTime: str
    providesService: Service
    serviceLocation: Union[Place, PostalAddress]
    servicePhone: Union[ContactPoint, List[ContactPoint]]
    servicePostalAddress: PostalAddress
    serviceSmsNumber: ContactPoint
    serviceUrl: str
    hoursAvailable: OpeningHoursSpecification
    contactOption: Union[str, List[str]]
    contactPoint: ContactPoint
    audience: Audience
    # Inherits all fields from Intangible/Thing


class BroadcastService(Service, total=False):
    """
    A class representing schema.org's BroadcastService.
    See: https://schema.org/BroadcastService
    """
    broadcastAffiliateOf: Organization
    broadcastDisplayName: str
    broadcastTimezone: str
    broadcaster: Organization
    hasBroadcastChannel: BroadcastChannel
    inLanguage: Union[str, List[str]]
    parentService: BroadcastService
    videoFormat: str


class BroadcastFrequencySpecification(Intangible, total=False):
    """
    A class representing schema.org's BroadcastFrequencySpecification.
    See: https://schema.org/BroadcastFrequencySpecification
    """
    broadcastFrequencyValue: Union[str, QuantitativeValue]
    broadcastFrequencyType: str


class BroadcastChannel(Intangible, total=False):
    """
    A class representing schema.org's BroadcastChannel.
    See: https://schema.org/BroadcastChannel
    """
    broadcastChannelId: str
    broadcastFrequency: Union[str, BroadcastFrequencySpecification]
    broadcastServiceTier: str
    genre: Union[str, List[str]]
    inBroadcastLineup: str
    providesBroadcastService: BroadcastService
