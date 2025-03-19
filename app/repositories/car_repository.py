from sqlalchemy.orm import Session

from app.models import CarModel
from app.schemas import SimulatorSchema


class CarRepository:

    async def store(self, payload: SimulatorSchema, session: Session):
        response = CarModel(**payload.model_dump())
        session.add(response)
        session.commit()
        session.refresh(response)
        return response
