from __future__ import annotations
from typing import TYPE_CHECKING
from .thing import Intangible

if TYPE_CHECKING:
    from .creative_work import CreativeWork


class AlignmentObject(Intangible, total=False):
    """
    An intangible item that describes an alignment between a learning resource and a node in an educational framework.
    See: https://schema.org/AlignmentObject
    """
    # The framework to which the resource being described is aligned.
    alignmentFramework: str
    # The name of a node in an established educational framework.
    targetName: str
    # The description of a node in an established educational framework.
    targetDescription: str
    # The URL of a node in an established educational framework.
    targetUrl: str
    # The notation for a node in an established educational framework.
    targetCode: str
    # The CreativeWork that is aligned to this AlignmentObject.
    targetCreativeWork: CreativeWork
