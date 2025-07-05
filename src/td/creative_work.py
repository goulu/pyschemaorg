from __future__ import annotations
from typing import Union, List

from .date_time import DateTime, Duration
from .thing import URL, Thing
from .values import StructuredValue


class InteractionCounter(StructuredValue, total=False):
    """
    A class representing schema.org's InteractionCounter.
    A summary of how users have interacted with this CreativeWork.
    See: https://schema.org/InteractionCounter
    """

    # The WebSite or SoftwareApplication where the interactions took place.
    interactionService: Union[WebSite, SoftwareApplication]

    # The Action representing the type of interaction (e.g. LikeAction, WatchAction).
    interactionType: Action
    # The number of interactions for the CreativeWork using the specified service.
    userInteractionCount: int


# Placeholder for AlignmentObject, which is not defined in this snippet
AlignmentObject = Thing


class CreativeWork(Thing, total=False):
    """
    A class representing schema.org's CreativeWork.
    The most generic kind of creative work, including books, movies, photographs, software programs, etc.
    See: https://schema.org/CreativeWork
    """
    about: Thing  # The subject matter of the content.
    # The human sensory perceptual system or cognitive faculty through which a person may process or perceive information.
    accessMode: str
    # A list of single or combined accessModes that are sufficient to understand all the intellectual content of a resource.
    accessModeSufficient: str
    # Indicates that the resource is compatible with the referenced accessibility API.
    accessibilityAPI: str
    # Identifies input methods that are sufficient to fully control the described resource.
    accessibilityControl: str
    # Content features of the resource, such as accessible media, alternatives and supported enhancements for accessibility.
    accessibilityFeature: str
    # A characteristic of the described resource that is physiologically dangerous to some users.
    accessibilityHazard: str
    # A human-readable summary of specific accessibility features or deficiencies, consistent with the other accessibility metadata but expressing subtleties such as "short descriptions are present but long descriptions will be needed for non-visual users."
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
    # A citation or reference to another creative work, such as another publication, web page, scholarly article, etc.
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
    # The specific time described by a creative work, for works (e.g. articles, video objects etc.) that emphasise a particular moment within an Event.
    contentReferenceTime: Union[str, DateTime]
    # A secondary contributor to the CreativeWork or Event.
    contributor: Union[Organization, Person]
    # The party holding the legal copyright to the CreativeWork.
    copyrightHolder: Union[Organization, Person]
    # Text of a notice appropriate for display regarding recognized rights holder, ownership dimensions.
    copyrightNotice: str
    # The year during which the CreativeWork was first copyrighted.
    copyrightYear: float
    # Indicates a correction to a CreativeWork. (URL is str)
    correction: Union[str, CreativeWork]
    # The country of origin of something, including products as well as creative works such as movies and TV shows.
    countryOfOrigin: Country
    # The status of a creative work in terms of its completion life-cycle.
    creativeWorkStatus: str
    # The creator/author of this CreativeWork.
    creator: Union[Organization, Person]
    # The date on which the CreativeWork was created or the item was added to a DataFeed. (Date can be str)
    dateCreated: Union[str, DateTime]
    # The date on which the CreativeWork was most recently modified or when the items entry was modified within a DataFeed. (Date can be str)
    dateModified: Union[str, DateTime]
    # Date of first broadcast/publication. (Date can be str)
    datePublished: Union[str, DateTime]
    # A link to the page containing the comments of the CreativeWork. (URL is str)
    discussionUrl: str
    # An EIDR (Entertainment Identifier Registry) identifier representing a specific edit / edition for a work. (Text or URL)
    editEIDR: str
    # Specifies the Person who edited the CreativeWork.
    editor: Person
    # An alignment to an established educational framework.
    educationalAlignment: AlignmentObject
    # The level in terms of progression through an educational or training context. (Text, URL, or DefinedTerm)
    educationalLevel: Union[str, DefinedTerm]
    # The purpose of a work in the context of education; for example, assignment, group work. (Text or DefinedTerm)
    educationalUse: Union[str, DefinedTerm]
    # A media object that encodes this CreativeWork.
    encoding: MediaObject
    # Media type typically expressed using a MIME format (e.g. application/zip). (Text or URL)
    encodingFormat: str
    # A creative work that this work is an example of.
    exampleOfWork: CreativeWork
    # Date the content expires and is no longer useful or available. (Date or DateTime)
    expires: Union[str, DateTime]
    # Media type, typically MIME format (e.g. application/zip) of the content e.g. a SoftwareApplication binary. (Text or URL)
    fileFormat: str
    # A person or organization that supports (sponsors) something through some kind of financial contribution.
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
    # The location where the CreativeWork was created, which may not be the same as the location depicted in the CreativeWork.
    locationCreated: Place
    # Indicates the primary entity described in some page or other CreativeWork.
    mainEntity: Thing
    # A maintainer of a Dataset, software package (SoftwareApplication), or other Project.
    maintainer: Union[Organization, Person]
    # A material that something is made from, e.g. leather, wool, cotton, paper. (Product, Text or URL)
    material: Union[str, Product]
    # The quantity of the materials being described or an expression of the physical space they occupy. (QuantitativeValue or Text)
    materialExtent: Union[str, QuantitativeValue]
    # Indicates that the CreativeWork contains a reference to, but is not necessarily about a concept.
    mentions: Thing
    # An offer to provide this item—for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event.
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
    # The publishingPrinciples or editorial principles followed by this Organization or Person. (CreativeWork or URL)
    publishingPrinciples: Union[str, CreativeWork]
    # The Event where the CreativeWork was recorded.
    recordedAt: Event
    # The place and time the release was issued, expressed as a PublicationEvent.
    releasedEvent: PublicationEvent
    review: Review  # A review of the item.
    # Indicates (by URL or string) a particular version of a schema used in some CreativeWork. (Text or URL)
    schemaVersion: str
    # Indicates the date on which the current structured data was generated / published. (Date)
    sdDatePublished: str
    # A license document that applies to this structured data, typically indicated by URL. (CreativeWork or URL)
    sdLicense: Union[CreativeWork, str]
    # Indicates the party responsible for generating and publishing the current structured data markup.
    sdPublisher: Union[Organization, Person]
    # A standardized size of a product or creative work. (QuantitativeValue or Text)
    size: Union[str, QuantitativeValue]
    # The Organization on whose behalf the creator was working.
    sourceOrganization: Organization
    # The "spatial" property can be used to describe the spatial place-names, regions, geometries or latitude/longitude pairs related to a CreativeWork.
    spatial: Place
    # The spatialCoverage of a CreativeWork indicates the place(s) which are the focus of the content.
    spatialCoverage: Place
    # A person or organization that supports a thing through a pledge, promise, or financial contribution.
    sponsor: Union[Organization, Person]
    # The item being described is intended to help a person learn the competency or learning outcome defined by the referenced term. (Text or DefinedTerm)
    teaches: Union[str, DefinedTerm]
    # The "temporal" property can be used to describe the temporal window defining the scope of the work. (DateTime or Text)
    temporal: Union[str, DateTime]
    # The temporalCoverage of a CreativeWork indicates the period that the content applies to. (DateTime, Text or URL)
    temporalCoverage: Union[str, DateTime]
    text: str  # The textual content of this CreativeWork.
    # A thumbnail image relevant to the Thing. (URL)
    thumbnailUrl: str
    # Approximate or typical time it takes to work with or through this learning resource. (Duration or Text)
    timeRequired: Duration
    # The work that this work has been translated from.
    translationOfWork: CreativeWork
    # Organization or person who adapts a creative work.
    translator: Union[Organization, Person]
    # The typical expected age range, e.g. 7-9, 11-.
    typicalAgeRange: str
    # The schema.org usageInfo property indicates further information about a CreativeWork. (CreativeWork or URL)
    usageInfo: Union[CreativeWork, str]
    # The version of the CreativeWork embodied by a specified resource. (Number or Text)
    version: Union[str, float]
    video: Union[VideoObject, Clip]  # An embedded video object.
    # Example/instance/realization/derivation of the concept of this creative work.
    workExample: CreativeWork
    # A work that is a translation of the content of this work.
    workTranslation: CreativeWork


class Claim(CreativeWork, total=False):
    """
    A class representing schema.org's Claim.
    A Claim is a statement made by a person or organization that expresses a belief or assertion. It is a subtype of CreativeWork.
    See: https://schema.org/Claim
    """
    appearance: CreativeWork  # An appearance in textual content of the claim, indicating the relevant sections of a document, blog post, or other CreativeWork.
    # For a Claim interpreted from MediaObject, the specific region of the MediaObject that is interpreted. Supersedes embeddedTextAnnotation.
    # As per https://.org/claimInterpreter, the type is Organization or Person.
    claimInterpreter: Union[Organization, Person]
    # Indicates the first known occurrence of a Claim in some CreativeWork.
    firstAppearance: CreativeWork


class CreativeWorkSeries(CreativeWork, total=False):
    """
    A class representing schema.org's CreativeWorkSeries.
    See: https://schema.org/CreativeWorkSeries
    """
    endDate: Union[str, DateTime]
    issn: str
    startDate: Union[str, DateTime]


class CreativeWorkSeason(CreativeWork, total=False):
    """
    A class representing schema.org's CreativeWorkSeason.
    See: https://schema.org/CreativeWorkSeason
    """
    actor: Union[Person, List[Person]]
    director: Union[Person, List[Person]]
    endDate: Union[str, DateTime]
    episode: Union[Episode, List[Episode]]
    numberOfEpisodes: int
    partOfSeries: CreativeWorkSeries
    performer: Union[PerformingGroup,
                     Person, List[Union[PerformingGroup, Person]]]
    productionCompany: Organization
    seasonNumber: Union[int, str]
    startDate: Union[str, DateTime]
    trailer: VideoObject


class Episode(CreativeWork, total=False):
    """
    A class representing schema.org's Episode.
    See: https://schema.org/Episode
    """
    actor: Union[Person, List[Person]]
    director: Union[Person, List[Person]]
    episodeNumber: Union[int, str]
    musicBy: Union[Person, Organization]
    partOfSeason: CreativeWorkSeason
    partOfSeries: CreativeWorkSeries
    productionCompany: Organization
    subtitleLanguage: Union[str, List[str]]
    titleEIDR: str
    trailer: VideoObject


class Review(CreativeWork, total=False):
    """
    A class representing schema.org's Review.
    See: https://schema.org/Review
    """
    # The item that is being reviewed
    itemReviewed: Union[str, Thing]
    # The actual body of the review
    reviewBody: str
    # The rating given in this review
    reviewRating: Rating
    # The author of the review (inherited from CreativeWork, but often used)
    # The publisher of the review (inherited from CreativeWork)
    # The date the review was published (inherited from CreativeWork)
    # The aggregate rating for the item being reviewed
    aggregateRating: AggregateRating
    # The item that this review is a response to
    positiveNotes: Union[str, CreativeWork,
                         List[Union[str, CreativeWork]]]
    negativeNotes: Union[str, CreativeWork,
                         List[Union[str, CreativeWork]]]
    # The review this is a reply to
    reviewAspect: str


class Comment(CreativeWork, total=False):
    """
    A class representing schema.org's Comment.
    See: https://schema.org/Comment
    """
    downvoteCount: int
    parentItem: CreativeWork
    upvoteCount: int
    sharedContent: CreativeWork
    # Inherits all fields from CreativeWork (including author, dateCreated, text, etc.)


class WebSite(CreativeWork, total=False):
    """
    A class representing schema.org's WebSite.
    See: https://schema.org/WebSite
    """
    issn: str


# Placeholder for DataFeed if not defined elsewhere
DataFeed = Thing  # Or a more specific class if available


class SoftwareApplication(CreativeWork, total=False):
    """
    A class representing schema.org's SoftwareApplication.
    A software application.
    See: https://schema.org/SoftwareApplication
    """
    applicationCategory: Union[str, URL]
    # Type of software application, e.g. Game, Multimedia.
    applicationSubCategory: Union[str, URL]
    # The name of the application suite to which the application belongs (e.g. Excel belongs to Office).
    applicationSuite: str
    # Device required to run the application (e.g. Apple iPhone 5).
    availableOnDevice: str
    # Countries for which the application is not supported.
    countriesNotSupported: str
    # Countries for which the application is supported.
    countriesSupported: str
    # If the file can be downloaded, URL to download the binary.
    downloadUrl: URL
    # Features or modules provided by this application (and possibly required by other applications).
    featureList: Union[str, URL]
    # Size of the application / package (e.g. 18MB). In the absence of a unit (MB, KB etc.), KB will be assumed.
    fileSize: str
    # URL at which the app may be installed, if different from the URL of the item.
    installUrl: URL
    # Minimum memory requirements.
    memoryRequirements: Union[str, URL]
    # Operating systems supported (Windows 7, OSX 10.6, Android 1.6).
    operatingSystem: str
    # Permission(s) required to run the app (for example, a mobile app may require full internet access or may run in a sandboxed environment).
    permissions: str
    # Processor architecture required to run the application (e.g. IA64).
    processorRequirements: str
    # Description of what is new in this catalog entry compared to the previous version of the software.
    releaseNotes: Union[str, URL]
    # A link to a screenshot image of the app.
    screenshot: Union[ImageObject, URL]
    # Additional content offered by the application.
    softwareAddOn: SoftwareApplication
    softwareHelp: CreativeWork  # Software application help.
    # Component dependency requirements for application. This includes runtime environments and shared libraries that are not part of the application distribution itself, but should be installed separately.
    softwareRequirements: Union[str, URL]
    softwareVersion: str  # Version of the software instance.
    # Storage requirements (e.g. 1MB).
    storageRequirements: Union[str, URL]
    # Supporting data for a SoftwareApplication.
    supportingData: DataFeed
    # Inherits all fields from CreativeWork
