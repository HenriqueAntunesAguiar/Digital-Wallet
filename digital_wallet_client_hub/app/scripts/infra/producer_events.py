from confluent_kafka import Producer
import json

class KafkaClientHubProducer:

    def __init__(self):
        conf={'bootstrap.servers':'kafka:29092'}
        self.producer = Producer(conf)

    def callback_delivery(self, err, msg):

        if err:
            print(f'Erro ao entregar: {err}')
        else:
            print(f'Mensagem entregue em {msg.topic()} [{msg.partition()}]')

    def send_requested_transaction(self, event):
        payload = {
            'transaction_uuid':event['transaction_uuid'],
            'wallet_id_to_debit':event['wallet_id_to_debit'],
            'wallet_id_to_credit':event['wallet_id_to_credit'],
            'amount':event['amount']
        }
        event = json.dumps(payload).encode('utf-8')
        self.producer.produce(topic='transaction_requested',
                              value=event,
                              callback=self.callback_delivery)
        
        self.producer.poll(0)
    
    def send_create_user(self):
        self.producer.produce(topic='create_wallet',
                              value=json.dumps({}).encode('utf-8'),
                              callback=self.callback_delivery)