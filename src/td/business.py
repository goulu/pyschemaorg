from __future__ import annotations
import enum


class BusinessFunction(enum.Enum):
    ConstructionInstallation = "https://schema.org/ConstructionInstallation"
    Dispose = "https://schema.org/Dispose"
    LeaseOut = "https://schema.org/LeaseOut"
    Maintain = "https://schema.org/Maintain"
    ProvideService = "https://schema.org/ProvideService"
    Repair = "https://schema.org/Repair"
    Sell = "https://schema.org/Sell"


class OfferItemCondition(enum.Enum):
    DamagedCondition = 1
    NewCondition = 2
    RefurbishedCondition = 3
    UsedCondition = 4
