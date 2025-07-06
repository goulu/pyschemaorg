from __future__ import annotations
from typing import Union
from .thing import Thing, Intangible


class ListItem(Intangible, total=False):
    """
    A class representing schema.org's ListItem.
    See: https://schema.org/ListItem
    """
    item: Thing
    nextItem: ListItem
    position: Union[int, str]
    previousItem: ListItem
    # Inherits all fields from Intangible/Thing
