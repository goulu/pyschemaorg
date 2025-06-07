from typing import List, Optional, Text, Union

from orm.schema import URL
from .date_time import Duration
from .event import Event, PublicationEvent
from .person import Person
from .types import ItemList
from .organization import Organization
from .creative_work import CreativeWork
import enum


class MusicPlaylist(CreativeWork, total=False):
    """
    A class representing .org's MusicPlaylist.
    See: https://.org/MusicPlaylist
    """
    numTracks: Optional[int]
    track: Optional[List[Union[ItemList, 'MusicRecording']]]


class MusicGroup(Organization, total=False):
    """
    A class representing .org's MusicGroup.
    See: https://.org/MusicGroup
    """
    genre: Optional[Union[Text, URL]]
    # Could be MusicAlbum, using str for simplicity
    album: Optional[List[str]]
    # Could be MusicRecording, using str for simplicity
    track: Optional[List[str]]


class MusicRecording(CreativeWork, total=False):
    """
    A class representing .org's MusicRecording.
    See: https://.org/MusicRecording
    """
    byArtist: Optional[Union[MusicGroup, Person]]
    duration: Optional[Duration]
    inAlbum: Optional['MusicAlbum']
    inPlaylist: Optional[MusicPlaylist]
    isrcCode: Optional[Text]
    recordingOf: Optional['MusicComposition']
    releasedEvent: Optional[PublicationEvent]


class MusicComposition(CreativeWork, total=False):
    """
    A class representing .org's MusicComposition.
    See: https://.org/MusicComposition
    """
    composer: Optional[Union[Organization, Person]]
    firstPerformance: Optional[Event]
    includedComposition: Optional['MusicComposition']
    iswcCode: Optional[Text]
    lyricist: Optional[Person]
    lyrics: Optional[CreativeWork]
    musicArrangement: Optional['MusicComposition']
    musicCompositionForm: Optional[Text]
    musicalKey: Optional[Text]
    recordedAs: Optional[MusicRecording]


class MusicAlbumProductionType(enum.Enum):
    """
    Enum for MusicAlbumProductionType.
    See: https://.org/MusicAlbumProductionType
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
    A class representing .org's MusicRelease.
    See: https://.org/MusicRelease
    """
    catalogNumber: Optional[Text]
    creditedTo: Optional[Union[Organization, Person]]
    duration: Optional[Duration]
    musicReleaseFormat: Optional['MusicReleaseFormatType']
    recordLabel: Optional[Organization]
    releaseOf: Optional['MusicAlbum']


class MusicAlbumReleaseType(enum.Enum):
    """
    Enum for MusicAlbumReleaseType.
    See: https://.org/MusicAlbumReleaseType
    """
    AlbumRelease = "AlbumRelease"
    BroadcastRelease = "BroadcastRelease"
    EPRelease = "EPRelease"
    SingleRelease = "SingleRelease"


class MusicReleaseFormatType(enum.Enum):
    """
    Enum for MusicReleaseFormatType.
    See: https://.org/MusicReleaseFormatType
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
    A class representing .org's MusicAlbum.
    See: https://.org/MusicAlbum
    """
    albumProductionType: Optional['MusicAlbumProductionType']
    albumRelease: Optional['MusicRelease']
    albumReleaseType: Optional['MusicAlbumReleaseType']
    byArtist: Optional[Union[MusicGroup, Person]]
    numTracks: Optional[int]
    track: Optional[List[Union[ItemList, MusicRecording]]]

class MusicEvent(Event, total=False):
    """
    A class representing .org's MusicEvent.
    See: https://.org/MusicEvent
    """
    pass