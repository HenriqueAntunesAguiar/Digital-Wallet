from app.scripts.transaction import Transaction

class TransactionApplicationService:

    def __init__(self, obj, amount_of_transaction):
        
        self.debit_wallet = obj[0]['wallet_id']
        self.debit_wallet_balance = obj[0]['balance']
        self.credit_wallet = obj[1]['wallet_id']
        self.credit_wallet_balance = obj[1]['balance']
        self.amount_of_transaction = amount_of_transaction

    def ExecuteTransaction(self):

        Transaction(self.debit_wallet, self.debit_wallet_balance, self.credit_wallet, self.credit_wallet_balance, self.amount_of_transaction).MakeTransaction()