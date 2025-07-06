from __future__ import annotations
from typing import Union, TYPE_CHECKING
from .creative_work import CreativeWork
if TYPE_CHECKING:
    from .music_group import MusicGroup
    from .person import Person
    from .music_album import MusicAlbum
    from .music_playlist import MusicPlaylist
    from .music_composition import MusicComposition
    from .publication_event import PublicationEvent


class MusicRecording(CreativeWork, total=False):
    """
    A class representing schema.org's MusicRecording.
    See: https://schema.org/MusicRecording
    """
    byArtist: Union['MusicGroup',
                    # The artist that performed this album or recording.
                    'Person']
    duration: str  # The duration of the item (as ISO 8601 duration).
    inAlbum: 'MusicAlbum'  # The album to which this recording belongs.
    # The playlist to which this recording belongs.
    inPlaylist: 'MusicPlaylist'
    # The International Standard Recording Code for the recording.
    isrcCode: str
    # The composition this recording is a recording of.
    recordingOf: 'MusicComposition'
    # The event where the recording was released.
    releasedEvent: 'PublicationEvent'
