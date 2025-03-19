from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import db_session
from app.schemas import SimulatorResponseSchema, SimulatorSchema
from app.services import SimulatorService

router = APIRouter()


@router.post(
    "/simulation",
    tags=["Simulation"],
    response_model=SimulatorResponseSchema,
    status_code=status.HTTP_200_OK,
)
async def make_simulation(
    payload: SimulatorSchema, session: Session = Depends(db_session)
):
    try:
        service = SimulatorService(car_details=payload)
        response = await service.make_simulation(session=session)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        ) from e
