from __future__ import annotations
from typing import Union, TYPE_CHECKING
from .creative_work import CreativeWork
if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person
    from .music_recording import MusicRecording


class MusicComposition(CreativeWork, total=False):
    """
    A class representing schema.org's MusicComposition.
    See: https://schema.org/MusicComposition
    """  # The person or organization who wrote a composition, or who is the composer of a work performed.
    composer: Union[Organization, Person]
    firstPerformance: str  # The date and place the work was first performed.
    # Smaller compositions included in this composition.
    includedComposition: MusicComposition
    # The International Standard Musical Work Code for the composition.
    iswcCode: str
    lyricist: Person  # The person who wrote the words.
    lyrics: str  # The words in the song.
    # An arrangement derived from the composition.
    musicArrangement: MusicComposition
    # The type of composition (e.g. sonata, symphony, etc.).
    musicCompositionForm: str
    musicalKey: str  # The key, e.g. F major, G minor, etc.
    recordedAs: MusicRecording  # The recording of this composition.
