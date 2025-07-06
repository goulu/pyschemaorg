import enum


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
