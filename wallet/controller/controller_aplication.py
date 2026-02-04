from domain.repositories.wallet_repository import WalletDb
from application.wallet_application_service import WalletApplicationService
    
class Controller:
    
    def __init__(self, event):
        self.wallet_id_to_credit = event['wallet_id_to_credit']
        self.wallet_id_to_debit = event['wallet_id_to_debit']
        self.transaction_uuid = event['transaction_uuid']
    
    def _run(self):
        
        wallet_db = WalletDb()
        wallet_to_credit_balance = wallet_db.get_wallet(wallet_id=self.wallet_id_to_credit).balance
        wallet_to_debit_balance = wallet_db.get_wallet(wallet_id=self.wallet_id_to_credit).balance

        wallet_response = WalletApplicationService(

            wallet_to_debit=self.wallet_id_to_debit,
            wallet_to_debit_balance=wallet_to_debit_balance,
            wallet_to_credit=self.wallet_id_to_credit,
            wallet_to_credit_balance=wallet_to_credit_balance,
            transaction_uuid=self.transaction_uuid
            
            ).execute(self.amount)
