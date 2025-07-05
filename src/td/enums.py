from __future__ import annotations
import enum


class OfferItemCondition(enum.Enum):
    DamagedCondition = 1,
    NewCondition = 2,
    RefurbishedCondition = 3,
    UsedCondition = 4


class EUEnergyEfficiencyEnumeration(enum.Enum):
    EUEnergyEfficiencyCategoryA = "https://schema.org/EUEnergyEfficiencyCategoryA"
    EUEnergyEfficiencyCategoryA1Plus = "https://schema.org/EUEnergyEfficiencyCategoryA1Plus"
    EUEnergyEfficiencyCategoryA2Plus = "https://schema.org/EUEnergyEfficiencyCategoryA2Plus"
    EUEnergyEfficiencyCategoryA3Plus = "https://schema.org/EUEnergyEfficiencyCategoryA3Plus"
    EUEnergyEfficiencyCategoryB = "https://schema.org/EUEnergyEfficiencyCategoryB"
    EUEnergyEfficiencyCategoryC = "https://schema.org/EUEnergyEfficiencyCategoryC"
    EUEnergyEfficiencyCategoryD = "https://schema.org/EUEnergyEfficiencyCategoryD"
    EUEnergyEfficiencyCategoryE = "https://schema.org/EUEnergyEfficiencyCategoryE"
    EUEnergyEfficiencyCategoryF = "https://schema.org/EUEnergyEfficiencyCategoryF"
    EUEnergyEfficiencyCategoryG = "https://schema.org/EUEnergyEfficiencyCategoryG"


EnergyConsumptionDetails = EUEnergyEfficiencyEnumeration


class BusinessFunction(enum.Enum):
    ConstructionInstallation = "https://schema.org/ConstructionInstallation"
    Dispose = "https://schema.org/Dispose"
    LeaseOut = "https://schema.org/LeaseOut"
    Maintain = "https://schema.org/Maintain"
    ProvideService = "https://schema.org/ProvideService"
    Repair = "https://schema.org/Repair"
    Sell = "https://schema.org/Sell"


class WarrantyScope(enum.Enum):
    LaborBringingIn = "https://schema.org/LaborBringingIn"
    LaborPickupDropOff = "https://schema.org/LaborPickupDropOff"
    LaborRepair = "https://schema.org/LaborRepair"
    PartsAndLaborBringingIn = "https://schema.org/PartsAndLaborBringingIn"
    PartsAndLaborPickupDropOff = "https://schema.org/PartsAndLaborPickupDropOff"
    PartsAndLaborRepair = "https://schema.org/PartsAndLaborRepair"
    PartsBringingIn = "https://schema.org/PartsBringingIn"
    PartsPickupDropOff = "https://schema.org/PartsPickupDropOff"
    PartsRepair = "https://schema.org/PartsRepair"


class ItemListOrderType(enum.Enum):
    ItemListOrderAscending = "https://schema.org/ItemListOrderAscending"
    ItemListOrderDescending = "https://schema.org/ItemListOrderDescending"
    ItemListUnordered = "https://schema.org/ItemListUnordered"


class DayOfWeek(enum.Enum):
    # https://.org/DayOfWeek
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7
    PublicHolidays = 8
