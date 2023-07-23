from typing import Optional
from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.sql import Select

from src.models.models import Digest, User


def get_user_query(user_id: UUID) -> Select:
    return select(User).where(User.user_id == user_id)


async def get_user_by_uuid(
    user_id: UUID,
    session: AsyncSession,
) -> Optional[User]:
    db_obj = await session.execute(get_user_query(user_id))
    return db_obj.scalars().first()


def get_digest_query(user_id: UUID) -> Select:
    return select(Digest).where(Digest.user_id == user_id)


async def get_user_by_id(user_id: UUID, session: AsyncSession):
    user = await get_user_by_uuid(user_id, session)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def get_latest_digest(user_id: UUID, session: AsyncSession):
    latest_digest = (
        (
            await session.execute(
                select(Digest)
                .filter(Digest.user_id == user_id)
                .order_by(Digest.id.desc())
                .limit(1)
                .options(selectinload(Digest.posts)),
            )
        )
        .scalars()
        .first()
    )
    return latest_digest


async def create_new_digest(
    user_id: UUID,
    adding_posts,
    session: AsyncSession,
):
    new_digest = Digest(user_id=user_id)
    for post in adding_posts:
        new_digest.posts.append(post)

    session.add(new_digest)
    await session.commit()

    return new_digest
