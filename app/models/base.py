import uuid as puuid
from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

Base = declarative_base()


class BaseModel(Base):

    __abstract__ = True

    uuid: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        default=lambda: str(puuid.uuid4()),
        primary_key=True,
        index=True,
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(),
        nullable=False,
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(),
        onupdate=datetime.now(),
        nullable=False,
    )
