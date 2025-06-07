import enum


class OfferItemCondition(enum.Enum):
    DamagedCondition = 1,
    NewCondition = 2,
    RefurbishedCondition = 3,
    UsedCondition = 4


class EUEnergyEfficiencyEnumeration(enum.Enum):
    EUEnergyEfficiencyCategoryA = "https://.org/EUEnergyEfficiencyCategoryA"
    EUEnergyEfficiencyCategoryA1Plus = "https://.org/EUEnergyEfficiencyCategoryA1Plus"
    EUEnergyEfficiencyCategoryA2Plus = "https://.org/EUEnergyEfficiencyCategoryA2Plus"
    EUEnergyEfficiencyCategoryA3Plus = "https://.org/EUEnergyEfficiencyCategoryA3Plus"
    EUEnergyEfficiencyCategoryB = "https://.org/EUEnergyEfficiencyCategoryB"
    EUEnergyEfficiencyCategoryC = "https://.org/EUEnergyEfficiencyCategoryC"
    EUEnergyEfficiencyCategoryD = "https://.org/EUEnergyEfficiencyCategoryD"
    EUEnergyEfficiencyCategoryE = "https://.org/EUEnergyEfficiencyCategoryE"
    EUEnergyEfficiencyCategoryF = "https://.org/EUEnergyEfficiencyCategoryF"
    EUEnergyEfficiencyCategoryG = "https://.org/EUEnergyEfficiencyCategoryG"


EnergyConsumptionDetails = EUEnergyEfficiencyEnumeration


class BusinessFunction(enum.Enum):
    ConstructionInstallation = "https://.org/ConstructionInstallation"
    Dispose = "https://.org/Dispose"
    LeaseOut = "https://.org/LeaseOut"
    Maintain = "https://.org/Maintain"
    ProvideService = "https://.org/ProvideService"
    Repair = "https://.org/Repair"
    Sell = "https://.org/Sell"


class WarrantyScope(enum.Enum):
    LaborBringingIn = "https://.org/LaborBringingIn"
    LaborPickupDropOff = "https://.org/LaborPickupDropOff"
    LaborRepair = "https://.org/LaborRepair"
    PartsAndLaborBringingIn = "https://.org/PartsAndLaborBringingIn"
    PartsAndLaborPickupDropOff = "https://.org/PartsAndLaborPickupDropOff"
    PartsAndLaborRepair = "https://.org/PartsAndLaborRepair"
    PartsBringingIn = "https://.org/PartsBringingIn"
    PartsPickupDropOff = "https://.org/PartsPickupDropOff"
    PartsRepair = "https://.org/PartsRepair"


class ItemListOrderType(enum.Enum):
    ItemListOrderAscending = "https://.org/ItemListOrderAscending"
    ItemListOrderDescending = "https://.org/ItemListOrderDescending"
    ItemListUnordered = "https://.org/ItemListUnordered"


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
