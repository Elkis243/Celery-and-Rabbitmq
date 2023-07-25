import pika
from django.core.management.base import BaseCommand
from app.models import Sale

 
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
        channel.basic_consume(queue='sales', on_message_callback=self.sales_data, auto_ack=True)

        self.stdout.write(
                self.style.SUCCESS("The consumer has started....")
            )
        channel.start_consuming()
        connection.close()

    def sales_data(ch, method, properties, body, b):
        data = b.decode('utf-8')
        data_split = data.split(',')
        dict_data = {}
        for item in data_split:
            key, value = item.split(':')
            dict_data[key.strip()] = value.strip()    
        article = dict_data['article']
        price = dict_data['price']
        quantity = int(dict_data['quantity'])
        amount = int(dict_data['amount'])
        branch = dict_data['branch']
        sale = Sale(
            article=article,
            price=str(price),
            quantity=quantity,
            amount=amount,
            branch=branch,
        )
        sale.save()
        print("[-] Message reçu !")
        
