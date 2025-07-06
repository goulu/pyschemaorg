from __future__ import annotations
from typing import Union, List, TYPE_CHECKING
from .creative_work import CreativeWork
from .data_type import DateTime

if TYPE_CHECKING:
    from .person import Person
    from .episode import Episode
    from .creative_work_series import CreativeWorkSeries
    from .performing_group import PerformingGroup
    from .organization import Organization
    from .video_object import VideoObject


class CreativeWorkSeason(CreativeWork, total=False):
    """
    A class representing schema.org's CreativeWorkSeason.
    See: https://schema.org/CreativeWorkSeason
    """
    # An actor, e.g. in TV, radio, movie, video games, etc., or in an event.
    actor: Union[Person, List[Person]]
    # The director of the season.
    director: Union[Person, List[Person]]
    # The end date and time of the season.
    # See: https://schema.org/endDate
    endDate: DateTime
    # An episode of the season.
    # See: https://schema.org/episode
    episode: Union[Episode, List[Episode]]
    # The number of episodes in this season or series.
    # See: https://schema.org/numberOfEpisodes
    numberOfEpisodes: int
    # The series to which this season or episode belongs.
    # See: https://schema.org/partOfSeries
    partOfSeries: CreativeWorkSeries
    # A performer in the season.
    # See: https://schema.org/performer
    performer: Union[PerformingGroup, Person,
                     List[Union[PerformingGroup, Person]]]
    # The production company or studio responsible for the season.
    # See: https://schema.org/productionCompany
    productionCompany: Organization
    # Position of the season within an ordered group of seasons.
    # See: https://schema.org/seasonNumber
    seasonNumber: Union[int, str]
    # The start date and time of the season.
    # See: https://schema.org/startDate
    startDate: DateTime
    # The trailer for the season.
    # See: https://schema.org/trailer
    trailer: VideoObject
