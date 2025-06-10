from __future__ import annotations
from typing import Optional, Union

from .enums import ItemListOrderType
from .thing import Thing, Intangible


class _Supersedable(Intangible, total=False):
    """
    base class for classes below. not in .org
    """
    supersededBy: Optional[Union[Enumeration, Class, Property]]


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
    domainIncludes: Optional[Class]
    rangeIncludes: Optional[Class]
    inverseOf: Optional[Property]


class ListItem(Intangible, total=False):
    """
    A class representing schema.org's ListItem.
    See: https://schema.org/ListItem
    """
    item: Optional[Thing]
    nextItem: Optional[ListItem]
    position: Optional[Union[int, str]]
    previousItem: Optional[ListItem]
    # Inherits all fields from Intangible/Thing


class ItemList(Intangible, total=False):
    """
    A class representing schema.org's ItemList.
    See: https://schema.org/ItemList
    """
    itemListElement: Optional[Union[Thing, ListItem, str]]
    numberOfItems: Optional[int]
    itemListOrder: Optional[ItemListOrderType]
    aggregateElement: Optional[Union[Thing, ListItem, str]]
    # Inherits all fields from Intangible/Thing
