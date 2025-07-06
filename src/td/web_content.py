from __future__ import annotations
from typing import TypedDict
from .creative_work import CreativeWork


# WebContent: https://schema.org/WebContent
class WebContent(CreativeWork, TypedDict, total=False):
    """
    A class representing schema.org's WebContent.
    WebContent is a type of CreativeWork that represents web-based content, such as web pages,
    articles, or other resources published on the web.
    See: https://schema.org/WebContent
    """
    pass
