from limits.app.scripts.limits import Limits
import pytest

def test_daily_limit_exceeded():
    limits = Limits(
        daily_limit=100.0,
        daily_limit_used=100.0,
        monthly_limit=1000.0,
        monthly_limit_used=10.0
    )

    with pytest.raises(Exception) as exc:
        limits.check_daily_limit(1)

    assert str(exc.value) == "Daily Limit Exceeded"

def test_monthly_limit_exceeded():
    limits = Limits(
        daily_limit=1000.0,
        daily_limit_used=10.0,
        monthly_limit=100.0,
        monthly_limit_used=100.0
    )

    with pytest.raises(Exception) as exc:
        limits.check_monthly_limit(1)

    assert str(exc.value) == "Monthly Limit Exceeded"

def test_limits_within_bounds():
    limits = Limits(
        daily_limit=100.0,
        daily_limit_used=10.0,
        monthly_limit=1000.0,
        monthly_limit_used=100.0
    )

    limits.check_daily_limit(10)
    limits.check_monthly_limit(10)
