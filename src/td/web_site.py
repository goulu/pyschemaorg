from __future__ import annotations
from .creative_work import CreativeWork


class WebSite(CreativeWork, total=False):
    """
    A class representing schema.org's WebSite.
    See: https://schema.org/WebSite
    """
    issn: str
