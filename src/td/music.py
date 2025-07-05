from __future__ import annotations
from typing import List, Union, Text

from .thing import URL
from .date_time import Duration
from .event import Event, PublicationEvent
from .person import Person
from .types import ItemList
from .organization import Organization
from .creative_work import CreativeWork
import enum


class MusicPlaylist(CreativeWork, total=False):
    """
    A class representing schema.org's MusicPlaylist.
    See: https://schema.org/MusicPlaylist
    """
    numTracks: int
    track: List[Union[ItemList, MusicRecording]]


class MusicGroup(Organization, total=False):
    """
    A class representing schema.org's MusicGroup.
    See: https://schema.org/MusicGroup
    """
    genre: Union[Text, URL]
    # Could be MusicAlbum, using str for simplicity
    album: List[str]
    # Could be MusicRecording, using str for simplicity
    track: List[str]


class MusicRecording(CreativeWork, total=False):
    """
    A class representing schema.org's MusicRecording.
    See: https://schema.org/MusicRecording
    """
    byArtist: Union[MusicGroup, Person]
    duration: Duration
    inAlbum: MusicAlbum
    inPlaylist: MusicPlaylist
    isrcCode: Text
    recordingOf: MusicComposition
    releasedEvent: PublicationEvent


class MusicComposition(CreativeWork, total=False):
    """
    A class representing schema.org's MusicComposition.
    See: https://schema.org/MusicComposition
    """
    composer: Union[Organization, Person]
    firstPerformance: Event
    includedComposition: MusicComposition
    iswcCode: Text
    lyricist: Person
    lyrics: CreativeWork
    musicArrangement: MusicComposition
    musicCompositionForm: Text
    musicalKey: Text
    recordedAs: MusicRecording


class MusicAlbumProductionType(enum.Enum):
    """
    Enum for MusicAlbumProductionType.
    See: https://schema.org/MusicAlbumProductionType
    """
    AlbumRelease = "AlbumRelease"
    CompilationAlbum = "CompilationAlbum"
    DemoAlbum = "DemoAlbum"
    DJMixAlbum = "DJMixAlbum"
    LiveAlbum = "LiveAlbum"
    MixtapeAlbum = "MixtapeAlbum"
    RemixAlbum = "RemixAlbum"
    SoundtrackAlbum = "SoundtrackAlbum"
    SpokenWordAlbum = "SpokenWordAlbum"
    StudioAlbum = "StudioAlbum"


class MusicRelease(CreativeWork, total=False):
    """
    A class representing schema.org's MusicRelease.
    See: https://schema.org/MusicRelease
    """
    catalogNumber: Text
    creditedTo: Union[Organization, Person]
    duration: Duration
    musicReleaseFormat: MusicReleaseFormatType
    recordLabel: Organization
    releaseOf: MusicAlbum


class MusicAlbumReleaseType(enum.Enum):
    """
    Enum for MusicAlbumReleaseType.
    See: https://schema.org/MusicAlbumReleaseType
    """
    AlbumRelease = "AlbumRelease"
    BroadcastRelease = "BroadcastRelease"
    EPRelease = "EPRelease"
    SingleRelease = "SingleRelease"


class MusicReleaseFormatType(enum.Enum):
    """
    Enum for MusicReleaseFormatType.
    See: https://schema.org/MusicReleaseFormatType
    """
    CassetteFormat = "CassetteFormat"
    CDFormat = "CDFormat"
    DATFormat = "DATFormat"
    DigitalAudioTapeFormat = "DigitalAudioTapeFormat"
    DigitalFormat = "DigitalFormat"
    DVDFormat = "DVDFormat"
    LaserDiscFormat = "LaserDiscFormat"
    VinylFormat = "VinylFormat"


class MusicAlbum(CreativeWork, total=False):
    """
    A class representing schema.org's MusicAlbum.
    See: https://schema.org/MusicAlbum
    """
    albumProductionType: Optional[MusicAlbumProductionType]
    albumRelease: Optional[MusicRelease]
    albumReleaseType: Optional[MusicAlbumReleaseType]
    byArtist: Optional[Union[MusicGroup, Person]]
    numTracks: Optional[int]
    track: Optional[List[Union[ItemList, MusicRecording]]]


class MusicEvent(Event, total=False):
    """
    A class representing schema.org's MusicEvent.
    See: https://schema.org/MusicEvent
    """
    pass
