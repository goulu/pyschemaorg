from __future__ import annotations
from .administrative_area import AdministrativeArea


class Country(AdministrativeArea, total=False):
    """
    A class representing schema.org's Country.
    See: https://schema.org/Country
    """
    pass
