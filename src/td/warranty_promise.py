from typing import TYPE_CHECKING, TypedDict
from .thing import Intangible
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue
    from .enums import WarrantyScope


class WarrantyPromise(Intangible, TypedDict, total=False):
    """A structured value representing the duration and scope of services that will be provided to a customer
    free of charge in case of a defect or malfunction of a product."""
    durationOfWarranty: QuantitativeValue
    warrantyScope: WarrantyScope
