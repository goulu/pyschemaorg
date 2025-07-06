from __future__ import annotations
from typing import Union, List, TYPE_CHECKING
from .creative_work import CreativeWork
if TYPE_CHECKING:
    from .music_album_production_type import MusicAlbumProductionType
    from .music_release import MusicRelease
    from .music_album_release_type import MusicAlbumReleaseType
    from .music_group import MusicGroup
    from .person import Person
    from .item_list import ItemList
    from .music_recording import MusicRecording


class MusicAlbum(CreativeWork, total=False):
    """
    A class representing schema.org's MusicAlbum.
    See: https://schema.org/MusicAlbum
    """
    albumProductionType: MusicAlbumProductionType  # The kind of release which this album is: single, EP or album.
    albumRelease: 'MusicRelease'  # A release of this album.
    # The kind of release which this album is: single, EP or album.
    albumReleaseType: 'MusicAlbumReleaseType'
    # The artist that performed this album or recording.
    byArtist: Union['MusicGroup', 'Person']
    numTracks: int  # The number of tracks in this album or recording.
    # A music recording (track) that is part of this album.
    track: List[Union['ItemList', 'MusicRecording']]
