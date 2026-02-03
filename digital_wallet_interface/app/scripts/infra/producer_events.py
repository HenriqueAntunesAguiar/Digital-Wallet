from confluent_kafka import Producer
import json

class KafkaWalletInterface:

    def __init__(self):
        conf={'bootstrap.server':'localhost:9092'}
        self.producer = Producer(conf)

    def callback_delivery(err, msg):

        if err:
            print(f'Erro ao entregar: {err}')
        else:
            print(f'Mensagem entregue em {msg.topic()} [{msg.partition()}]')

    def send_successfull_event(self, _type, transaction_uuid, wallet_id_to_debit, wallet_id_to_credit, amount):
        event = json.dumps({
            'type':_type,
            'transaction_uuid':transaction_uuid,
            'wallet_id_to_debit':wallet_id_to_debit,
            'wallet_id_to_credit':wallet_id_to_credit,
            'amount':amount,
        })
        self.producer.produce(topic='transaction_requested',
                              value=event,
                              callback=self.callback_delivery)
        
        self.producer.poll(0)