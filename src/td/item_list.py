from __future__ import annotations
from typing import TypedDict, Union
import enum

from .thing import Thing, Intangible
from .list_item import ListItem


class ItemListOrderType(enum.Enum):
    ItemListOrderAscending = "https://schema.org/ItemListOrderAscending"
    ItemListOrderDescending = "https://schema.org/ItemListOrderDescending"
    ItemListUnordered = "https://schema.org/ItemListUnordered"


class ItemList(Intangible, TypedDict, total=False):
    """
    A class representing schema.org's ItemList.
    See: https://schema.org/ItemList
    """
    itemListElement: Union[Thing, ListItem, str]
    numberOfItems: int
    itemListOrder: ItemListOrderType
    aggregateElement: Union[Thing, ListItem, str]
    # Inherits all fields from Intangible/Thing
