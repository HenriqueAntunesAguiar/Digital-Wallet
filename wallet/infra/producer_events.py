
# KAFKA FILE CONFIG
from confluent_kafka import Producer
import json

class KafkaWalletProducer:

    def __init__(self):
        conf = {'bootstrap.servers':'kafka:29092'}
        self.producer = Producer(conf)

    def callback_delivery(err, msg):

        if err:
            print(f'Erro ao entregar: {err}')
        else:
            print(f'Mensagem entregue em {msg.topic()} [{msg.partition()}]')

    def send_wallet_successfull(self, _type, transaction_uuid, wallet_id, amount, new_balance):
        event = json.dumps({
            'type':_type,
            'transaction_uuid':transaction_uuid,
            'wallet_id':wallet_id,
            'amount':amount,
            'new_balance':new_balance,
        })
        self.producer.produce(topic='wallet_approved',
                              value=event,
                              callback=self.callback_delivery)
        
        self.producer.poll(0)

    def send_wallet_failed(self, _type, transaction_uuid, wallet_id, amount, error):
        event = json.dumps({
            'type':_type,
            'transaction_uuid':transaction_uuid,
            'wallet_id':wallet_id,
            'amount':amount,
            'error':error
        })
        self.producer.produce(topic='wallet_denied',
                              value=event,
                              callback=self.callback_delivery)
        
        self.producer.poll(0)

    def send_create_limit(self, wallet_id):
        event = json.dumps({
            'wallet_id':wallet_id
        })
        self.producer.produce(topic='create_limit',
                              value=event,
                              callback=self.callback_delivery)
        
        self.producer.poll(0)
