from __future__ import annotations
from typing import Union
from .thing import Intangible
from .quantitative_value import QuantitativeValue


class BroadcastFrequencySpecification(Intangible, total=False):
    """
    A class representing schema.org's BroadcastFrequencySpecification.
    See: https://schema.org/BroadcastFrequencySpecification
    """
    # The frequency in MHz for a particular broadcast.
    broadcastFrequencyValue: Union[str, QuantitativeValue]
    broadcastFrequencyType: str  # The type of frequency (e.g., AM, FM, DAB).
