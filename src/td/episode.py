from __future__ import annotations
from typing import Union, List, TYPE_CHECKING
from .creative_work import CreativeWork
if TYPE_CHECKING:
    from .person import Person
    from .organization import Organization
    from .creative_work_season import CreativeWorkSeason
    from .creative_work_series import CreativeWorkSeries
    from .video_object import VideoObject


class Episode(CreativeWork, total=False):
    """
    A class representing schema.org's Episode.
    See: https://schema.org/Episode
    """
    actor: Union[Person, List[Person]
                 # An actor, e.g. in TV, radio, movie, video games, etc., or in an event.
                 ]
    # A director of e.g. TV, radio, movie, video games, or events.
    director: Union[Person, List[Person]]
    # Position of the episode within an ordered group of episodes.
    episodeNumber: Union[int, str]
    musicBy: Union[Person, Organization]  # The composer of the soundtrack.
    # The season to which this episode belongs.
    partOfSeason: CreativeWorkSeason
    # The series to which this episode belongs.
    partOfSeries: CreativeWorkSeries
    # The production company or studio responsible for the item.
    productionCompany: Organization
    # Languages in which subtitles/captions are available.
    subtitleLanguage: Union[str, List[str]]
    # The titleEIDR is an identifier for TV, radio and internet episodes.
    titleEIDR: str
    # The trailer of a movie or TV/radio series, season, episode, etc.
    trailer: VideoObject
