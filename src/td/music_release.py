from __future__ import annotations
from typing import Union, TYPE_CHECKING
from .creative_work import CreativeWork
if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person
    from .music_release_format_type import MusicReleaseFormatType
    from .music_album import MusicAlbum


class MusicRelease(CreativeWork, total=False):
    """
    A class representing schema.org's MusicRelease.
    See: https://schema.org/MusicRelease
    """
    catalogNumber: str  # The catalog number for the release.
    # The group the release is credited to.
    creditedTo: Union[Organization, Person]
    duration: str  # The duration of the item (as ISO 8601 duration).
    # The format of the release (e.g. CD, digital, vinyl, etc.).
    musicReleaseFormat: MusicReleaseFormatType
    recordLabel: Organization  # The label that issued the release.
    releaseOf: MusicAlbum  # The album this is a release of.
