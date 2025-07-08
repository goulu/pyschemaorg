from __future__ import annotations
from typing import TypedDict
from .thing import Intangible


class Language(Intangible, TypedDict, total=False):
    """
    A class representing schema.org's Language.
    See: https://schema.org/Language
    """
    pass
