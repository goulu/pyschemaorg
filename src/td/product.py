from typing import List, TYPE_CHECKING
from .thing import Thing, URL
from .enums import EnergyConsumptionDetails
from .business import OfferItemCondition
if TYPE_CHECKING:
    from .brand import Brand
    from .organization import Organization
    from .review import Review
    from .aggregate_rating import AggregateRating
    from .offer import Offer
    from .quantitative_value import QuantitativeValue
    from .audience import Audience
    from .property_value import PropertyValue


class Product(Thing, total=False):
    """A product is anything that is made available for sale."""
    name: str
    description: str
    sku: str
    mpn: str
    brand: 'Brand'
    manufacturer: 'Organization'
    review: 'Review'
    aggregateRating: 'AggregateRating'
    offers: 'Offer'
    url: URL
    gtin8: str
    gtin12: str
    gtin13: str
    gtin14: str
    productID: str
    releaseDate: str
    color: str
    material: str
    weight: 'QuantitativeValue'
    height: 'QuantitativeValue'
    width: 'QuantitativeValue'
    depth: 'QuantitativeValue'
    audience: 'Audience'
    category: str
    isAccessoryOrSparePartFor: List['Product']
    isConsumableFor: List['Product']
    isRelatedTo: List['Product']
    isSimilarTo: List['Product']
    itemCondition: OfferItemCondition
    model: str
    additionalProperty: List['PropertyValue']
    award: str
    gtin: str
    hasEnergyConsumptionDetails: EnergyConsumptionDetails
    hasMeasurement: 'QuantitativeValue'
    inProductGroupWithID: str
    pattern: str
    productLine: 'Product'
    productionDate: str
    purchaseDate: str
    releaseNotes: str
    slogan: str
    nsn: str
