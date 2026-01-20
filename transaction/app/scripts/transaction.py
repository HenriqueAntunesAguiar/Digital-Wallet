from app.models import TransactionLogs

class Transaction:
    def __init__(self, wallet_to_debit, wallet_to_credit,  amount):

        self.amount = amount
        self.wallet_to_debit = wallet_to_debit
        self.wallet_to_credit = wallet_to_credit

    def RegisterTransaction(self):

        transaction = TransactionLogs(
                                    from_wallet=self.wallet_to_debit,
                                    to_wallet=self.wallet_to_credit,
                                    amount=self.amount,
                                    status="PENDING"
                                )
        transaction.save()
        return transaction.transaction_uuid

    def UpdateTransaction(self, transaction_uuid, status):
        re = TransactionLogs.objects.get(transaction_uuid=transaction_uuid)
        
        if status:
            
            re.status = 'COMPLITED'
        else:
            re.status = 'FAILED'

        re.save()