from __future__ import annotations
from typing import Union
from .data_type import URL
from .creative_work import CreativeWork
from .data_feed import DataFeed
from .image_object import ImageObject


class SoftwareApplication(CreativeWork, total=False):
    """
    A class representing schema.org's SoftwareApplication.
    See: https://schema.org/SoftwareApplication
    """
    applicationCategory: Union[str, URL]
    applicationSubCategory: Union[str, URL]
    applicationSuite: str
    availableOnDevice: str
    countriesNotSupported: str
    countriesSupported: str
    downloadUrl: URL
    featureList: Union[str, URL]
    fileSize: str
    installUrl: URL
    memoryRequirements: Union[str, URL]
    operatingSystem: str
    permissions: str
    processorRequirements: str
    releaseNotes: Union[str, URL]
    screenshot: Union[ImageObject, URL]
    softwareAddOn: 'SoftwareApplication'
    softwareHelp: CreativeWork
    softwareRequirements: Union[str, URL]
    softwareVersion: str
    storageRequirements: Union[str, URL]
    supportingData: DataFeed
