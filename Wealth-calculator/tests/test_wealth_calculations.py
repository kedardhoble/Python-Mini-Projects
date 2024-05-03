import pytest
from ..main import calculate_wealth_by_year, calculate_years_till_freedom

# Fixture to provide common test data
@pytest.fixture
def wealth_parameters():
    return {
        "current_wealth": 10000,
        "rate_of_return": 5,
        "monthly_savings": 500,
        "years": 10,
        "target_wealth": 100000,
    }

# Test cases for `calculate_wealth_by_year`
@pytest.mark.parametrize("rate_of_return, monthly_savings, expected_result", [
    (5, 500, [17100.00, 24605.00, 32635.25, 41216.01, 50479.81, 60564.80, 71615.04, 83780.79, 97119.83, 111709.82]),  # 10 years, 5% return
    (0, 500, [16000.00, 22000.00, 28000.00, 34000.00, 40000.00, 46000.00, 52000.00, 58000.00, 64000.00, 70000.00]),  # 10 years, 0% return
])
def test_calculate_wealth_by_year(wealth_parameters, rate_of_return, monthly_savings, expected_result):
    current_wealth = wealth_parameters["current_wealth"]
    years = wealth_parameters["years"]

    result = calculate_wealth_by_year(current_wealth, rate_of_return, monthly_savings, years)

    # Use approximation for floating-point comparisons
    assert result == pytest.approx(expected_result, rel=1e-2)

# Test cases for `calculate_years_till_freedom`
@pytest.mark.parametrize("target_wealth, expected_years", [
    (100000, 10),  # 10 years to reach 100k with 5% return and $500/month
    (20000, 2),  # 2 years to reach 20k with 0% return
    (5000, 0),  # Already reached target wealth
])
def test_calculate_years_till_freedom(wealth_parameters, target_wealth, expected_years):
    current_wealth = wealth_parameters["current_wealth"]
    rate_of_return = wealth_parameters["rate_of_return"]
    monthly_savings = wealth_parameters["monthly_savings"]

    result = calculate_years_till_freedom(current_wealth, rate_of_return, monthly_savings, target_wealth)

    assert result == expected_years
