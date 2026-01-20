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

