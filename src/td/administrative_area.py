from __future__ import annotations
from typing import TypedDict
from .place import Place


class AdministrativeArea(Place, TypedDict, total=False):
    """
    A class representing schema.org's AdministrativeArea.
    See: https://schema.org/AdministrativeArea
    """
    pass
