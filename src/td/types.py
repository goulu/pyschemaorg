from __future__ import annotations
from typing import Union

from .enums import ItemListOrderType
from .thing import Thing, Intangible


class _Supersedable(Intangible, total=False):
    """
    base class for classes below. not in .org
    """
    supersededBy: Union[Enumeration, Class, Property]


class Enumeration(_Supersedable, total=False):
    """
    Derived from https://.org/Enumeration
    """
    pass


class Class(_Supersedable, total=False):
    """
    Derived from https://.org/Class
    """
    pass


class Property(_Supersedable, total=False):
    """
    Derived from https://.org/Property
    """
    domainIncludes: Class
    rangeIncludes: Class
    inverseOf: Property


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


class ItemList(Intangible, total=False):
    """
    A class representing schema.org's ItemList.
    See: https://schema.org/ItemList
    """
    itemListElement: Union[Thing, ListItem, str]
    numberOfItems: int
    itemListOrder: ItemListOrderType
    aggregateElement: Union[Thing, ListItem, str]
    # Inherits all fields from Intangible/Thing
