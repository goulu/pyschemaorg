from __future__ import annotations
from typing import Union
from .rating import Rating
from .thing import Thing


class AggregateRating(Rating, total=False):
    """
    A class representing schema.org's AggregateRating.
    See: https://schema.org/AggregateRating
    """
    itemReviewed: Union[str, Thing]
    ratingCount: int
    reviewCount: int
