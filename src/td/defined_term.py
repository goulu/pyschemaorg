from typing import Optional, Union, List
from .thing import Intangible, URL
from .creative_work import CreativeWork


class DefinedTerm(Intangible, total=False):
    """
    A class representing .org's DefinedTerm.
    A word, name, acronym, phrase, etc. with a formal definition.
    See: https://.org/DefinedTerm
    """
    termCode: Optional[str]  # A code that identifies this DefinedTerm within a DefinedTermSet
    # A DefinedTermSet that contains this term.
    inDefinedTermSet: Optional[Union[URL, 'DefinedTermSet']]


class DefinedTermSet(CreativeWork, total=False):
    """
    A class representing .org's DefinedTermSet.
    A set of defined terms for example a set of categories or a classification scheme, a glossary, dictionary or enumeration.
    See: https://.org/DefinedTermSet
    """
    hasDefinedTerm: Optional[Union[DefinedTerm, List[DefinedTerm]]
                             ]  # A DefinedTerm contained in this set.