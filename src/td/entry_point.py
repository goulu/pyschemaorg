from __future__ import annotations
from typing import TYPE_CHECKING, Union

from .thing import Thing
from .data_type import Text, URL
if TYPE_CHECKING:
    from .software_application import SoftwareApplication


class EntryPoint(Thing, total=False):
    """
    A class representing schema.org's EntryPoint.
    An entry point, within some Web-based protocol.
    See: https://schema.org/EntryPoint
    """
    actionApplication: SoftwareApplication  # An application that can complete the request.
    # The high level platform(s) where the Action can be performed for the given URL.
    # To specify a specific application or operating system instance, use actionApplication.
    actionPlatform: Union[Text, URL]
    # The supported content type(s) for an EntryPoint response.
    contentType: Text
    # The supported encoding type(s) for an EntryPoint response.
    encodingType: Text
    # An HTTP method that specifies the appropriate HTTP method for a request to an HTTP EntryPoint.
    # Values are capitalized strings as used in HTTP.
    httpMethod: Text
    # An url template (RFC6570) that will be used to construct the target of the execution of the action.
    urlTemplate: Text
