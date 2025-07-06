from __future__ import annotations
from typing import List, Union, TYPE_CHECKING
from .creative_work import CreativeWork
if TYPE_CHECKING:
    from .item_list import ItemList
    from .music_recording import MusicRecording


class MusicPlaylist(CreativeWork, total=False):
    """
    A class representing schema.org's MusicPlaylist.
    See: https://schema.org/MusicPlaylist
    """
    numTracks: int  # The number of tracks in this album or recording.
    # A music recording (track) that is part of this album.
    track: List[Union['ItemList', 'MusicRecording']]
