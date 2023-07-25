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
channel.queue_declare(queue= 'messages')
channel.queue_bind(exchange='operations', queue='messages', routing_key='messages')

def publish_message(data):
       channel.basic_publish(exchange='operations', routing_key='messages', body=data)
       print("[-] Message envoyé !")