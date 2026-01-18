from django.shortcuts import render
from app.document import ApplicationService
from app.models import Wallet, WalletLogs

if list(Wallet.objects.all().values()) == []:
    for i in range(0,2):
        Wallet.objects.create(balance=100.00)

def WalletController(request):
    # wallet_id_to_debit = request.get('wallet_id_to_debit')
    # wallet_id_to_credit = request.get('wallet_id_to_credit')
    # value_of_transection = request.get('value_of_transection')
    amount_of_transection = 50.0

    for i in range(0,2):

        model = list(Wallet.objects.all().values())
        wallet_id_to_debit = model[i]['wallet_id']
        wallet_id_to_credit = model[i+1]['wallet_id']

        break

    obj = list(Wallet.objects.filter(wallet_id__in=[wallet_id_to_debit, wallet_id_to_credit]).values())

    debited_model_log = WalletLogs.objects.create(type='WalletDebited', wallet=wallet_id_to_debit, amount=amount_of_transection)

    wallet_app = ApplicationService(client_debit_uuid=obj[0]['wallet_id'], client_debit_balance=obj[0]['balance'],
                                    client_credit_uuid=obj[1]['wallet_id'], client_credit_balance=obj[1]['balance'],
                                    amount_of_transaction=amount_of_transection)
    
    debit_log = wallet_app.MakeDebit()

    if debit_log is None:

        debited_model_log.status = 'SUCCESS'
        debited_model_log.save()

        credited_model_log = WalletLogs.objects.create(type='WalletCredited', wallet=wallet_id_to_credit, amount=amount_of_transection)
        credit_log = wallet_app.MakeCredit()

        if credit_log is None:

            credited_model_log.status='SUCCESS'
            credited_model_log.save()
        else:
            credited_model_log.status='FAILED'
            credited_model_log.save()
        
    else:
        debited_model_log.status = 'FAILED'
        debited_model_log.save()