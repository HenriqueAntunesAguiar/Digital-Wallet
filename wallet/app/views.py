from django.shortcuts import render
import json
from django.http import JsonResponse
from wallet.app.scripts.application.wallet_application_service import WalletApplicationService
from wallet.app.scripts.domain.repositories.wallet_repository import WalletDb
from wallet.app.scripts.infra.events import WalletKafka

def WalletController(request):
    
    if request.method == 'POST':
        body = json.loads(request.body)

        wallet_id_to_debit = body.get('wallet_id_to_debit')
        wallet_id_to_credit = body.get('wallet_id_to_credit')
        amount = body.get('amount')
        transaction_uuid = body.get('transaction_uuid')
    
    wallet_db = WalletDb()
    wallet_to_credit_balance = wallet_db.get_wallet(wallet_id=wallet_id_to_credit).balance
    wallet_to_debit_balance = wallet_db.get_wallet(wallet_id=wallet_id_to_credit).balance

    wallet_response = WalletApplicationService(

        wallet_to_debit=wallet_id_to_debit,
        wallet_to_debit_balance=wallet_to_debit_balance,
        wallet_to_credit=wallet_id_to_credit,
        wallet_to_credit_balance=wallet_to_credit_balance,
        transaction_uuid=transaction_uuid
        
        ).execute(amount)
    
    kafka = WalletKafka()

    try:
        if wallet_response['error']:
        
            for event in wallet_response:

                kafka.send_failed_event(
                    type=event['type'],
                    transaction_uuid=event['transaction_uuid'],
                    wallet_id=event['wallet_id'],
                    amount=event['amount'],
                    error=event['error']
                )
    
    except:

        for event in wallet_response:

            kafka.send_successfull_event(
                _type=event['type'],
                transaction_uuid=event['transaction_uuid'],
                wallet_id=event['wallet_id'], 
                amount=event['amount'], 
                new_balance=event['new_balance']
            )
    
