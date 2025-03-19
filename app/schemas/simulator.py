from pydantic import BaseModel


class Simulator(BaseModel):
    brand: str
    model: str
    year: int
    price: float
    percentage: float
    broker_fee: float
