from app.scripts.wallet import ApplicationService
from app.models import TransactionLogs

class Transaction:
    def __init__(self, obj, amount_of_transaction):
        self.amount_of_transaction = amount_of_transaction

        self.debit_wallet = obj[0]['wallet_id']
        self.debit_wallet_balance = obj[0]['balance']
        self.credit_wallet = obj[1]['wallet_id']
        self.credit_wallet_balance = obj[1]['balance']

    def MakeTransaction(self):

        transaction = TransactionLogs(
                                    from_wallet=self.debit_wallet,
                                    to_wallet=self.credit_wallet,
                                    amount=self.amount_of_transaction,
                                    status="PENDING"
                                )
        transaction.save()
        wallet_app = ApplicationService(
                                    debit_wallet=self.debit_wallet,
                                    debit_wallet_balance=self.debit_wallet_balance,
                                    credit_wallet=self.credit_wallet, 
                                    credit_wallet_balance=self.credit_wallet_balance
                                )
        try:
            wallet_app.execute(self.amount_of_transaction)
            transaction.status = "COMPLETED"
            transaction.save()

        except:
            transaction.status = "FAILED"
            transaction.save()

        