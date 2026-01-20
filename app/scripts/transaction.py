from app.scripts.wallet_application_service import WalletApplicationService
from app.models import TransactionLogs

class Transaction:
    def __init__(self, debit_wallet, debit_wallet_balance, credit_wallet, credit_wallet_balance,  amount_of_transaction):

        self.amount_of_transaction = amount_of_transaction
        self.debit_wallet = debit_wallet
        self.debit_wallet_balance = debit_wallet_balance
        self.credit_wallet = credit_wallet
        self.credit_wallet_balance = credit_wallet_balance

    def MakeTransaction(self):

        transaction = TransactionLogs(
                                    from_wallet=self.debit_wallet,
                                    to_wallet=self.credit_wallet,
                                    amount=self.amount_of_transaction,
                                    status="PENDING"
                                )
        transaction.save()
        wallet_app = WalletApplicationService(
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