from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict, Union, List

from .media_object import MediaObject

if TYPE_CHECKING:
    from .person import Person
    from .creative_work import CreativeWork
    from .organization import Organization
    from .image_object import ImageObject


class VideoObject(MediaObject, TypedDict, total=False):
    """
    A class representing schema.org's VideoObject.
    See: https://schema.org/VideoObject
    """
    # An actor in the video.
    # See: https://schema.org/actor
    actor: Union[str, Person, List[Union[str, Person]]]
    # Caption for the video or transcript.
    # See: https://schema.org/caption
    caption: Union[str, CreativeWork, bool]
    # The director of the video.
    # See: https://schema.org/director
    director: Union[str, Person, List[Union[str, Person]]]
    # The composer or music group responsible for the music in the video.
    # See: https://schema.org/musicBy
    musicBy: Union[str, Person, Organization]
    # Thumbnail image for the video.
    # See: https://schema.org/thumbnail
    thumbnail: Union[str, ImageObject, List[Union[str, ImageObject]]]
    # Transcript of the video content.
    # See: https://schema.org/transcript
    transcript: str
    # The frame size of the video.
    # See: https://schema.org/videoFrameSize
    videoFrameSize: str
    # The quality of the video.
    # See: https://schema.org/videoQuality
    videoQuality: str
