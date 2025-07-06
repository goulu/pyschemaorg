from typing import TYPE_CHECKING
from .thing import Intangible
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue


class PriceSpecification(Intangible, total=False):
    """A structured value representing a price or price range."""
    price: float
    priceCurrency: str
    eligibleQuantity: 'QuantitativeValue'
    eligibleTransactionVolume: 'PriceSpecification'
    maxPrice: float
    minPrice: float
    validFrom: str
    validThrough: str
    valueAddedTaxIncluded: bool
    billingIncrement: float
    priceType: str
    referenceQuantity: 'QuantitativeValue'
    unitCode: str
    unitText: str
