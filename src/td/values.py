from __future__ import annotations
from typing import Union, List
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
    additionalProperty: Union['PropertyValue', List['PropertyValue']]
    maxValue: Union[float, int]
    minValue: Union[float, int]
    unitCode: str
    unitText: str
    value: Union[str, float, int, bool, List[Union[str, float, int, bool]]]
    valueReference: Union[str, Thing, List[Union[str, Thing]]]


class PropertyValue(StructuredValue, total=False):
    """
    A class representing schema.org's PropertyValue.
    See: https://schema.org/PropertyValue
    """
    maxValue: Union[float, int]
    minValue: Union[float, int]
    unitCode: str
    unitText: str
    value: Union[str, float, int, bool, List[Union[str, float, int, bool]]]
    valueReference: Union[str, Thing, 'QuantitativeValue',
                          List[Union[str, Thing, 'QuantitativeValue']]]
    measurementTechnique: Union[str, List[str]]
    propertyID: str
