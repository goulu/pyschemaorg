from typing import Optional, Union
from .thing import Thing
from .person import Person
from .organization import Organization


class Rating(Thing, total=False):
    """
    A class representing .org's Rating.
    See: https://.org/Rating
    """
    author: Optional[Union[str, Person, Organization]]
    bestRating: Optional[Union[str, float, int]]
    ratingExplanation: Optional[str]
    ratingValue: Optional[Union[str, float, int]]
    reviewAspect: Optional[str]
    worstRating: Optional[Union[str, float, int]]


class AggregateRating(Rating, total=False):
    """
    A class representing .org's AggregateRating.
    See: https://.org/AggregateRating
    """
    itemReviewed: Optional[Union[str, Thing]]
    ratingCount: Optional[int]
    reviewCount: Optional[int]
    # Inherits all fields from Rating (author, bestRating, ratingExplanation, ratingValue, reviewAspect, worstRating)
