class Wallet:

    def __init__(self, wallet_id: str, balance: float, transaction_uuid):
        self.wallet_id = wallet_id
        self.balance = balance
        self._events = []
        self.transaction_uuid = transaction_uuid

    def debit(self, amount: float):
        if self.balance < amount:
            raise Exception("Insufficient funds")

        self.balance -= amount
        self._events.append({
            "type": "WalletDebited",
            "wallet_id": self.wallet_id,
            "transaction_uuid":self.transaction_uuid, 
            "amount": amount
        })

    def credit(self, amount: float):
        self.balance += amount
        self._events.append({
            "type": "WalletCredited",
            "wallet_id": self.wallet_id,
            "transaction_uuid":self.transaction_uuid, 
            "amount": amount
        })

    def pull_events(self):
        events = self._events
        self._events = []
        return events

