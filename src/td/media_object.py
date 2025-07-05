from __future__ import annotations
from typing import Union, List
from .values import QuantitativeValue
from .creative_work import CreativeWork, CreativeWorkSeason, CreativeWorkSeries, Episode


class MediaObject(CreativeWork, total=False):
    """
    A class representing schema.org's MediaObject.
    See: https://schema.org/MediaObject
    """
    associatedArticle: CreativeWork
    bitrate: str
    contentSize: str
    contentUrl: str
    duration: str
    embedUrl: str
    encodesCreativeWork: CreativeWork
    endTime: str
    height: Union[str, QuantitativeValue]
    ineligibleRegion: Union[str, Place, List[Union[str, Place]]]
    playerType: str
    productionCompany: Organization
    regionsAllowed: Union[str, Place, List[Union[str, Place]]]
    requiresSubscription: Union[bool, str, CreativeWork]
    sha256: str
    startTime: str
    uploadDate: str
    width: Union[str, QuantitativeValue]
    # Inherits all fields from CreativeWork


class AudioObject(MediaObject, total=False):
    """
    A class representing schema.org's AudioObject.
    See: https://schema.org/AudioObject
    """
    caption: Union[str, CreativeWork]
    transcript: str
    # already in MediaObject
    regionsAllowed: Union[str, Place, List[Union[str, Place]]]
    productionCompany: Organization  # already in MediaObject
    # Inherits all fields from MediaObject


class ImageObject(MediaObject, total=False):
    """
    A class representing schema.org's ImageObject.
    See: https://schema.org/ImageObject
    """
    caption: Union[str, CreativeWork]
    exifData: Union[str, CreativeWork]
    representativeOfPage: bool
    thumbnail: Union[str, ImageObject, List[Union[str, ImageObject]]]
    associatedArticle: CreativeWork  # already in MediaObject
    embeddedTextCaption: str
    height: Union[str, QuantitativeValue]  # already in MediaObject
    width: Union[str, QuantitativeValue]  # already in MediaObject
    # Inherits all fields from MediaObject


class VideoObject(MediaObject, total=False):
    """
    A class representing schema.org's VideoObject.
    See: https://schema.org/VideoObject
    """
    actor: Union[str, Person, List[Union[str, Person]]]
    caption: Union[str, CreativeWork, bool]
    director: Union[str, Person, List[Union[str, Person]]]
    musicBy: Union[str, Person, Organization]
    thumbnail: Union[str, ImageObject, List[Union[str, ImageObject]]]
    transcript: str
    videoFrameSize: str
    videoQuality: str
    # Inherits all fields from MediaObject


class Clip(VideoObject, total=False):
    """
    A class representing schema.org's Clip.
    See: https://schema.org/Clip
    """
    actor: Union[str, Person, List[Union[str, Person]]]
    director: Union[str, Person, List[Union[str, Person]]]
    musicBy: Union[str, Person, Organization]
    partOfEpisode: Episode
    partOfSeason: CreativeWorkSeason
    partOfSeries: CreativeWorkSeries
    # Inherits all fields from VideoObject
