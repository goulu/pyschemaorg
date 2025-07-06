from __future__ import annotations
from typing import Union, List, TYPE_CHECKING
from .thing import Intangible, Thing

if TYPE_CHECKING:
    from .service_channel import ServiceChannel
    from .opening_hours_specification import OpeningHoursSpecification
    from .offer import Offer
    from .review import Review
    from .creative_work import CreativeWork
    from .aggregate_rating import AggregateRating
    from .place import Place
    from .audience import Audience
    from .brand import Brand
    from .organization import Organization
    from .person import Person
    from .product import Product
    from .image_object import ImageObject


class Service(Intangible, total=False):
    """
    A class representing schema.org's Service.
    See: https://schema.org/Service
    """
    aggregateRating: 'AggregateRating'
    areaServed: Union[str, 'Place', List[Union[str, 'Place']]]
    audience: 'Audience'
    availableChannel: 'ServiceChannel'
    award: Union[str, List[str]]
    brand: Union['Brand', List['Brand']]
    broker: Union['Organization', 'Person']
    category: Union[str, Thing, List[Union[str, Thing]]]
    hoursAvailable: 'OpeningHoursSpecification'
    isSimilarTo: Union['Product', 'Service']
    isRelatedTo: Union['Product', 'Service']
    logo: Union[str, 'ImageObject']
    offers: 'Offer'
    provider: Union['Organization', 'Person']
    providerMobility: str
    review: Union['Review', List['Review']]
    serviceOutput: Thing
    serviceType: str
    slogan: str
    termsOfService: Union[str, 'CreativeWork']
