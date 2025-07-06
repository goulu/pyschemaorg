from __future__ import annotations
from typing import TypedDict


from .structured_value import StructuredValue
from .administrative_area import AdministrativeArea


class Audience(StructuredValue, TypedDict, total=False):
    """
    A class representing schema.org's Audience.
    See: https://schema.org/Audience
    """
    audienceType: str
    geographicArea: AdministrativeArea
