from __future__ import annotations
from typing import Union
from .thing import Thing

from .data_type import Text, DateTime


class DataFeedItem(Thing, total=False):
    """
    A class representing schema.org's DataFeedItem.
    See: https://schema.org/DataFeedItem
    """
    # The date on which the CreativeWork was created or the item was added to the DataFeed.
    dateCreated: DateTime
    # The datetime the item was deleted from the DataFeed.
    dateDeleted: DateTime
    # The datetime the item was modified in the DataFeed.
    dateModified: DateTime
    # An entity represented by an entry in a list or data feed (e.g. an 'artist' in a list of 'artists').
    item: Thing


class DataFeed(Thing, total=False):
    """
    A class representing schema.org's DataFeed.
    See: https://schema.org/DataFeed
    """
    # An item within a data feed. Can be a DataFeedItem or CreativeWork.
    dataFeedElement: Union[DataFeedItem, Thing, Text]
