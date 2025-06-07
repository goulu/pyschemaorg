from typing import List, Optional, Union

from .business import Offer

from .service import BroadcastService
from .thing import Thing
from .schedule import Schedule
from .place import Audience, PostalAddress, Place
from .person import Person
from .organization import Organization
from .creative_work import CreativeWork, Review
from .rating import AggregateRating


class Event(Thing, total=False):
    """
    A class representing .org's Event.
    See: https://.org/Event
    """
    about: Optional[Union[str, CreativeWork, List[Union[str, CreativeWork]]]]
    actor: Optional[Union[Person, List[Person]]]
    aggregateRating: Optional[AggregateRating]
    attendee: Optional[Union[Person, Organization,
                             List[Union[Person, Organization]]]]
    audience: Optional[Audience]
    composer: Optional[Union[Person, Organization]]
    contributor: Optional[Union[Person, Organization]]
    director: Optional[Union[Person, List[Person]]]
    doorTime: Optional[Union[str, Schedule]]
    duration: Optional[str]
    endDate: Optional[str]
    eventAttendanceMode: Optional[str]
    eventSchedule: Optional[Schedule]
    eventStatus: Optional[str]
    funder: Optional[Union[Person, Organization,
                           List[Union[Person, Organization]]]]
    inLanguage: Optional[Union[str, List[str]]]
    isAccessibleForFree: Optional[bool]
    location: Optional[Union[str, Place, PostalAddress,
                             List[Union[str, Place, PostalAddress]]]]
    maximumAttendeeCapacity: Optional[int]
    offers: Optional['Offer']
    organizer: Optional[Union[Person, Organization,
                              List[Union[Person, Organization]]]]
    performer: Optional[Union[Person, Organization,
                              List[Union[Person, Organization]]]]
    previousStartDate: Optional[str]
    recordedIn: Optional[CreativeWork]
    remainingAttendeeCapacity: Optional[int]
    review: Optional[Review]
    sponsor: Optional[Union[Person, Organization,
                            List[Union[Person, Organization]]]]
    startDate: Optional[str]
    subEvent: Optional['Event']
    subEvents: Optional[List['Event']]
    superEvent: Optional['Event']
    translator: Optional[Union[Person, Organization]]
    typicalAgeRange: Optional[str]
    workFeatured: Optional[CreativeWork]
    workPerformed: Optional[CreativeWork]


class PublicationEvent(Event, total=False):
    """
    A class representing .org's PublicationEvent.
    See: https://.org/PublicationEvent
    """
    publishedBy: Optional[Union[Organization, Person]]
    publishedOn: Optional['BroadcastService']
