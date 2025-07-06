from __future__ import annotations
from typing import TypedDict, Union, List, TYPE_CHECKING
from .creative_work import CreativeWork

if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue
    from .place import Place
    from .organization import Organization


class MediaObject(CreativeWork, TypedDict, total=False):
    """
    A class representing schema.org's MediaObject.
    See: https://schema.org/MediaObject
    """
    # A NewsArticle associated with the MediaObject.
    # See: https://schema.org/associatedArticle
    associatedArticle: CreativeWork
    # The bitrate of the media object.
    # See: https://schema.org/bitrate
    bitrate: str
    # File size in (mega/kilo) bytes.
    # See: https://schema.org/contentSize
    contentSize: str
    # Actual bytes of the media object, for example the image file or video file.
    # See: https://schema.org/contentUrl
    contentUrl: str
    # Duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format.
    # See: https://schema.org/duration
    duration: str
    # A URL pointing to a player for a specific video.
    # See: https://schema.org/embedUrl
    embedUrl: str
    # The CreativeWork encoded by this media object.
    # See: https://schema.org/encodesCreativeWork
    encodesCreativeWork: CreativeWork
    # The end time of the event or item.
    # See: https://schema.org/endTime
    endTime: str
    # The height of the item.
    # See: https://schema.org/height
    height: Union[str, QuantitativeValue]
    # The region(s) for which the media is ineligible.
    # See: https://schema.org/ineligibleRegion
    ineligibleRegion: Union[str, Place, List[Union[str, Place]]]
    # Player type required—for example, Flash or Silverlight.
    # See: https://schema.org/playerType
    playerType: str
    # The production company or studio responsible for the item.
    # See: https://schema.org/productionCompany
    productionCompany: Organization
    # The region(s) for which the media is allowed.
    # See: https://schema.org/regionsAllowed
    regionsAllowed: Union[str, Place, List[Union[str, Place]]]
    # Indicates if subscription is required.
    # See: https://schema.org/requiresSubscription
    requiresSubscription: Union[bool, str, CreativeWork]
    # The SHA-256 hash of the content.
    # See: https://schema.org/sha256
    sha256: str
    # The start time of the event or item.
    # See: https://schema.org/startTime
    startTime: str
    # Date when this media object was uploaded to this site.
    # See: https://schema.org/uploadDate
    uploadDate: str
    # The width of the item.
    # See: https://schema.org/width
    width: Union[str, QuantitativeValue]
