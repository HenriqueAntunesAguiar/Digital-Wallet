
# KAFKA FILE CONFIG
from confluent_kafka import Producer
import json

class KafkaLimitsProducer:

    def __init__(self):
        conf = {'bootstrap.servers':'kafka:29092'}
        self.producer = Producer(conf)

    def callback_delivery(err, msg):

        if err:
            print(f'Erro ao entregar: {err}')
        else:
            print(f'Mensagem entregue em {msg.topic()} [{msg.partition()}]')

    def limit_approved(self, event):
        msg = json.dumps({
            'transaction_uuid':event['transaction_uuid'],
            'wallet_id_to_debit':event['wallet_id_to_debit'],
            'wallet_id_to_credit':event['wallet_id_to_credit'],
            'amount':event['amount']
        })
        self.producer.produce(topic='wallet_approved',
                              value=msg,
                              callback=self.callback_delivery)
        
        self.producer.poll(0)

    def limit_denied(self, event):
        msg = json.dumps({
            'transaction_uuid':event['transaction_uuid'],
            'wallet_id_to_debit':event['wallet_id_to_debit'],
            'wallet_id_to_credit':event['wallet_id_to_credit'],
            'amount':event['amount'],
            'error':event['error']
        })
        self.producer.produce(topic='wallet_denied',
                              value=msg,
                              callback=self.callback_delivery)
        
        self.producer.poll(0)

