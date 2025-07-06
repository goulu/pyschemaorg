from __future__ import annotations
from typing import TypedDict, Union, List
from .structured_value import StructuredValue
from .thing import Thing
from .property_value import PropertyValue


class QuantitativeValue(StructuredValue, TypedDict, total=False):
    """
    A class representing schema.org's QuantitativeValue.
    See: https://schema.org/QuantitativeValue
    """
    additionalProperty: Union[PropertyValue, List[PropertyValue]]
    maxValue: Union[float, int]
    minValue: Union[float, int]
    unitCode: str
    unitText: str
    value: Union[str, float, int, bool, List[Union[str, float, int, bool]]]
    valueReference: Union[str, Thing, List[Union[str, Thing]]]
