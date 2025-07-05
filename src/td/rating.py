from __future__ import annotations
from typing import Union
from .thing import Thing
from .person import Person
from .organization import Organization


class Rating(Thing, total=False):
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


class AggregateRating(Rating, total=False):
    """
    A class representing schema.org's AggregateRating.
    See: https://schema.org/AggregateRating
    """
    itemReviewed: Union[str, Thing]
    ratingCount: int
    reviewCount: int
    # Inherits all fields from Rating (author, bestRating, ratingExplanation, ratingValue, reviewAspect, worstRating)
