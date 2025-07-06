import enum


class MusicAlbumReleaseType(enum.Enum):
    """
    Enum for MusicAlbumReleaseType.
    See: https://schema.org/MusicAlbumReleaseType
    """
    AlbumRelease = "AlbumRelease"
    BroadcastRelease = "BroadcastRelease"
    EPRelease = "EPRelease"
    SingleRelease = "SingleRelease"
