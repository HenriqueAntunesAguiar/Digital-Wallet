from django.shortcuts import render
from app.models import WalletModel
import json
from django.http import JsonResponse
from app.scripts.wallet_application_service import WalletApplicationService

def WalletController(request):
    
    if request.method == 'POST':
        body = json.loads(request.body)

        wallet_to_debit = body.get('wallet_id_to_debit')
        wallet_id_to_credit = body.get('wallet_id_to_credit')
        amount = body.get('amount')
        transaction_uuid = body.get('transaction_uuid')
    model = list(Wallet.objects.filter(wallet_id__in=[wallet_to_debit, wallet_id_to_credit]).values())

    for line in model:

        if line['wallet_id'] == wallet_to_debit:
            wallet_to_debit_balance = line['balance']    
        else:
            wallet_to_credit_balance = line['balance']    

    wallet_response = WalletApplicationService(wallet_to_debit=wallet_to_debit,
                            wallet_to_debit_balance=wallet_to_debit_balance,
                            wallet_to_credit=wallet_id_to_credit,
                            wallet_to_credit_balance=wallet_to_credit_balance,
                            transaction_uuid=transaction_uuid).execute(amount)
    if wallet_response['status'] == 'success':
        return JsonResponse({'events':wallet_response['events']}, status=200)
    
    else:
        return JsonResponse({'error':wallet_response['error']}, status=200)
    
