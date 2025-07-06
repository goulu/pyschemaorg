from __future__ import annotations
from .creative_work import CreativeWork


class Comment(CreativeWork, total=False):
    """
    A class representing schema.org's Comment.
    See: https://schema.org/Comment
    """
    downvoteCount: int
    parentItem: CreativeWork
    upvoteCount: int
    sharedContent: CreativeWork
