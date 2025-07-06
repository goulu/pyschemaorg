from __future__ import annotations
from typing import TYPE_CHECKING, Union, List
from .media_object import MediaObject

if TYPE_CHECKING:
    from .creative_work import CreativeWork
    from .quantitative_value import QuantitativeValue


class ImageObject(MediaObject, total=False):
    """
    A class representing schema.org's ImageObject.
    See: https://schema.org/ImageObject
    """
    # Caption for the image.
    # See: https://schema.org/caption
    caption: Union[str, CreativeWork]
    # EXIF data for the image.
    # See: https://schema.org/exifData
    exifData: Union[str, CreativeWork]
    # Indicates whether this image is representative of the content of the page.
    # See: https://schema.org/representativeOfPage
    representativeOfPage: bool
    # Thumbnail image for the content.
    # See: https://schema.org/thumbnail
    thumbnail: Union[str, ImageObject, List[Union[str, ImageObject]]]
    # Associated article for the image.
    # See: https://schema.org/associatedArticle
    associatedArticle: CreativeWork
    # Embedded text caption for the image.
    # See: https://schema.org/embeddedTextCaption
    embeddedTextCaption: str
    # Height of the image.
    # See: https://schema.org/height
    height: Union[str, QuantitativeValue]
    # Width of the image.
    # See: https://schema.org/width
    width: Union[str, QuantitativeValue]
