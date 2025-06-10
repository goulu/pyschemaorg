from __future__ import annotations
from typing import Optional, Union, List
from .values import QuantitativeValue
from .creative_work import CreativeWork, CreativeWorkSeason, CreativeWorkSeries, Episode


class MediaObject(CreativeWork, total=False):
    """
    A class representing schema.org's MediaObject.
    See: https://schema.org/MediaObject
    """
    associatedArticle: Optional[CreativeWork]
    bitrate: Optional[str]
    contentSize: Optional[str]
    contentUrl: Optional[str]
    duration: Optional[str]
    embedUrl: Optional[str]
    encodesCreativeWork: Optional[CreativeWork]
    endTime: Optional[str]
    height: Optional[Union[str, QuantitativeValue]]
    ineligibleRegion: Optional[Union[str, Place, List[Union[str, Place]]]]
    playerType: Optional[str]
    productionCompany: Optional[Organization]
    regionsAllowed: Optional[Union[str, Place, List[Union[str, Place]]]]
    requiresSubscription: Optional[Union[bool, str, CreativeWork]]
    sha256: Optional[str]
    startTime: Optional[str]
    uploadDate: Optional[str]
    width: Optional[Union[str, QuantitativeValue]]
    # Inherits all fields from CreativeWork


class AudioObject(MediaObject, total=False):
    """
    A class representing schema.org's AudioObject.
    See: https://schema.org/AudioObject
    """
    caption: Optional[Union[str, CreativeWork]]
    transcript: Optional[str]
    # already in MediaObject
    regionsAllowed: Optional[Union[str, Place, List[Union[str, Place]]]]
    productionCompany: Optional[Organization]  # already in MediaObject
    # Inherits all fields from MediaObject


class ImageObject(MediaObject, total=False):
    """
    A class representing schema.org's ImageObject.
    See: https://schema.org/ImageObject
    """
    caption: Optional[Union[str, CreativeWork]]
    exifData: Optional[Union[str, CreativeWork]]
    representativeOfPage: Optional[bool]
    thumbnail: Optional[Union[str, ImageObject,
                              List[Union[str, ImageObject]]]]
    associatedArticle: Optional[CreativeWork]  # already in MediaObject
    embeddedTextCaption: Optional[str]
    height: Optional[Union[str, QuantitativeValue]]  # already in MediaObject
    width: Optional[Union[str, QuantitativeValue]]  # already in MediaObject
    # Inherits all fields from MediaObject


class VideoObject(MediaObject, total=False):
    """
    A class representing schema.org's VideoObject.
    See: https://schema.org/VideoObject
    """
    actor: Optional[Union[str, Person, List[Union[str, Person]]]]
    caption: Optional[Union[str, CreativeWork, bool]]
    director: Optional[Union[str, Person, List[Union[str, Person]]]]
    musicBy: Optional[Union[str, Person, Organization]]
    thumbnail: Optional[Union[str, ImageObject,
                              List[Union[str, ImageObject]]]]
    transcript: Optional[str]
    videoFrameSize: Optional[str]
    videoQuality: Optional[str]
    # Inherits all fields from MediaObject


class Clip(VideoObject, total=False):
    """
    A class representing schema.org's Clip.
    See: https://schema.org/Clip
    """
    actor: Optional[Union[str, Person, List[Union[str, Person]]]]
    director: Optional[Union[str, Person, List[Union[str, Person]]]]
    musicBy: Optional[Union[str, Person, Organization]]
    partOfEpisode: Optional[Episode]
    partOfSeason: Optional[CreativeWorkSeason]
    partOfSeries: Optional[CreativeWorkSeries]
    # Inherits all fields from VideoObject
