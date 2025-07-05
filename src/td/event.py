from __future__ import annotations
from typing import Optional, Union

from .date_time import Date, Time, DateTime, Duration

from .business import Offer

from .service import BroadcastService
from .thing import URL, Thing, Text
from .schedule import Schedule
from .place import Audience, Language, PostalAddress, Place, VirtualLocation
from .person import Person
from .organization import Organization
from .creative_work import CreativeWork, Review
from .rating import AggregateRating

type Location = Union[Place, PostalAddress, Text, VirtualLocation]

type PersOrg = Union[Person, Organization]


class Event(Thing, total=False):
    """
    A class representing schema.org's Event.
    See: https://schema.org/Event
    """
    about: Optional[Thing]
    """The subject matter of the content."""
    actor: Optional[Person]
    """An actor, e.g. a person or organization, participating in the event."""
    aggregateRating: Optional[AggregateRating]
    """The overall rating, based on a collection of reviews or ratings, of the item."""
    attendee: Optional[PersOrg]
    """A person or organization attending the event."""
    audience: Optional[Audience]
    """An intended audience, i.e. a group for whom something was created."""
    composer: Optional[PersOrg]
    """The person or organization who wrote a composition, or who is the composer of a work performed at some event."""
    contributor: Optional[PersOrg]
    """A secondary contributor to the CreativeWork or Event."""
    director: Optional[Person]
    """A director of e.g. a movie, TV series, or radio program."""
    doorTime: Optional[Union[DateTime, Time]]
    """The time admission will commence."""
    duration: Optional['Duration']
    """The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format."""
    endDate: Optional[Union[Date, DateTime]]
    """The end date and time of the item (in ISO 8601 date format)."""
    eventAttendanceMode: Optional['EventAttendanceModeEnumeration']
    """The eventAttendanceMode of an event indicates whether it occurs online, offline, or a mix."""
    eventSchedule: Optional[Schedule]
    """Associates an event with a series schedule."""
    eventStatus: Optional['EventStatusType']
    """An eventStatus of an event represents its status; particularly useful when an event is cancelled or rescheduled."""
    funder: Optional[PersOrg]
    """A person or organization that supports (sponsors) something through some kind of financial contribution."""
    inLanguage: Optional[Union[Language, Text]]
    """The language of the content or performance or used in an action."""
    isAccessibleForFree: Optional[bool]
    """A flag to signal that the item, event, or place is accessible for free."""
    keywords: Optional[Union[Text, URL]]
    """Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas."""
    location: Optional[Location]
    """The location of for example where the event is happening, an organization is located, or where an action takes place."""
    maximumAttendeeCapacity: Optional[int]
    """The total number of individuals that may attend an event."""
    offers: Optional[Offer]
    """An offer to provide this item—for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event."""
    organizer: Optional[PersOrg]
    """An organizer of an Event."""
    performer: Optional[PersOrg]
    """A performer at the event—for example, a presenter, musician, musical group or actor."""
    previousStartDate: Optional['Date']
    """Used in conjunction with eventStatus for rescheduled or cancelled events."""
    recordedIn: Optional[CreativeWork]
    """The CreativeWork that captured all or part of this Event."""
    remainingAttendeeCapacity: Optional[int]
    """The number of attendee places for an event that are still available."""
    review: Optional[Review]
    """A review of the item."""
    sponsor: Optional[PersOrg]
    """A person or organization that supports a thing through a pledge, promise, or financial contribution."""
    startDate: Optional[Union['Date', 'DateTime']]
    """The start date and time of the item (in ISO 8601 date format)."""
    subEvent: Optional[Event]
    """An Event that is part of this Event."""
    superEvent: Optional[Event]
    """An event that this event is a part of."""
    translator: Optional[PersOrg]
    """Organization or person who adapts a creative work to different languages, regional differences and technical requirements of a target market, or that translates during real-time communication."""
    typicalAgeRange: Optional[Text]
    """The typical expected age range, e.g. '7-9', '11-'."""
    workFeatured: Optional[CreativeWork]
    """A work featured in some event, e.g. exhibited in an exhibition or shown in a festival."""
    workPerformed: Optional[CreativeWork]
    """A work performed in some event, for example a play performed in a theatre."""


class PublicationEvent(Event, total=False):
    """
    A class representing schema.org's PublicationEvent.
    See: https://schema.org/PublicationEvent
    """
    publishedBy: Optional[Union[Organization, Person]]
    publishedOn: Optional[BroadcastService]
