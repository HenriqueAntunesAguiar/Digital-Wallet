from datetime import datetime

class Wallet:

    def __init__(self, wallet_id:str, balance:float):
       self.wallet_id = wallet_id
       self.balance = balance
       self.events = []

    def debit(self, amount:float):
        if self.balance - amount < 0:
            raise Exception('Invalid amount')
        
        self.balance -= amount
        self.events.append({
            'type': 'WalletDebited',
            'wallet_id': self.wallet_id,
            'amount': amount
        })

    def credit(self, amount:float):
        self.balance += amount
        self.events.append({
            'type': 'WalletCredited',
            'wallet_id': self.wallet_id,
            'amount': amount
        })

    def GetEvents(self):
        events = self.events
        self.events = []

        return events

class ApplicationService:
    
    def __init__(self, client_debit_uuid, client_debit_balance, client_credit_uuid, client_credit_balance, amount_of_transaction):

        self.client_credit_uuid = client_credit_uuid
        self.client_credit_balance = client_credit_balance
        self.client_credit_wallet = Wallet(client_credit_uuid, client_credit_balance)

        self.client_debit_uuid = client_debit_uuid
        self.client_debit_balance = client_debit_balance

        self.amount_of_transaction = amount_of_transaction

    def MakeDebit(self):

        client_debit_wallet = Wallet(self.client_debit_uuid, self.client_debit_balance)

        try:
            client_debit_wallet.debit(self.amount_of_transaction)
            return None
        
        except Exception as error:
            return str(error)

    def MakeCredit(self):

        client_credit_wallet = Wallet(self.client_credit_uuid, self.client_credit_balance)
        client_credit_wallet.credit(self.amount_of_transaction)

