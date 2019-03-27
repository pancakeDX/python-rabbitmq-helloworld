import pika

#連接RMQ
user = 'guest'
password = 'guest'
host='localhost'
vhost='%2F'


#RMQ參數定義
exchange = 'hello_exchange'
routing_key = 'hello_rk'

rabbitmq_uri = 'amqp://{}:{}@{}:5672/{}'.format(user, password, host, vhost)
connection = pika.BlockingConnection(pika.connection.URLParameters(rabbitmq_uri))
channel = connection.channel()

channel.basic_publish(exchange=exchange, routing_key=routing_key, body='Hello World', 
                        properties=pika.BasicProperties(delivery_mode = 2))
