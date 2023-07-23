from uuid import UUID

from fastapi import APIRouter, Depends, Header, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.crud import create_new_digest, get_latest_digest, get_user_by_id
from src.api.schemas import UserDigestResponse
from src.api.utils import filter_new_posts, get_user_subscription_posts
from src.core.database import get_async_session
from src.models.models import User


router = APIRouter()


@router.get("/get_digest", response_model=UserDigestResponse)
async def get_digest(
    user_id: UUID = Header(...),
    session: AsyncSession = Depends(get_async_session),
):
    """
    Retrieve information about latest user's digest.
    """
    user = await get_user_by_id(user_id, session)
    digest = await get_latest_digest(session=session, user_id=user.user_id)
    if not digest:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Digest not found",
        )

    return {"posts": [post.text for post in digest.posts]}


@router.post("/create_digest/")
async def create_digest(
    user_id: UUID,
    popularity: int = Query(None, ge=0, le=100),
    session: AsyncSession = Depends(get_async_session),
):
    user = await get_user_by_id(user_id, session)

    adding_posts = await get_user_subscription_posts(
        user.user_id,
        popularity,
        session,
    )

    if not adding_posts:
        return {"user_id": user_id, "message": "No posts for digest"}

    latest_digest = await get_latest_digest(user_id, session)

    if latest_digest:
        latest_digest_date = latest_digest.created_at
        previous_post_ids = {post.id for post in latest_digest.posts}
        adding_posts = filter_new_posts(
            adding_posts,
            previous_post_ids,
            latest_digest_date,
        )

        if not adding_posts:
            return {"user_id": user_id, "message": "No new posts for digest"}

    new_digest = await create_new_digest(user_id, adding_posts, session)

    return new_digest


@router.post("/users/")
async def create_user(
    user_name: str,
    session: AsyncSession = Depends(get_async_session),
):
    # Создаем нового пользователя и добавляем его в базу данных
    new_user = User(name=user_name)
    session.add(new_user)
    await session.commit()
    return new_user
