from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models import BaseModel


class CarModel(BaseModel):

    __tablename__ = "cars"

    brand: Mapped[str] = mapped_column(
        String(60),
        nullable=False,
    )
    model: Mapped[str] = mapped_column(
        String(60),
        nullable=False,
    )
    year: Mapped[int] = mapped_column(
        Integer(),
        nullable=False,
    )
    price: Mapped[float] = mapped_column(
        Float(precision=2),
        nullable=False,
    )
    percentage: Mapped[float] = mapped_column(
        Float(precision=2),
        nullable=False,
    )
    broker_fee: Mapped[float] = mapped_column(
        Float(precision=2),
        nullable=False,
    )
