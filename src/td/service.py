from __future__ import annotations
from typing import Optional, Union, List
from .thing import Intangible, Thing
from .types import ItemList

OfferCatalog = ItemList


class Service(Intangible, total=False):
    """
    A class representing schema.org's Service.
    See: https://schema.org/Service
    """
    aggregateRating: Optional[AggregateRating]
    areaServed: Optional[Union[str, Place, List[Union[str, Place]]]]
    audience: Optional[Audience]
    availableChannel: Optional[ServiceChannel]
    award: Optional[Union[str, List[str]]]
    brand: Optional[Union[Brand, List[Brand]]]
    broker: Optional[Union[Organization, Person]]
    category: Optional[Union[str, Thing, List[Union[str, Thing]]]]
    hasOfferCatalog: Optional[OfferCatalog]
    hoursAvailable: Optional[OpeningHoursSpecification]
    isSimilarTo: Optional[Union[Product, Service]]
    isRelatedTo: Optional[Union[Product, Service]]
    logo: Optional[Union[str, ImageObject]]
    offers: Optional[Offer]
    provider: Optional[Union[Organization, Person]]
    providerMobility: Optional[str]
    review: Optional[Union[Review, List[Review]]]
    serviceOutput: Optional[Thing]
    serviceType: Optional[str]
    slogan: Optional[str]
    termsOfService: Optional[Union[str, CreativeWork]]


class ServiceChannel(Intangible, total=False):
    """
    A class representing schema.org's ServiceChannel.
    See: https://schema.org/ServiceChannel
    """
    availableLanguage: Optional[Union[str, List[str]]]
    processingTime: Optional[str]
    providesService: Optional[Service]
    serviceLocation: Optional[Union[Place, PostalAddress]]
    servicePhone: Optional[Union[ContactPoint, List[ContactPoint]]]
    servicePostalAddress: Optional[PostalAddress]
    serviceSmsNumber: Optional[ContactPoint]
    serviceUrl: Optional[str]
    hoursAvailable: Optional[OpeningHoursSpecification]
    contactOption: Optional[Union[str, List[str]]]
    contactPoint: Optional[ContactPoint]
    audience: Optional[Audience]
    # Inherits all fields from Intangible/Thing


class BroadcastService(Service, total=False):
    """
    A class representing schema.org's BroadcastService.
    See: https://schema.org/BroadcastService
    """
    broadcastAffiliateOf: Optional[Organization]
    broadcastDisplayName: Optional[str]
    broadcastTimezone: Optional[str]
    broadcaster: Optional[Organization]
    hasBroadcastChannel: Optional[BroadcastChannel]
    inLanguage: Optional[Union[str, List[str]]]
    parentService: Optional[BroadcastService]
    videoFormat: Optional[str]


class BroadcastFrequencySpecification(Intangible, total=False):
    """
    A class representing schema.org's BroadcastFrequencySpecification.
    See: https://schema.org/BroadcastFrequencySpecification
    """
    broadcastFrequencyValue: Optional[Union[str, QuantitativeValue]]
    broadcastFrequencyType: Optional[str]


class BroadcastChannel(Intangible, total=False):
    """
    A class representing schema.org's BroadcastChannel.
    See: https://schema.org/BroadcastChannel
    """
    broadcastChannelId: Optional[str]
    broadcastFrequency: Optional[Union[str, BroadcastFrequencySpecification]]
    broadcastServiceTier: Optional[str]
    genre: Optional[Union[str, List[str]]]
    inBroadcastLineup: Optional[str]
    providesBroadcastService: Optional[BroadcastService]
