from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict, Union, List

from .structured_value import StructuredValue
if TYPE_CHECKING:
    from .thing import Thing
    from .quantitative_value import QuantitativeValue


class PropertyValue(StructuredValue, TypedDict, total=False):
    """
    A class representing schema.org's PropertyValue.
    See: https://schema.org/PropertyValue
    """
    maxValue: Union[float, int]
    minValue: Union[float, int]
    unitCode: str
    unitText: str
    value: Union[str, float, int, bool]
    valueReference: Union[str, Thing, QuantitativeValue]
    measurementTechnique: Union[str, List[str]]
    propertyID: str
