import enum


class MusicReleaseFormatType(enum.Enum):
    """
    Enum for MusicReleaseFormatType.
    See: https://schema.org/MusicReleaseFormatType
    """
    CassetteFormat = "CassetteFormat"
    CDFormat = "CDFormat"
    DATFormat = "DATFormat"
    DigitalAudioTapeFormat = "DigitalAudioTapeFormat"
    DigitalFormat = "DigitalFormat"
    DVDFormat = "DVDFormat"
    LaserDiscFormat = "LaserDiscFormat"
    VinylFormat = "VinylFormat"
