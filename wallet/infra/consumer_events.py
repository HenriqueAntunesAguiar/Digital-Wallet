
# KAFKA FILE CONFIG
from confluent_kafka import Consumer
import json
from controller.controller_aplication import Controller, CreateWallet

class KafkaWalletConsumer:

    def __init__(self):
        conf = {'bootstrap.servers':'kafka:29092',
                'group.id':'wallet-service',
                'auto.offset.reset':'earliest'}
        self.consumer = Consumer(conf)
        self.consumer.subscribe(['limit_approved', 'create_wallet'])

    def _run(self):

        print('Wallet - esperando mensagem')
        
        while True:
            msg = self.consumer.poll(1.0)

            if msg is None:
                continue
            
            if msg.error():
                print(msg.error())
                continue

            print('Recebido:', json.loads(msg.value().decode('utf-8')))

            if msg.topic == '':
                Controller(msg.value)._run()

            elif msg.topic == 'create_wallet':
                CreateWallet.create()

if __name__ == '__main__':
    print('Wallet - executando consumer')
    KafkaWalletConsumer()._run()
