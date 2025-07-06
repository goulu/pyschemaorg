from __future__ import annotations
from typing import TYPE_CHECKING, Union, List
from .video_object import VideoObject

if TYPE_CHECKING:
    from .person import Person
    from .organization import Organization
    from .episode import Episode
    from .creative_work_season import CreativeWorkSeason
    from .creative_work_series import CreativeWorkSeries


class Clip(VideoObject, total=False):
    """
    A class representing schema.org's Clip.
    See: https://schema.org/Clip
    """
    # An actor in the clip.
    # See: https://schema.org/actor
    actor: Union[str, Person, List[Union[str, Person]]]
    # The director of the clip.
    # See: https://schema.org/director
    director: Union[str, Person, List[Union[str, Person]]]
    # The composer or music group responsible for the music in the clip.
    # See: https://schema.org/musicBy
    musicBy: Union[str, Person, Organization]
    # The episode to which this clip belongs.
    # See: https://schema.org/partOfEpisode
    partOfEpisode: Episode
    # The season to which this clip belongs.
    # See: https://schema.org/partOfSeason
    partOfSeason: CreativeWorkSeason
    # The series to which this clip belongs.
    # See: https://schema.org/partOfSeries
    partOfSeries: CreativeWorkSeries
