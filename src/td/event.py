from __future__ import annotations
from typing import Union

from .data_type import Date, Time, DateTime, Duration, URL, Text

from .business import Offer

from .service import BroadcastService
from .thing import Thing
from .schedule import Schedule
from .place import Audience, Language, PostalAddress, Place, VirtualLocation
from .person import Person
from .organization import Organization
from .creative_work import CreativeWork, Review
from .rating import AggregateRating
from enum import Enum

type Location = Union[Place, PostalAddress, Text, VirtualLocation]

type PersOrg = Union[Person, Organization]


class EventStatusType(str, Enum):
    """
    EventStatusType is an enumeration type whose instances represent several states of an Event.
    See: https://schema.org/EventStatusType
    """
    EventCancelled = "EventCancelled"
    EventMovedOnline = "EventMovedOnline"
    EventPostponed = "EventPostponed"
    EventRescheduled = "EventRescheduled"
    EventScheduled = "EventScheduled"


class EventAttendanceModeEnumeration(str, Enum):
    """
    An enumeration type indicating the attendance mode of an event.
    See: https://schema.org/EventAttendanceModeEnumeration
    """
    MixedMode = "MixedMode"
    OfflineMode = "OfflineMode"
    OnlineMode = "OnlineMode"


class Event(Thing, total=False):
    """
    A class representing schema.org's Event.
    See: https://schema.org/Event
    """
    about: Thing
    """The subject matter of the content."""
    actor: Person
    """An actor, e.g. a person or organization, participating in the event."""
    aggregateRating: AggregateRating
    """The overall rating, based on a collection of reviews or ratings, of the item."""
    attendee: PersOrg
    """A person or organization attending the event."""
    audience: Audience
    """An intended audience, i.e. a group for whom something was created."""
    composer: PersOrg
    """The person or organization who wrote a composition, or who is the composer of a work performed at some event."""
    contributor: PersOrg
    """A secondary contributor to the CreativeWork or Event."""
    director: Person
    """A director of e.g. a movie, TV series, or radio program."""
    doorTime: Union[DateTime, Time]
    """The time admission will commence."""
    duration: Duration
    """The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format."""
    endDate: Union[Date, DateTime]
    """The end date and time of the item (in ISO 8601 date format)."""
    eventAttendanceMode: EventAttendanceModeEnumeration
    """The eventAttendanceMode of an event indicates whether it occurs online, offline, or a mix."""
    eventSchedule: Schedule
    """Associates an event with a series schedule."""
    eventStatus: EventStatusType
    """An eventStatus of an event represents its status; particularly useful when an event is cancelled or rescheduled."""
    funder: PersOrg
    """A person or organization that supports (sponsors) something through some kind of financial contribution."""
    inLanguage: Union[Language, Text]
    """The language of the content or performance or used in an action."""
    isAccessibleForFree: bool
    """A flag to signal that the item, event, or place is accessible for free."""
    keywords: Union[Text, URL]
    """Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas."""
    location: Location
    """The location of for example where the event is happening, an organization is located, or where an action takes place."""
    maximumAttendeeCapacity: int
    """The total number of individuals that may attend an event."""
    offers: Offer
    """An offer to provide this item—for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event."""
    organizer: PersOrg
    """An organizer of an Event."""
    performer: PersOrg
    """A performer at the event—for example, a presenter, musician, musical group or actor."""
    previousStartDate: Date
    """Used in conjunction with eventStatus for rescheduled or cancelled events."""
    recordedIn: CreativeWork
    """The CreativeWork that captured all or part of this Event."""
    remainingAttendeeCapacity: int
    """The number of attendee places for an event that are still available."""
    review: Review
    """A review of the item."""
    sponsor: PersOrg
    """A person or organization that supports a thing through a pledge, promise, or financial contribution."""
    startDate: Union[Date, DateTime]
    """The start date and time of the item (in ISO 8601 date format)."""
    subEvent: Event
    """An Event that is part of this Event."""
    superEvent: Event
    """An event that this event is a part of."""
    translator: PersOrg
    """Organization or person who adapts a creative work to different languages, regional differences and technical requirements of a target market, or that translates during real-time communication."""
    typicalAgeRange: Text
    """The typical expected age range, e.g. '7-9', '11-'."""
    workFeatured: CreativeWork
    """A work featured in some event, e.g. exhibited in an exhibition or shown in a festival."""
    workPerformed: CreativeWork
    """A work performed in some event, for example a play performed in a theatre."""


class PublicationEvent(Event, total=False):
    """
    A class representing schema.org's PublicationEvent.
    See: https://schema.org/PublicationEvent
    """
    publishedBy: Union[Organization, Person]
    publishedOn: BroadcastService
