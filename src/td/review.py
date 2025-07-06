from __future__ import annotations
from typing import Text, TypedDict, Union, List

from matplotlib.pylab import TYPE_CHECKING
from .creative_work import CreativeWork
if TYPE_CHECKING:
    from .web_content import WebContent
    from .item_list import ItemList
    from .list_item import ListItem
    from .thing import Thing
    from .rating import Rating
    from .aggregate_rating import AggregateRating


class Review(CreativeWork, TypedDict, total=False):
    """
    A class representing schema.org's Review.
    See: https://schema.org/Review
    """
    itemReviewed: Union[str, Thing]
    reviewBody: str
    reviewRating: Rating
    aggregateRating: AggregateRating
    positiveNotes: Union[ItemList, ListItem, Text, WebContent]
    negativeNotes: Union[str, CreativeWork, List[Union[str, CreativeWork]]]
    reviewAspect: str
