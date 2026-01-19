class Wallet:

    def __init__(self, wallet_id: str, balance: float):
        self.wallet_id = wallet_id
        self.balance = balance
        self._events = []

    def debit(self, amount: float):
        if self.balance < amount:
            raise Exception("Insufficient funds")

        self.balance -= amount
        self._events.append({
            "type": "WalletDebited",
            "wallet_id": self.wallet_id,
            "amount": amount
        })

    def credit(self, amount: float):
        self.balance += amount
        self._events.append({
            "type": "WalletCredited",
            "wallet_id": self.wallet_id,
            "amount": amount
        })

    def pull_events(self):
        events = self._events
        self._events = []
        return events

class ApplicationService:

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


