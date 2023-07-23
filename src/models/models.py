from __future__ import annotations

import datetime
import uuid
from typing import List
from uuid import UUID

from sqlalchemy import Column, ForeignKey, Table, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship


Base = declarative_base()

digest_post = Table(
    "digest_post",
    Base.metadata,
    Column(
        "digest_id",
        ForeignKey("digest.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "post_id", ForeignKey("post.id", ondelete="CASCADE"), primary_key=True,
    ),
)


class User(Base):
    __tablename__ = "user"

    user_id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    subscriptions: Mapped[List[Subscription]] = relationship(
        back_populates="user",
    )
    digest: Mapped[List[Digest]] = relationship()


class Subscription(Base):
    __tablename__ = "subscription"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    source_name: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("user.user_id", ondelete="CASCADE"),
    )
    user: Mapped[User | None] = relationship(back_populates="subscriptions")
    posts: Mapped[List[Post]] = relationship()


class Post(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True)
    subscription_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            "subscription.id",
            ondelete="CASCADE",
        ),
    )
    subscription: Mapped[Subscription] = relationship(back_populates="posts")
    text: Mapped[str] = mapped_column(nullable=False)
    popularity: Mapped[int] = mapped_column()
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=func.now(), index=True,
    )
    digests: Mapped[List[Digest]] = relationship(
        "Digest", secondary=digest_post, back_populates="posts",
    )


class Digest(Base):
    __tablename__ = "digest"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("user.user_id", ondelete="CASCADE"),
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=func.now(), index=True,
    )
    posts: Mapped[List[Post]] = relationship(
        secondary=digest_post,
        back_populates="digests",
    )
