import pytest

from src.main import app


class TestLiftPass:
    def test_add_new_price(self) -> None:
        client = app.test_client()
        response = client.put("/prices", query_string={"type": "test", "cost": 40})
        assert response.status_code == 200

    def test_1jour_general_price_is_35(self) -> None:
        client = app.test_client()
        response = client.get("/prices", query_string={"type": "1jour"})
        assert response.json == {"cost": 35}

    def test_1jour_cost_is_35_if_is_holiday(self) -> None:
        client = app.test_client()
        response = client.get(
            "/prices", query_string={"type": "1jour", "date": "2019-02-25"}
        )
        assert response.json == {"cost": 35}

    def test_1jour_cost_is_35_percent_reduced_if_is_not_holiday_and_is_monday(
        self,
    ) -> None:
        client = app.test_client()
        response = client.get(
            "/prices", query_string={"type": "1jour", "date": "2024-02-26"}
        )
        assert response.json == {"cost": 23}

    @pytest.mark.parametrize(
        "age, expected_price", [(5, 0), (10, 25), (65, 27), (16, 35)]
    )
    def test_1jour_cost_with_age_matches_expected_price(
        self, age: int, expected_price: int
    ) -> None:
        client = app.test_client()
        response = client.get(
            "/prices", query_string={"type": "1jour", "age": f"{age}"}
        )
        assert response.json == {"cost": expected_price}

    def test_night_general_price_is_0(self) -> None:
        client = app.test_client()
        response = client.get("/prices", query_string={"type": "night"})
        assert response.json == {"cost": 0}

    @pytest.mark.parametrize("age, expected_price", [(10, 19), (65, 8)])
    def test_night_cost_with_age_matches_expected_price(
        self, age: int, expected_price: int
    ) -> None:
        client = app.test_client()
        response = client.get(
            "/prices", query_string={"type": "night", "age": f"{age}"}
        )
        assert response.json == {"cost": expected_price}
