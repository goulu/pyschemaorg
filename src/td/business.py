from __future__ import annotations
from datetime import datetime
from typing import List, Union
from .thing import Intangible, Thing, URL
from .values import StructuredValue
from .enums import BusinessFunction, OfferItemCondition, EnergyConsumptionDetails, WarrantyScope


class Product(Thing, total=False):
    """A product is anything that is made available for sale."""
    name: str
    description: str
    sku: str
    mpn: str
    brand: Brand
    manufacturer: Organization
    review: Review
    aggregateRating: AggregateRating
    offers: Offer
    url: URL
    gtin8: str
    gtin12: str
    gtin13: str
    gtin14: str
    productID: str
    releaseDate: str
    color: str
    material: str
    weight: QuantitativeValue
    height: QuantitativeValue
    width: QuantitativeValue
    depth: QuantitativeValue
    audience: Audience
    category: str
    isAccessoryOrSparePartFor: List[Product]
    isConsumableFor: List[Product]
    isRelatedTo: List[Product]
    isSimilarTo: List[Product]
    itemCondition: OfferItemCondition
    model: str
    additionalProperty: List[PropertyValue]
    award: str
    gtin: str
    hasEnergyConsumptionDetails: EnergyConsumptionDetails
    hasMeasurement: QuantitativeValue
    inProductGroupWithID: str
    pattern: str
    productLine: Product
    productionDate: str
    purchaseDate: str
    releaseNotes: str
    slogan: str
    nsn: str


class PriceSpecification(Intangible, total=False):
    """A structured value representing a price or price range."""
    price: float
    priceCurrency: str
    eligibleQuantity: QuantitativeValue
    eligibleTransactionVolume: PriceSpecification
    maxPrice: float
    minPrice: float
    validFrom: str
    validThrough: str
    valueAddedTaxIncluded: bool
    billingIncrement: float
    priceType: str
    referenceQuantity: QuantitativeValue
    unitCode: str
    unitText: str


class TypeAndQuantityNode(StructuredValue, total=False):
    """A structured value indicating the quantity, unit of measurement, and business function of goods included in a bundle offer."""
    amountOfThisGood: float
    typeOfGood: Product
    unitCode: str
    businessFunction: BusinessFunction
    unitText: str
    valueAddedTaxIncluded: bool


class WarrantyPromise(Intangible, total=False):
    """A structured value representing the duration and scope of services that will be provided to a customer free of charge in case of a defect or malfunction of a product."""
    durationOfWarranty: QuantitativeValue
    warrantyScope: WarrantyScope


class Offer(Intangible, total=False):
    """
    A class representing schema.org's Offer.
    See: https://schema.org/Offer
    """
    acceptedPaymentMethod: str
    addOn: Offer
    advanceBookingRequirement: QuantitativeValue
    areaServed: Union[Place, AdministrativeArea, GeoShape, str]
    asin: str
    availability: str
    availabilityEnds: datetime
    availabilityStarts: datetime
    availableAtOrFrom: Place
    availableDeliveryMethod: str
    businessFunction: BusinessFunction
    category: str
    deliveryLeadTime: QuantitativeValue
    eligibleCustomerType: str
    eligibleDuration: QuantitativeValue
    eligibleQuantity: QuantitativeValue
    eligibleRegion: Union[Place, AdministrativeArea, GeoShape, str]
    eligibleTransactionVolume: PriceSpecification
    gtin12: str
    gtin13: str
    gtin14: str
    gtin8: str
    includesObject: TypeAndQuantityNode
    ineligibleRegion: Union[Place, AdministrativeArea, GeoShape, str]
    inventoryLevel: QuantitativeValue
    itemCondition: OfferItemCondition
    itemOffered: Product
    mpn: str
    priceSpecification: PriceSpecification
    price: float
    priceCurrency: str
    seller: Organization
    serialNumber: str
    sku: str
    validFrom: datetime
    validThrough: datetime
    warranty: WarrantyPromise
    review: Review
    aggregateRating: AggregateRating
    url: URL


class Demand(Intangible, total=False):
    """
    A class representing schema.org's Demand.
    See: https://schema.org/Demand
    """
    acceptedPaymentMethod: str
    addOn: Offer
    advanceBookingRequirement: QuantitativeValue
    areaServed: Union[Place, AdministrativeArea, GeoShape, str]
    asin: str
    availability: str
    availabilityEnds: datetime
    availabilityStarts: datetime
    availableAtOrFrom: Place
    availableDeliveryMethod: str
    businessFunction: BusinessFunction
    category: str
    deliveryLeadTime: QuantitativeValue
    eligibleCustomerType: str
    eligibleDuration: QuantitativeValue
    eligibleQuantity: QuantitativeValue
    eligibleRegion: Union[Place, AdministrativeArea, GeoShape, str]
    eligibleTransactionVolume: PriceSpecification
    gtin12: str
    gtin13: str
    gtin14: str
    gtin8: str
    includesObject: TypeAndQuantityNode
    ineligibleRegion: Union[Place, AdministrativeArea, GeoShape, str]
    inventoryLevel: QuantitativeValue
    itemCondition: OfferItemCondition
    itemOffered: Product
    mpn: str
    priceSpecification: PriceSpecification
    seller: Organization
    serialNumber: str
    sku: str
    validFrom: datetime
    validThrough: datetime
    warranty: WarrantyPromise


class OwnershipInfo(Intangible, total=False):
    """
    A class representing schema.org's OwnershipInfo.
    See: https://schema.org/OwnershipInfo
    """
    acquiredFrom: Union[Organization, Person]
    ownedFrom: datetime
    ownedThrough: datetime
    typeOfGood: Union[Product, List[Product]]
    ownedQuantity: QuantitativeValue


class Brand(Intangible, total=False):
    """A brand is a name used by an organization or business person for labeling a product, product group, or similar."""
    logo: ImageObject
    review: Review
    aggregateRating: AggregateRating
    slogan: str
    url: URL
    name: str
    description: str
    owner: Organization
    product: List[Product]
