from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict, Union, List
from .thing import Intangible

if TYPE_CHECKING:
    from .service import Service
    from .place import Place
    from .postal_address import PostalAddress
    from .contact_point import ContactPoint, ContactPointOption
    from .opening_hours_specification import OpeningHoursSpecification
    from .audience import Audience


class ServiceChannel(Intangible, TypedDict, total=False):
    """
    A class representing schema.org's ServiceChannel.
    See: https://schema.org/ServiceChannel
    """

    # Languages in which service is provided
    availableLanguage: Union[str, List[str]]

    # Estimated processing time for the service
    processingTime: str

    # The service provided through this channel
    providesService: Service

    # Location where the service can be provided
    serviceLocation: Union[Place, PostalAddress]

    # Phone number to use to access the service
    servicePhone: ContactPoint

    # Postal address for accessing the service
    servicePostalAddress: PostalAddress

    # SMS number to use to access the service
    serviceSmsNumber: ContactPoint

    # URL to access the service
    serviceUrl: str

    # Opening hours of the service channel
    hoursAvailable: OpeningHoursSpecification

    # Contact options for the service
    contactOption: ContactPointOption

    # Contact point for the service
    contactPoint: ContactPoint

    # Audience eligible for the service
    audience: Audience
