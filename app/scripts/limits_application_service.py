from app.models import WalletLimits
from app.scripts.limits import Limits

class LimitsApplicationService:

    def __init__(self, wallet_id:str):
        self.wallet_id = wallet_id
        self.model_wallet_limit = WalletLimits.objects.get(wallet_id=self.wallet_id)

    def GetDatasOfWallet(self, amount:float):

        daily_limit = self.model_wallet_limit.daily_limit
        monthly_limit = self.model_wallet_limit.monthly_limit
        daily_limit_used = self.model_wallet_limit.daily_limit_used
        monthly_limit_used = self.model_wallet_limit.monthly_limit_used

        limits = Limits(self.wallet_id, daily_limit, daily_limit_used, monthly_limit, monthly_limit_used)
        
        limits.check_daily_limit(amount)
        limits.check_monthly_limit(amount)

    def UpdateUsedLimits(self, amount:float):
        self.model_wallet_limit.daily_limit_used += amount
        self.model_wallet_limit.monthly_limit_used += amount
        self.model_wallet_limit.save()
        