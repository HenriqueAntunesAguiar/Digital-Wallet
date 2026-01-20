from app.scripts.wallet import Wallet

class WalletApplicationService:

    def __init__(self, debit_wallet:str, debit_wallet_balance:float, credit_wallet:str, credit_wallet_balance:float):

        self.debit_wallet = Wallet(debit_wallet, debit_wallet_balance)
        self.credit_wallet = Wallet(credit_wallet,credit_wallet_balance)

    def execute(self, amount: float):

        self.debit_wallet.debit(amount)
        self.credit_wallet.credit(amount)        

        return (
            self.debit_wallet.pull_events() +
            self.credit_wallet.pull_events()
        )


