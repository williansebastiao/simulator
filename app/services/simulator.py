from datetime import datetime

from app.schemas import SimulatorSchema

RATE_PRODUCED = 0.5
CAR_VALUE = 0.5
CAR_PRICE = 10000


class SimulatorService:
    def __init__(self, car_details: SimulatorSchema):
        self.car_details = car_details

    async def rate_applied(self) -> float:
        car_details = self.car_details
        current_year = datetime.now().year
        car_age = current_year - car_details.year

        rate = (car_age * (RATE_PRODUCED / 100)) + (
            (car_details.price // CAR_PRICE) * (CAR_VALUE / 100)
        )
        return round(rate, 4)

    async def calculate_base_premium(self, rate_applied: float) -> float:
        car_details = self.car_details

        base_premium = round(car_details.price * rate_applied, 2)
        deductible_discount = round(
            base_premium * (car_details.percentage / 100), 2
        )
        premium = base_premium - deductible_discount + car_details.broker_fee

        return round(premium, 2)

    async def calculate_policy_limit(self):
        car_details = self.car_details

        base_policy_limit = car_details.price * (car_details.percentage / 100)
        deductible_value = base_policy_limit * (car_details.percentage / 100)
        final_policy_limit = base_policy_limit - deductible_value

        return round(final_policy_limit, 2), round(deductible_value, 2)

    async def make_simulation(self):
        rate_applied = await self.rate_applied()
        calculated_premium = await self.calculate_base_premium(rate_applied)
        policy_limit, deductible_value = await self.calculate_policy_limit()

        return {
            "car_details": self.car_details.model_dump(),
            "applied_rate": rate_applied,
            "calculated_premium": calculated_premium,
            "policy_limit": policy_limit,
            "deductible_value": deductible_value,
        }
