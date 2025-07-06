from __future__ import annotations
from typing import TypedDict, Union, TYPE_CHECKING

from .data_type import DateTime, Duration
from .thing import Thing

if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue
    from .person import Person
    from .organization import Organization
    from .country import Country
    from .aggregate_rating import AggregateRating
    from .audience import Audience
    from .comment import Comment
    from .place import Place
    from .rating import Rating
    from .language import Language
    from .defined_term import DefinedTerm
    from .claim import Claim
    from .review import Review
    from .offer import Offer
    from .demand import Demand
    from .product import Product
    from .publication_event import PublicationEvent
    from .interaction_counter import InteractionCounter
    from .media_object import MediaObject
    from .audio_object import AudioObject
    from .clip import Clip
    from .event import Event
    from .video_object import VideoObject


class CreativeWork(Thing, TypedDict, total=False):
    """
    A class representing schema.org's CreativeWork.
    The most generic kind of creative work, including books, movies, photographs, software programs, etc.
    See: https://schema.org/CreativeWork
    """
    about: Thing  # The subject matter of the content.
    # The human sensory perceptual system or cognitive faculty through which a person may process or
    # perceive information.
    accessMode: str
    # A list of single or combined accessModes that are sufficient to understand all the intellectual
    # content of a resource.
    accessModeSufficient: str
    # Indicates that the resource is compatible with the referenced accessibility API.
    accessibilityAPI: str
    # Identifies input methods that are sufficient to fully control the described resource.
    accessibilityControl: str
    # Content features of the resource, such as accessible media, alternatives and supported
    # enhancements for accessibility.
    accessibilityFeature: str
    # A characteristic of the described resource that is physiologically dangerous to some users.
    accessibilityHazard: str
    # A human-readable summary of specific accessibility features or deficiencies, consistent with the
    # other accessibility metadata but expressing subtleties such as "short descriptions are present but
    # long descriptions will be needed for non-visual users."
    accessibilitySummary: str
    # Specifies the Person that is legally accountable for the CreativeWork.
    accountablePerson: Person
    # The overall rating, based on a collection of reviews or ratings, of the item.
    aggregateRating: AggregateRating
    # A secondary title of the CreativeWork.
    alternativeHeadline: str
    # A media object that encodes this CreativeWork.
    associatedMedia: MediaObject
    # An intended audience, i.e. a group for whom something was created.
    audience: Audience
    # An audio object embedded in the CreativeWork.
    audio: Union[AudioObject, Clip]
    # The author of this CreativeWork.
    author: Union[Organization, Person]
    award: str  # An award won by or for this item.
    # Fictional person connected with a creative work.
    character: Person
    # A citation or reference to another creative work, such as another publication, web page,
    # scholarly article, etc.
    citation: Union[str, CreativeWork]
    comment: Comment  # Comments, typically from users.
    # The number of comments this CreativeWork (or part thereof) has received.
    commentCount: int
    # Conditions that affect the availability of, or method(s) of access to, an item.
    conditionsOfAccess: str
    # The location depicted or described in the content.
    contentLocation: Place
    # Official rating of a piece of content—for example, MPAA PG-13.
    contentRating: Union[str, Rating]
    # The specific time described by a creative work, for works (e.g. articles, video objects etc.)
    # that emphasise a particular moment within an Event.
    contentReferenceTime: Union[str, DateTime]
    # A secondary contributor to the CreativeWork or Event.
    contributor: Union[Organization, Person]
    # The party holding the legal copyright to the CreativeWork.
    copyrightHolder: Union[Organization, Person]
    # Text of a notice appropriate for display regarding recognized rights holder, ownership
    # dimensions.
    copyrightNotice: str
    # The year during which the CreativeWork was first copyrighted.
    copyrightYear: float
    # Indicates a correction to a CreativeWork. (URL is str)
    correction: Union[str, CreativeWork]
    # The country of origin of something, including products as well as creative works such as movies
    # and TV shows.
    countryOfOrigin: Country
    # The status of a creative work in terms of its completion life-cycle.
    creativeWorkStatus: str
    # The creator/author of this CreativeWork.
    creator: Union[Organization, Person]
    # The date on which the CreativeWork was created or the item was added to a DataFeed. (Date can be str)
    dateCreated: Union[str, DateTime]
    # The date on which the CreativeWork was most recently modified or when the items entry was
    # modified within a DataFeed. (Date can be str)
    dateModified: Union[str, DateTime]
    # Date of first broadcast/publication. (Date can be str)
    datePublished: Union[str, DateTime]
    # A link to the page containing the comments of the CreativeWork. (URL is str)
    discussionUrl: str
    # An EIDR (Entertainment Identifier Registry) identifier representing a specific edit / edition for
    # a work. (Text or URL)
    editEIDR: str
    # Specifies the Person who edited the CreativeWork.
    editor: Person
    # An alignment to an established educational framework.
    # educationalAlignment: AlignmentObject  # Uncomment and implement stub if needed
    # The level in terms of progression through an educational or training context. (Text, URL, or
    # DefinedTerm)
    educationalLevel: Union[str, DefinedTerm]
    # The purpose of a work in the context of education; for example, assignment, group work. (Text or
    # DefinedTerm)
    educationalUse: Union[str, DefinedTerm]
    # A media object that encodes this CreativeWork.
    encoding: MediaObject
    # Media type typically expressed using a MIME format (e.g. application/zip). (Text or URL)
    encodingFormat: str
    # A creative work that this work is an example of.
    exampleOfWork: CreativeWork
    # Date the content expires and is no longer useful or available. (Date or DateTime)
    expires: Union[str, DateTime]
    # Media type, typically MIME format (e.g. application/zip) of the content e.g. a SoftwareApplication
    # binary. (Text or URL)
    fileFormat: str
    # A person or organization that supports (sponsors) something through some kind of financial
    # contribution.
    funder: Union[Organization, Person]
    # Genre of the creative work, broadcast channel or group. (Text or URL)
    genre: str
    # Indicates a CreativeWork that is (in some sense) a part of this CreativeWork.
    hasPart: CreativeWork
    headline: str  # Headline of the article.
    # The language of the content or performance or used in an action. (Language or Text)
    inLanguage: Union[str, Language]
    # The number of interactions for the CreativeWork using the WebSite or SoftwareApplication.
    interactionStatistic: InteractionCounter
    # The predominant mode of learning supported by the learning resource.
    interactivityType: str
    # A claim represented by the CreativeWork.
    interpretedAsClaim: Claim
    # A flag to signal that the item, event, or place is accessible for free.
    isAccessibleForFree: bool
    # A resource that was used in the creation of this resource. (CreativeWork, Product, or URL)
    isBasedOn: Union[str, CreativeWork, Product]
    # Indicates whether this content is family friendly.
    isFamilyFriendly: bool
    # Indicates a CreativeWork that this CreativeWork is (in some sense) part of. (CreativeWork or URL)
    isPartOf: Union[str, CreativeWork]
    # Keywords or tags used to describe this content. (Text, URL or DefinedTerm)
    keywords: Union[str, DefinedTerm]
    # The predominant type or kind characterizing the learning resource. (Text or DefinedTerm)
    learningResourceType: Union[str, DefinedTerm]
    # A license document that applies to this content, typically indicated by URL. (CreativeWork or URL)
    license: Union[CreativeWork, str]
    # The location where the CreativeWork was created, which may not be the same as the location
    # depicted in the CreativeWork.
    locationCreated: Place
    # Indicates the primary entity described in some page or other CreativeWork.
    mainEntity: Thing
    # A maintainer of a Dataset, software package (SoftwareApplication), or other Project.
    maintainer: Union[Organization, Person]
    # A material that something is made from, e.g. leather, wool, cotton, paper. (Product, Text or URL)
    material: Union[str, Product]
    # The quantity of the materials being described or an expression of the physical space they occupy.
    # (QuantitativeValue or Text)
    materialExtent: Union[str, QuantitativeValue]
    # Indicates that the CreativeWork contains a reference to, but is not necessarily about a concept.
    mentions: Thing
    # An offer to provide this item—for example, an offer to sell a product, rent the DVD of a movie,
    # perform a service, or give away tickets to an event.
    offers: Union[Offer, Demand]
    # A pattern that something has, for example polka dot, striped, Canadian flag. (Text or DefinedTerm)
    pattern: Union[str, DefinedTerm]
    # The position of an item in a series or sequence of items.
    position: Union[str, int]
    # The person or organization who produced the work (e.g. music album, movie, tv/radio series etc.).
    producer: Union[Organization, Person]
    # The service provider, service operator, or service performer; the goods producer.
    provider: Union[Organization, Person]
    # A publication event associated with the item.
    publication: PublicationEvent
    # The publisher of the creative work.
    publisher: Union[Organization, Person]
    # The publishing division which published the comic.
    publisherImprint: Organization
    # The publishingPrinciples or editorial principles followed by this Organization or Person.
    # (CreativeWork or URL)
    publishingPrinciples: Union[str, CreativeWork]
    # The Event where the CreativeWork was recorded.
    recordedAt: Event
    # The place and time the release was issued, expressed as a PublicationEvent.
    releasedEvent: PublicationEvent
    review: Review  # A review of the item.
    # Indicates (by URL or string) a particular version of a schema used in some CreativeWork.
    # (Text or URL)
    schemaVersion: str
    # Indicates the date on which the current structured data was generated / published. (Date)
    sdDatePublished: str
    # A license document that applies to this structured data, typically indicated by URL.
    # (CreativeWork or URL)
    sdLicense: Union[CreativeWork, str]
    # Indicates the party responsible for generating and publishing the current structured data markup.
    sdPublisher: Union[Organization, Person]
    # A standardized size of a product or creative work. (QuantitativeValue or Text)
    size: Union[str, QuantitativeValue]
    # The Organization on whose behalf the creator was working.
    sourceOrganization: Organization
    # The "spatial" property can be used to describe the spatial place-names, regions, geometries or
    # latitude/longitude pairs related to a CreativeWork.
    spatial: Place
    # The spatialCoverage of a CreativeWork indicates the place(s) which are the focus of the content.
    spatialCoverage: Place
    # A person or organization that supports a thing through a pledge, promise, or financial
    # contribution.
    sponsor: Union[Organization, Person]
    # The item being described is intended to help a person learn the competency or learning outcome
    # defined by the referenced term. (Text or DefinedTerm)
    teaches: Union[str, DefinedTerm]
    # The "temporal" property can be used to describe the temporal window defining the scope of the
    # work. (DateTime or Text)
    temporal: Union[str, DateTime]
    # The temporalCoverage of a CreativeWork indicates the period that the content applies to.
    # (DateTime, Text or URL)
    temporalCoverage: Union[str, DateTime]
    text: str  # The textual content of this CreativeWork.
    # A thumbnail image relevant to the Thing. (URL)
    thumbnailUrl: str
    # Approximate or typical time it takes to work with or through this learning resource.
    # (Duration or Text)
    timeRequired: Duration
    # The work that this work has been translated from.
    translationOfWork: CreativeWork
    # Organization or person who adapts a creative work.
    translator: Union[Organization, Person]
    # The typical expected age range, e.g. 7-9, 11-.
    typicalAgeRange: str
    # The schema.org usageInfo property indicates further information about a CreativeWork.
    # (CreativeWork or URL)
    usageInfo: Union[CreativeWork, str]
    # The version of the CreativeWork embodied by a specified resource. (Number or Text)
    version: Union[str, float]
    video: Union[VideoObject, Clip]  # An embedded video object.
    # Example/instance/realization/derivation of the concept of this creative work.
    workExample: CreativeWork
    # A work that is a translation of the content of this work.
    workTranslation: CreativeWork
