from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict, Union, List
from .media_object import MediaObject

if TYPE_CHECKING:
    from .creative_work import CreativeWork
    from .place import Place
    from .organization import Organization


class AudioObject(MediaObject, TypedDict, total=False):
    """
    A class representing schema.org's AudioObject.
    See: https://schema.org/AudioObject
    """
    # Caption for the audio or transcript.
    # See: https://schema.org/caption
    caption: Union[str, CreativeWork]
    # Transcript of the audio content.
    # See: https://schema.org/transcript
    transcript: str
    # Regions where the media is allowed.
    # See: https://schema.org/regionsAllowed
    regionsAllowed: Union[str, Place, List[Union[str, Place]]]
    # The production company or studio responsible for the audio.
    # See: https://schema.org/productionCompany
    productionCompany: Organization
