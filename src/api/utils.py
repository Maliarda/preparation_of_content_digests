from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.models import Post, Subscription


async def get_user_subscription_posts(
    user_id: UUID,
    popularity: int,
    session: AsyncSession,
):
    query = (
        select(Post).join(Subscription).where(Subscription.user_id == user_id)
    )

    if popularity is not None:
        query = query.filter(Post.popularity > popularity)

    user_subscription_ids = await session.execute(query)
    return [post[0] for post in user_subscription_ids]


def filter_new_posts(adding_posts, previous_post_ids, latest_digest_date):
    return [
        post
        for post in adding_posts
        if post.id not in previous_post_ids
        and post.created_at > latest_digest_date
    ]
