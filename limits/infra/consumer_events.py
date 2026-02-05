
# KAFKA FILE CONFIG
from confluent_kafka import Consumer
import json
from controller.limits_application_service import LimitsApplicationService, CreateLimits

class KafkaLimitsConsumer:

    def __init__(self):
        conf = {'bootstrap.servers':'kafka:29092',
                'group.id':'limit-service',
                'auto.offset.reset':'earliest'}
        self.consumer = Consumer(conf)
        self.consumer.subscribe(['transaction_requested', 'update_limit', 'create_limit'])

    def _run(self):

        print('Limit - esperando mensagem')
        
        while True:
            msg = self.consumer.poll(1.0)

            if msg is None:
                continue
            
            if msg.error():
                print(msg.error())
                continue
            
            print('Recebido:', json.loads(msg.value().decode('utf-8')))
            
            if msg.topic() == 'transaction_requested':
                LimitsApplicationService(msg.value).get_check_limits()
            
            if msg.topic() == 'update_limit':
                LimitsApplicationService(msg.value).update_used_limits()
            
            if msg.topic() == 'create_limit':
                CreateLimits(msg.value).create_limit()

if __name__ == '__main__':
    print('Limit - executando consumer')
    KafkaLimitsConsumer()._run()
