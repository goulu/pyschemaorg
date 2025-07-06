from __future__ import annotations
from typing import TypedDict
from .thing import Intangible


class StructuredValue(Intangible, TypedDict, total=False):
    """
    A class representing schema.org's StructuredValue.
    See: https://schema.org/StructuredValue
    """
    # StructuredValue does not define additional properties beyond Intangible as of June 2024.
    pass
