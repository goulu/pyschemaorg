from typing import TYPE_CHECKING, TypedDict
from .structured_value import StructuredValue
if TYPE_CHECKING:
    from .product import Product
    from .business import BusinessFunction


class TypeAndQuantityNode(StructuredValue, TypedDict, total=False):
    """A structured value indicating the quantity, unit of measurement, and business function of goods included
    in a bundle offer."""
    amountOfThisGood: float
    typeOfGood: Product
    unitCode: str
    businessFunction: BusinessFunction
    unitText: str
    valueAddedTaxIncluded: bool
