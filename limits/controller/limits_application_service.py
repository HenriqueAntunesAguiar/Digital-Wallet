from domain.repositories.limits_repository import LimitDb
from domain.limits import Limits
from infra.producer_events import KafkaLimitsProducer

class LimitsApplicationService:

    def __init__(self, event):
        self.event = event
        self.wallet_id = event['wallet_id']
        self.amount = event['amount']

        self.wallet_limit_db = LimitDb.get_limit(wallet_id=self.wallet_id)
        
        self.daily_limit = self.wallet_limit_db['daily_limit']
        self.daily_limit_used = self.wallet_limit_db['daily_limit_used']
        self.monthly_limit = self.wallet_limit_db['monthly_limit']
        self.monthly_limit_used = self.wallet_limit_db['monthly_limit_used']

    def get_check_limits(self):

        limits = Limits(self.daily_limit, self.daily_limit_used, self.monthly_limit, self.monthly_limit_used)

        kafka_limits = KafkaLimitsProducer()

        try:
            limits.check_daily_limit(self.amount)
            limits.check_monthly_limit(self.amount)
            kafka_limits.limit_approved(self.event)

        except Exception as err:
            self.event['error'] = err
            kafka_limits.limit_denied(self.event)


    def update_used_limits(self, amount:float):
        
        self.daily_limit_used += amount
        self.monthly_limit_used += amount

        self.wallet_limit_db.update_limits(self.wallet_id, self.daily_limit, self.daily_limit_used, self.monthly_limit, self.monthly_limit_used)
        self.wallet_limit_db.close()

class CreateLimits:

    def __init__(self, event):
        self.event = event
        self.wallet_id = event['wallet_id']

    def create_limit(self):
        try:
            daily_limit = self.event['daily_limit']
            monthly_limit = self.event['monthly_limit']
        except:
            daily_limit = 1000.00
            monthly_limit = 30000.00

        self.wallet_limit_db = LimitDb.create_limit(wallet_id=self.wallet_id, daily_limit=daily_limit, monthy_limit=monthly_limit)
