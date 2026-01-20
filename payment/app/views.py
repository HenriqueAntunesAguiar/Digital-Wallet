from django.shortcuts import render
from django.http import JsonResponse
import requests
from app.scripts.payment_application_service import PaymentApplicationService
import json

def CreateWallets(request):
    requests.get(url='localhost:8001/create-wallets/')

def MakePayment(request):
    body_request = json.loads(request.body)
    wallet_to_debit_id = body_request.get('wallet_to_debit_id')
    wallet_to_credit_id = body_request.get('wallet_to_credit_id')
    amount = body_request.get('amount')

    response = PaymentApplicationService(wallet_to_debit_id, wallet_to_credit_id, amount).Execute()
    return JsonResponse(response)
