import pika
from django.core.management.base import BaseCommand
from app.models import Message

class Command(BaseCommand):
    help = 'RabbitMQ started consuming'

    def handle(self, *args, **options): 
        credentials = pika.PlainCredentials('guest', 'guest')
        connection  = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='localhost',
                port=5672,
                virtual_host='/',
                credentials=credentials,
                heartbeat=600,
                blocked_connection_timeout=300
            )
        )
        channel = connection.channel()
        channel.basic_consume(queue='messages', on_message_callback=self.messages_data, auto_ack=True)

        self.stdout.write(
                self.style.SUCCESS("The consumer has started....")
            )
        channel.start_consuming()
        connection.close()

    def messages_data(ch, method, properties, body, b):
        branch = 'Masina'
        data = b.decode('utf-8')
        data_split = data.split(',')
        dict_data = {}
        for item in data_split:
            key, value = item.split(':')
            dict_data[key.strip()] = value.strip()    
        branch_name= dict_data['branch_name']
        message = dict_data['message']
        if (branch == branch_name):
            msg = Message(
                branch_name=branch_name,
                message=message
            )
            msg.save()
            print("[-] Message reçu !")

        
