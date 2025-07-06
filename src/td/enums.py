from __future__ import annotations
import enum


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
