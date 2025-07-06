from typing import TYPE_CHECKING, TypedDict, Union
from .thing import Intangible
from .data_type import DateTime
if TYPE_CHECKING:
    from .place import Place
    from .administrative_area import AdministrativeArea
    from .geo_shape import GeoShape
    from .quantitative_value import QuantitativeValue
    from .type_and_quantity_node import TypeAndQuantityNode
    from .price_specification import PriceSpecification
    from .organization import Organization
    from .product import Product
    from .warranty_promise import WarrantyPromise
    from .business import BusinessFunction, OfferItemCondition
    from .offer import Offer


class Demand(Intangible, TypedDict, total=False):
    """
    A class representing schema.org's Demand.
    See: https://schema.org/Demand
    """
    acceptedPaymentMethod: str
    addOn: 'Offer'
    advanceBookingRequirement: 'QuantitativeValue'
    areaServed: Union['Place', 'AdministrativeArea', 'GeoShape', str]
    asin: str
    availability: str
    availabilityEnds: DateTime
    availabilityStarts: DateTime
    availableAtOrFrom: 'Place'
    availableDeliveryMethod: str
    businessFunction: 'BusinessFunction'
    category: str
    deliveryLeadTime: 'QuantitativeValue'
    eligibleCustomerType: str
    eligibleDuration: 'QuantitativeValue'
    eligibleQuantity: 'QuantitativeValue'
    eligibleRegion: Union['Place', 'AdministrativeArea', 'GeoShape', str]
    eligibleTransactionVolume: 'PriceSpecification'
    gtin12: str
    gtin13: str
    gtin14: str
    gtin8: str
    includesObject: 'TypeAndQuantityNode'
    ineligibleRegion: Union['Place', 'AdministrativeArea', 'GeoShape', str]
    inventoryLevel: 'QuantitativeValue'
    itemCondition: 'OfferItemCondition'
    itemOffered: 'Product'
    mpn: str
    priceSpecification: 'PriceSpecification'
    seller: 'Organization'
    serialNumber: str
    sku: str
    validFrom: DateTime
    validThrough: DateTime
    warranty: 'WarrantyPromise'
