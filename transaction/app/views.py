from django.shortcuts import render
import json
from django.http import JsonResponse
from app.scripts.transaction import Transaction

def RegisterTransaction(request):

    if request.method == 'POST':
    
        body_request = json.loads(request.body)

        wallet_to_debit = body_request.get('wallet_to_debit_id')
        wallet_to_credit = body_request.get('wallet_to_credit_id')
        amount = body_request.get('amount')

        transaction_uuid = Transaction(wallet_to_debit, wallet_to_credit, amount).RegisterTransaction()

        return JsonResponse({'transaction_uuid':transaction_uuid}, status=200)