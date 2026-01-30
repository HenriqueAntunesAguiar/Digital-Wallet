
# KAFKA FILE CONFIG
from kafka import KafkaProducer
import json, time

class WalletKafka:

    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_server='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )

    def send_successfull_event(self, _type, transaction_uuid, wallet_id, amount, new_balance):
        event = {
            'type':_type,
            'transaction_uuid':transaction_uuid,
            'wallet_id':wallet_id,
            'amount':amount,
            'new_balance':new_balance,
        }
        self.producer.send('wallet-events',event)
        self.producer.flush()

    def send_failed_event(self, _type, transaction_uuid, wallet_id, amount, error):
        event = {
            'type':_type,
            'transaction_uuid':transaction_uuid,
            'wallet_id':wallet_id,
            'amount':amount,
            'error':error
        }
        self.producer.send('wallet-events',event)
        self.producer.flush()