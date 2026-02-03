from wallet.domain.wallet import Wallet

class WalletApplicationService:

    def __init__(self, debit_wallet:str, debit_wallet_balance:float, credit_wallet:str, credit_wallet_balance:float, transaction_uuid):

        self.debit_wallet = Wallet(debit_wallet, debit_wallet_balance, transaction_uuid)
        self.credit_wallet = Wallet(credit_wallet, credit_wallet_balance, transaction_uuid)

    def execute(self, amount: float):

        try:
            self.debit_wallet.debit(amount)
            self.credit_wallet.credit(amount)        

            events = (self.debit_wallet.pull_events() + self.credit_wallet.pull_events())            

            return events
                
        except Exception as e:

            print(e)
            
            events = (self.debit_wallet.pull_events() + self.credit_wallet.pull_events())
            return events
           