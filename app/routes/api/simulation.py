from fastapi import APIRouter, HTTPException, status

from app.schemas import SimulatorResponseSchema, SimulatorSchema
from app.services import SimulatorService

router = APIRouter()


@router.post(
    "/simulation",
    tags=["Simulation"],
    response_model=SimulatorResponseSchema,
    status_code=status.HTTP_200_OK,
)
async def make_simulation(payload: SimulatorSchema):
    try:
        service = SimulatorService(car_details=payload)
        response = await service.make_simulation()
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        ) from e
