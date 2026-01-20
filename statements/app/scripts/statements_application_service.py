from app.models import TransactionLogs
from datetime import datetime
from app.scripts.statements import WalletExtract

class WalletExtractApplicationService:

    def __init__(self, wallet_id):
        self.wallet_id = wallet_id

    def GetDataForExtract(self):
        now = datetime.now()
        transaction_model = list(TransactionLogs.objects.filter(timestamp__year=now.year,
                                                                timestamp__month=now.month,
                                                                wallet_id=self.wallet_id,
                                                                status='COMPLETED').values())

        return WalletExtract(transaction_model).Extract()