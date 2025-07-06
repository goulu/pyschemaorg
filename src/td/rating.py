from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict, Union
from .thing import Thing

if TYPE_CHECKING:
    from .person import Person
    from .organization import Organization


class Rating(Thing, TypedDict, total=False):
    """
    A class representing schema.org's Rating.
    See: https://schema.org/Rating
    """

    author: Union[str, Person, Organization]
    bestRating: Union[str, float, int]
    ratingExplanation: str
    ratingValue: Union[str, float, int]
    reviewAspect: str
    worstRating: Union[str, float, int]
