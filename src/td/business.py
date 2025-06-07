
from datetime import datetime
from typing import Optional, List, Union

from .person import Person
from .creative_work import Review
from .media_object import ImageObject
from .place import Place, GeoShape, AdministrativeArea, Audience
from .rating import AggregateRating
from .values import PropertyValue, QuantitativeValue, StructuredValue
from .thing import Intangible, Thing, URL
from .organization import Organization
from .enums import BusinessFunction, OfferItemCondition, EnergyConsumptionDetails, WarrantyScope


class Product(Thing, total=False):
    """A product is anything that is made available for sale."""
    name: Optional[str]
    description: Optional[str]
    sku: Optional[str]
    mpn: Optional[str]
    brand: Optional["Brand"]
    manufacturer: Optional[Organization]
    review: Optional[Review]
    aggregateRating: Optional[AggregateRating]
    offers: Optional["Offer"]
    url: Optional[URL]
    gtin8: Optional[str]
    gtin12: Optional[str]
    gtin13: Optional[str]
    gtin14: Optional[str]
    productID: Optional[str]
    releaseDate: Optional[str]
    color: Optional[str]
    material: Optional[str]
    weight: Optional["QuantitativeValue"]
    height: Optional["QuantitativeValue"]
    width: Optional["QuantitativeValue"]
    depth: Optional["QuantitativeValue"]
    audience: Optional["Audience"]
    category: Optional[str]
    isAccessoryOrSparePartFor: Optional[List["Product"]]
    isConsumableFor: Optional[List["Product"]]
    isRelatedTo: Optional[List["Product"]]
    isSimilarTo: Optional[List["Product"]]
    itemCondition: Optional["OfferItemCondition"]
    model: Optional[str]
    additionalProperty: Optional[List["PropertyValue"]]
    award: Optional[str]
    gtin: Optional[str]
    hasEnergyConsumptionDetails: Optional["EnergyConsumptionDetails"]
    hasMeasurement: Optional["QuantitativeValue"]
    inProductGroupWithID: Optional[str]
    pattern: Optional[str]
    productLine: Optional["Product"]
    productionDate: Optional[str]
    purchaseDate: Optional[str]
    releaseNotes: Optional[str]
    slogan: Optional[str]
    nsn: Optional[str]


class PriceSpecification(Intangible, total=False):
    """A structured value representing a price or price range."""
    price: Optional[float]
    priceCurrency: Optional[str]
    eligibleQuantity: Optional[QuantitativeValue]
    eligibleTransactionVolume: Optional["PriceSpecification"]
    maxPrice: Optional[float]
    minPrice: Optional[float]
    validFrom: Optional[str]
    validThrough: Optional[str]
    valueAddedTaxIncluded: Optional[bool]
    billingIncrement: Optional[float]
    priceType: Optional[str]
    referenceQuantity: Optional[QuantitativeValue]
    unitCode: Optional[str]
    unitText: Optional[str]


class TypeAndQuantityNode(StructuredValue, total=False):
    """A structured value indicating the quantity, unit of measurement, and business function of goods included in a bundle offer."""
    amountOfThisGood: Optional[float]
    typeOfGood: Optional[Product]
    unitCode: Optional[str]
    typeOfGood: Optional[Product]
    amountOfThisGood: Optional[float]
    businessFunction: Optional[BusinessFunction]
    unitCode: Optional[str]
    unitText: Optional[str]
    valueAddedTaxIncluded: Optional[bool]


class WarrantyPromise(Intangible, total=False):
    """A structured value representing the duration and scope of services that will be provided to a customer free of charge in case of a defect or malfunction of a product."""
    durationOfWarranty: Optional[QuantitativeValue]
    warrantyScope: Optional[WarrantyScope]


class Offer(Intangible, total=False):
    """
    A class representing .org's Offer.
    See: https://.org/Offer
    """
    acceptedPaymentMethod: Optional[str]
    addOn: Optional["Offer"]
    advanceBookingRequirement: Optional[QuantitativeValue]
    areaServed: Optional[Union[Place, AdministrativeArea, GeoShape, str]]
    asin: Optional[str]
    availability: Optional[str]
    availabilityEnds: Optional[datetime]
    availabilityStarts: Optional[datetime]
    availableAtOrFrom: Optional[Place]
    availableDeliveryMethod: Optional[str]
    businessFunction: Optional[BusinessFunction]
    category: Optional[str]
    deliveryLeadTime: Optional[QuantitativeValue]
    eligibleCustomerType: Optional[str]
    eligibleDuration: Optional[QuantitativeValue]
    eligibleQuantity: Optional[QuantitativeValue]
    eligibleRegion: Optional[Union[Place, AdministrativeArea, GeoShape, str]]
    eligibleTransactionVolume: Optional[PriceSpecification]
    gtin12: Optional[str]
    gtin13: Optional[str]
    gtin14: Optional[str]
    gtin8: Optional[str]
    includesObject: Optional[TypeAndQuantityNode]
    ineligibleRegion: Optional[Union[Place, AdministrativeArea, GeoShape, str]]
    inventoryLevel: Optional[QuantitativeValue]
    itemCondition: Optional[OfferItemCondition]
    itemOffered: Optional[Product]
    mpn: Optional[str]
    priceSpecification: Optional[PriceSpecification]
    price: Optional[float]
    priceCurrency: Optional[str]
    seller: Optional[Organization]
    serialNumber: Optional[str]
    sku: Optional[str]
    validFrom: Optional[datetime]
    validThrough: Optional[datetime]
    warranty: Optional[WarrantyPromise]
    review: Optional[Review]
    aggregateRating: Optional[AggregateRating]
    url: Optional[URL]


class Demand(Intangible, total=False):
    """
    A class representing .org's Demand.
    See: https://.org/Demand
    """
    acceptedPaymentMethod: Optional[str]
    addOn: Optional[Offer]
    advanceBookingRequirement: Optional[QuantitativeValue]
    areaServed: Optional[Union[Place, AdministrativeArea, GeoShape, str]]
    asin: Optional[str]
    availability: Optional[str]
    availabilityEnds: Optional[datetime]
    availabilityStarts: Optional[datetime]
    availableAtOrFrom: Optional[Place]
    availableDeliveryMethod: Optional[str]
    businessFunction: Optional[BusinessFunction]
    category: Optional[str]
    deliveryLeadTime: Optional[QuantitativeValue]
    eligibleCustomerType: Optional[str]
    eligibleDuration: Optional[QuantitativeValue]
    eligibleQuantity: Optional[QuantitativeValue]
    eligibleRegion: Optional[Union[Place, AdministrativeArea, GeoShape, str]]
    eligibleTransactionVolume: Optional[PriceSpecification]
    gtin12: Optional[str]
    gtin13: Optional[str]
    gtin14: Optional[str]
    gtin8: Optional[str]
    includesObject: Optional[TypeAndQuantityNode]
    ineligibleRegion: Optional[Union[Place, AdministrativeArea, GeoShape, str]]
    inventoryLevel: Optional[QuantitativeValue]
    itemCondition: Optional[OfferItemCondition]
    itemOffered: Optional[Product]
    mpn: Optional[str]
    priceSpecification: Optional[PriceSpecification]
    seller: Optional[Organization]
    serialNumber: Optional[str]
    sku: Optional[str]
    validFrom: Optional[datetime]
    validThrough: Optional[datetime]
    warranty: Optional[WarrantyPromise]


class OwnershipInfo(Intangible, total=False):
    """
    A class representing .org's OwnershipInfo.
    See: https://.org/OwnershipInfo
    """
    acquiredFrom: Optional[Union[Organization, Person]]
    ownedFrom: Optional[datetime]
    ownedThrough: Optional[datetime]
    typeOfGood: Optional[Union[Product, List[Product]]]
    ownedQuantity: Optional[QuantitativeValue]
    # Inherits all fields from Intangible/Thing


class Brand(Intangible, total=False):
    """A brand is a name used by an organization or business person for labeling a product, product group, or similar."""
    logo: Optional[ImageObject]
    review: Optional[Review]
    aggregateRating: Optional[AggregateRating]
    slogan: Optional[str]
    url: Optional[URL]
    name: Optional[str]
    description: Optional[str]
    # The organization(s) that owns the brand (if different from the manufacturer).
    owner: Optional[Organization]
    # Products associated with this brand.
    product: Optional[List[Product]]
