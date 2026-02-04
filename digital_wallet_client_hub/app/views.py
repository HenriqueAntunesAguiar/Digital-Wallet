from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
import uuid
from app.scripts.infra.producer_events import KafkaClientHubProducer

# Create your views here.
@csrf_exempt
def MakeTransaction(request):

    if request.method == 'POST':

        try:

            request_body = json.loads(request.body)
            wallet_id_to_debit = request_body.get('wallet_id_to_debit')
            wallet_id_to_credit = request_body.get('wallet_id_to_credit')
            amount = request_body.get('amount')
        
        except:

            return JsonResponse({'error': 'JSON inválido'}, status=400)
        
        transaction_uuid = uuid.uuid4()
        msg = {
            'wallet_id_do_debit':wallet_id_to_debit,
            'wallet_id_to_credit':wallet_id_to_credit,
            'amount':amount,
            'transaction_uuid':transaction_uuid

        }
        kafka_producer = KafkaClientHubProducer()
        kafka_producer.send_successfull_event(msg)

        return JsonResponse({'msg':'Solicitado com sucesso.'}, status=200)
    
    else:

        return JsonResponse({'error':'Método não permitido'}, status=405)
