from datetime import datetime
from unittest.mock import AsyncMock

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import SimulatorSchema
from app.services import SimulatorService


@pytest.mark.asyncio
async def test_rate_applied():
    car_data = SimulatorSchema(
        brand="HB20S",
        model="Hyundai",
        year=2020,
        price=20000,
        percentage=10,
        broker_fee=100,
    )
    service = SimulatorService(car_details=car_data)

    expected_rate = ((datetime.now().year - 2020) * (0.5 / 100)) + (
        (20000 // 10000) * (0.5 / 100)
    )

    rate = await service.rate_applied()

    assert rate == round(expected_rate, 4)


@pytest.mark.asyncio
async def test_calculate_base_premium():
    car_data = SimulatorSchema(
        brand="HB20S",
        model="Hyundai",
        year=2020,
        price=20000,
        percentage=10,
        broker_fee=100,
    )
    service = SimulatorService(car_details=car_data)

    rate_applied = 0.01
    expected_premium = round(20000 * rate_applied, 2)
    deductible_discount = round(expected_premium * (10 / 100), 2)
    expected_final_premium = expected_premium - deductible_discount + 100

    premium = await service.calculate_base_premium(rate_applied)

    assert premium == round(expected_final_premium, 2)


@pytest.mark.asyncio
async def test_calculate_policy_limit():
    car_data = SimulatorSchema(
        brand="HB20S",
        model="Hyundai",
        year=2020,
        price=20000,
        percentage=10,
        broker_fee=100,
    )
    service = SimulatorService(car_details=car_data)

    expected_base_policy_limit = 20000 * (10 / 100)
    expected_deductible = expected_base_policy_limit * (10 / 100)
    expected_final_policy_limit = (
        expected_base_policy_limit - expected_deductible
    )

    policy_limit, deductible_value = await service.calculate_policy_limit()

    assert policy_limit == round(expected_final_policy_limit, 2)
    assert deductible_value == round(expected_deductible, 2)


@pytest.mark.asyncio
async def test_make_simulation(mocker):
    car_data = SimulatorSchema(
        brand="HB20S",
        model="Hyundai",
        year=2020,
        price=20000,
        percentage=10,
        broker_fee=100,
    )
    service = SimulatorService(car_details=car_data)

    mock_session = AsyncMock(spec=AsyncSession)
    mock_repository = mocker.patch(
        "app.repositories.CarRepository.store", new_callable=AsyncMock
    )
    mock_repository.return_value = car_data

    response = await service.make_simulation(session=mock_session)

    assert response["applied_rate"] is not None
    assert response["calculated_premium"] is not None
    assert response["policy_limit"] is not None
    assert response["deductible_value"] is not None
    assert response["car_details"] is not None
