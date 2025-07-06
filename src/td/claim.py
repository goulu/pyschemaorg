from __future__ import annotations
from typing import Union
from .creative_work import CreativeWork
from .organization import Organization
from .person import Person


class Claim(CreativeWork, total=False):
    """
    A class representing schema.org's Claim.
    See: https://schema.org/Claim
    """
    appearance: CreativeWork
    claimInterpreter: Union[Organization, Person]
    firstAppearance: CreativeWork
