from app.scripts.wallet import Wallet
from app.models import WalletModel
class WalletApplicationService:

    def __init__(self, debit_wallet:str, debit_wallet_balance:float, credit_wallet:str, credit_wallet_balance:float, transaction_uuid):

        self.debit_wallet = Wallet(debit_wallet, debit_wallet_balance, transaction_uuid)
        self.credit_wallet = Wallet(credit_wallet,credit_wallet_balance, transaction_uuid)

    def execute(self, amount: float):
        try:
            self.debit_wallet.debit(amount)
            self.credit_wallet.credit(amount)        

            self.att_model(self.debit_wallet.wallet_id, self.debit_wallet.balance)
            self.att_model(self.credit_wallet.wallet_id, self.credit_wallet.balance)
            
            return {'status':'success', 'events':(
                self.debit_wallet.pull_events() +
                self.credit_wallet.pull_events()
            )}
        except Exception as e:
            return {'status':'fail','error':str(e)}
        
    def att_model(self, wallet_id, new_ballance):
        re = WalletModel.objects.get(wallet_id=wallet_id)
        re.balance = new_ballance
        re.save()


