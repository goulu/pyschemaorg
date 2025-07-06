from typing import TYPE_CHECKING, TypedDict
from .thing import Intangible
from .data_type import URL

if TYPE_CHECKING:
    from .image_object import ImageObject
    from .review import Review
    from .aggregate_rating import AggregateRating
    from .organization import Organization
    from .product import Product


class Brand(Intangible, TypedDict, total=False):
    """
    A brand is a name used by an organization or business person for labeling a product, product group, or similar.
    See: https://schema.org/Brand
    """
    logo: ImageObject  # A logo associated with the brand.
    review: Review  # A review of the item.
    # The overall rating, based on a collection of reviews or ratings, of the item.
    aggregateRating: AggregateRating
    slogan: str  # A slogan or motto associated with the brand or item.
    url: URL  # URL of the item.
    name: str  # The name of the item.
    description: str  # A description of the item.
    owner: Organization  # The organization or person that owns the brand.
    product: Product  # A product produced by the brand or organization.
