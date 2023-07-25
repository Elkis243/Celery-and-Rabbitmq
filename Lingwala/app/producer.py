import pika

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
channel.exchange_declare('operations', durable=True, exchange_type='topic')
channel.queue_declare(queue= 'sales')
channel.queue_bind(exchange='operations', queue='sales', routing_key='sales')

def publish_sale(data):
       channel.basic_publish(exchange='operations', routing_key='sales', body=data)
       print("[-] Message envoyé !")