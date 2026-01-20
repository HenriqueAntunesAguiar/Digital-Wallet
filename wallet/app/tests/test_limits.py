import pytest
from app.scripts.limits import Limits

def test_check_daily_limit_ok():
    limits = Limits(
        daily_limit=100,
        daily_limit_used=40,
        monthly_limit=500,
        monthly_limit_used=100
    )

    limits.check_daily_limit(50)  # não deve lançar erro

def test_check_daily_limit_exceeded():
    limits = Limits(
        daily_limit=100,
        daily_limit_used=60,
        monthly_limit=500,
        monthly_limit_used=100
    )

    with pytest.raises(Exception, match="Daily Limit Exceeded"):
        limits.check_daily_limit(50)

def test_check_monthly_limit_exceeded():
    limits = Limits(
        daily_limit=200,
        daily_limit_used=50,
        monthly_limit=300,
        monthly_limit_used=280
    )

    with pytest.raises(Exception, match="Monthly Limit Exceeded"):
        limits.check_monthly_limit(30)
