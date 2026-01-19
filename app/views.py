from django.shortcuts import render
from app.models import Wallet
from app.scripts.transaction import Transaction

if list(Wallet.objects.all().values()) == []:
    for i in range(0,2):
        Wallet.objects.create(balance=100.00)

def WalletController(request):
    # wallet_id_to_debit = request.get('wallet_id_to_debit')
    # wallet_id_to_credit = request.get('wallet_id_to_credit')
    # value_of_transection = request.get('value_of_transection')
    amount_of_transaction = 50.0

    for i in range(0,2):

        model = list(Wallet.objects.all().values())
        wallet_id_to_debit = model[i]['wallet_id']
        wallet_id_to_credit = model[i+1]['wallet_id']

        break

    obj = list(Wallet.objects.filter(wallet_id__in=[wallet_id_to_debit, wallet_id_to_credit]).values())

    Transaction(obj=obj, amount_of_transaction=amount_of_transaction)