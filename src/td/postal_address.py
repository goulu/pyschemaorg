from __future__ import annotations
from typing import Union

from .contact_point import ContactPoint
from .country import Country


class PostalAddress(ContactPoint, total=False):
    """
    A class representing schema.org's PostalAddress.
    See: https://schema.org/PostalAddress
    """
    # The country. For example, USA. You can also provide the two-letter
    # ISO 3166-1 alpha-2 country code.
    addressCountry: Union[str, Country]
    addressLocality: str  # The locality. For example, Mountain View.
    addressRegion: str  # The region. For example, CA.
    extendedAddress: str  # The extended address. For example, Suite 100.
    # The post office box number for PO box addresses.
    postOfficeBoxNumber: str
    postalCode: str  # The postal code. For example, 94043.
    # The street address. For example, 1600 Amphitheatre Pkwy.
    streetAddress: str
