from enum import Enum
from .creative_work import CreativeWork


class MapCategoryType(Enum):
    """
    An enumeration of map categories as defined by schema.org.
    See: https://schema.org/MapCategoryType
    """
    PARKING_MAP = "https://schema.org/ParkingMap"
    SEATING_MAP = "https://schema.org/SeatingMap"
    TRANSIT_MAP = "https://schema.org/TransitMap"
    VENUE_MAP = "https://schema.org/VenueMap"


class Map(CreativeWork, total=False):
    """
    A class representing schema.org's Map.
    See: https://schema.org/Map
    """
    # Indicates the kind of Map, from MapCategoryType.
    mapType: MapCategoryType
