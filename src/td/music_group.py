from __future__ import annotations
from typing import Union, List, TYPE_CHECKING
from .organization import Organization
from .data_type import Text, URL
if TYPE_CHECKING:
    from .music_album import MusicAlbum
    from .music_recording import MusicRecording


class MusicGroup(Organization, total=False):
    """
    A class representing schema.org's MusicGroup.
    See: https://schema.org/MusicGroup
    """
    genre: Union[Text,
                 # Genre of the creative work, broadcast channel or group.
                 URL]
    album: List['MusicAlbum']  # A music album.
    track: List['MusicRecording']  # A music recording (track).
