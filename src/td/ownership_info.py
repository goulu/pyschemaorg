from typing import TYPE_CHECKING, List, Union
from .thing import Intangible
from .data_type import DateTime
if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person
    from .product import Product
    from .quantitative_value import QuantitativeValue


class OwnershipInfo(Intangible, total=False):
    """
    A class representing schema.org's OwnershipInfo.
    See: https://schema.org/OwnershipInfo
    """
    acquiredFrom: Union[Organization, Person]
    ownedFrom: DateTime
    ownedThrough: DateTime
    typeOfGood: Union[Product, List[Product]]
    ownedQuantity: QuantitativeValue
