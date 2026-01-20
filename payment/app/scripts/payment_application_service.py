import uuid
import requests

class PaymentApplicationService:

    def __init__(self, wallet_to_debit_id, wallet_to_credit_id, amount):
        self.wallet_to_debit_id = wallet_to_debit_id
        self.wallet_to_credit_id = wallet_to_credit_id
        self.amount = amount

    def Execute(self):
        # Limits Service
        limit_response = requests.post(url='localhost:8002/', data={
            'wallet_to_debit_id':uuid.UUID(self.wallet_to_debit_id),
            'amount':self.amount,
        })

        if limit_response.json()['allowed'] == True:

            transaction_response = requests.post(url='localhost:8003/', data={
                'wallet_to_debit_id':uuid.UUID(self.wallet_to_debit_id),
                'wallet_to_credit_id':uuid.UUID(self.wallet_to_credit_id),
                'amount':self.amount,
            })

            transaction_uuid = transaction_response.json()['transaction_uuid']
            
            # Wallet Service
            events = requests.post(url='localhost:8001/', data={
                'wallet_to_debit_id':uuid.UUID(self.wallet_to_debit_id),
                'wallet_to_credit_id':uuid.UUID(self.wallet_to_credit_id),
                'amount':self.amount,
                'transaction_uuid':transaction_uuid
            })

            return {'status':200}

        else:
            return limit_response.json()