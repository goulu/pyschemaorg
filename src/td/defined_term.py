from __future__ import annotations
from typing import TypedDict, Union, List
from .thing import Intangible, URL
from .creative_work import CreativeWork


class DefinedTerm(Intangible, TypedDict, total=False):
    """
    A class representing schema.org's DefinedTerm.
    A word, name, acronym, phrase, etc. with a formal definition.
    See: https://schema.org/DefinedTerm
    """
    termCode: str  # A code that identifies this DefinedTerm within a DefinedTermSet
    # A DefinedTermSet that contains this term.
    inDefinedTermSet: Union[URL, DefinedTermSet]


class DefinedTermSet(CreativeWork, TypedDict, total=False):
    """
    A class representing schema.org's DefinedTermSet.
    A set of defined terms for example a set of categories or a classification scheme, 
    a glossary, dictionary or enumeration.
    See: https://schema.org/DefinedTermSet
    """
    # A DefinedTerm contained in this set.
    hasDefinedTerm: Union[DefinedTerm, List[DefinedTerm]
                          ]
