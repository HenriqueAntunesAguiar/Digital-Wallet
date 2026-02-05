class Limits:

    def __init__(self, daily_limit:float, daily_limit_used:float, monthly_limit:float, monthly_limit_used:float):

        self.daily_limit = daily_limit
        self.daily_limit_used = daily_limit_used
        self.monthly_limit = monthly_limit
        self.monthly_limit_used = monthly_limit_used

    def check_daily_limit(self, amount):

        if self.daily_limit_used + amount > self.daily_limit:
            raise Exception("Daily Limit Exceeded")

    def check_monthly_limit(self, amount):
        if self.monthly_limit_used + amount > self.monthly_limit:
            raise Exception("Monthly Limit Exceeded")

