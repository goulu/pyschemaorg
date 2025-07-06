from typing import TYPE_CHECKING, TypedDict, Union
from .thing import Intangible, URL
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
    from .review import Review
    from .aggregate_rating import AggregateRating
    from .business import BusinessFunction, OfferItemCondition


class Offer(Intangible, TypedDict, total=False):
    """
    A class representing schema.org's Offer.
    See: https://schema.org/Offer
    """
    acceptedPaymentMethod: str  # The payment method(s) accepted by seller for this offer.
    # An additional offer that can only be obtained in combination with the first offer.
    addOn: 'Offer'
    # The amount of time that is required between accepting the offer and the actual usage of the resource or service.
    advanceBookingRequirement: 'QuantitativeValue'
    # The geographic area where a service or offered item is provided.
    areaServed: Union['Place', 'AdministrativeArea', 'GeoShape', str]
    asin: str  # Amazon Standard Identification Number (ASIN).
    # The availability of this item—for example In stock, Out of stock, Pre-order, etc.
    availability: str
    # The end of the availability of the product or service included in the offer.
    availabilityEnds: DateTime
    # The beginning of the availability of the product or service included in the offer.
    availabilityStarts: DateTime
    # The place(s) from which the offer can be obtained (e.g. store locations).
    availableAtOrFrom: 'Place'
    # The delivery method(s) available for this offer.
    availableDeliveryMethod: str
    # The business function (e.g. sell, lease, repair, dispose) of the offer.
    businessFunction: 'BusinessFunction'
    category: str  # A category for the item.
    # The typical delay between the receipt of the order and the goods leaving the warehouse.
    deliveryLeadTime: 'QuantitativeValue'
    # The type(s) of customers for which the offer is eligible.
    eligibleCustomerType: str
    # The duration for which the offer is valid.
    eligibleDuration: 'QuantitativeValue'
    # The interval and unit of measurement of ordering quantities for which the offer or price specification is valid.
    eligibleQuantity: 'QuantitativeValue'
    # The region(s) for which the offer or delivery is available.
    eligibleRegion: Union['Place', 'AdministrativeArea', 'GeoShape', str]
    # The transaction volume, in a monetary unit, for which the offer or price specification is valid.
    eligibleTransactionVolume: 'PriceSpecification'
    # The GTIN-12 code of the product, or the product to which the offer refers.
    gtin12: str
    # The GTIN-13 code of the product, or the product to which the offer refers.
    gtin13: str
    # The GTIN-14 code of the product, or the product to which the offer refers.
    gtin14: str
    # The GTIN-8 code of the product, or the product to which the offer refers.
    gtin8: str
    # This links to a node describing a quantity and business function of goods included in the offer.
    includesObject: 'TypeAndQuantityNode'
    # The region(s) for which the offer or delivery is not available.
    ineligibleRegion: Union['Place', 'AdministrativeArea', 'GeoShape', str]
    # The current approximate inventory level for the item or items.
    inventoryLevel: 'QuantitativeValue'
    # A predefined value from OfferItemCondition specifying the condition of the product or service.
    itemCondition: 'OfferItemCondition'
    itemOffered: 'Product'  # The item being offered.
    # The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.
    mpn: str
    # One or more detailed price specifications, indicating the unit price and delivery or payment charges.
    priceSpecification: 'PriceSpecification'
    # The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.
    price: float
    # The currency (in 3-letter ISO 4217 format) of the price or a price component.
    priceCurrency: str
    # An entity which offers (sells / leases / lends / loans) the services / goods.
    seller: 'Organization'
    # The serial number or any alphanumeric identifier of a particular product.
    serialNumber: str
    # The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service.
    sku: str
    validFrom: DateTime  # The date when the item becomes valid.
    validThrough: DateTime  # The date after when the item is not valid.
    # The warranty promise(s) included in the offer.
    warranty: 'WarrantyPromise'
    review: 'Review'  # A review of the item.
    # The overall rating, based on a collection of reviews or ratings, of the item.
    aggregateRating: 'AggregateRating'
    url: URL  # URL of the item.
