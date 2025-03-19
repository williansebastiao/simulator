from pydantic import BaseModel


class SimulatorSchema(BaseModel):
    brand: str
    model: str
    year: int
    price: float
    percentage: float
    broker_fee: float

    model_config = {
        "from_attributes": True,
    }


class SimulatorResponseSchema(BaseModel):
    car_details: SimulatorSchema
    applied_rate: float
    calculated_premium: float
    policy_limit: float
    deductible_value: float
