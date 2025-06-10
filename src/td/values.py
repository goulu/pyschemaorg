from __future__ import annotations
from typing import Optional, Union, List
from .thing import Thing, Intangible


class StructuredValue(Intangible, total=False):
    """
    A class representing schema.org's StructuredValue.
    See: https://schema.org/StructuredValue
    """
    # StructuredValue does not define additional properties beyond Intangible as of June 2024.
    pass


class QuantitativeValue(StructuredValue, total=False):
    """
    A class representing schema.org's QuantitativeValue.
    See: https://schema.org/QuantitativeValue
    """
    additionalProperty: Optional[Union[PropertyValue, List[PropertyValue]]]
    maxValue: Optional[Union[float, int]]
    minValue: Optional[Union[float, int]]
    unitCode: Optional[str]
    unitText: Optional[str]
    value: Optional[Union[str, float, int, bool,
                          List[Union[str, float, int, bool]]]]
    valueReference: Optional[Union[str, Thing, List[Union[str, Thing]]]]


class PropertyValue(StructuredValue, total=False):
    """
    A class representing schema.org's PropertyValue.
    See: https://schema.org/PropertyValue
    """
    maxValue: Optional[Union[float, int]]
    minValue: Optional[Union[float, int]]
    unitCode: Optional[str]
    unitText: Optional[str]
    value: Optional[Union[str, float, int, bool,
                          List[Union[str, float, int, bool]]]]
    valueReference: Optional[Union[str, Thing, QuantitativeValue,
                                   List[Union[str, Thing, QuantitativeValue]]]]
    measurementTechnique: Optional[Union[str, List[str]]]
    propertyID: Optional[str]
