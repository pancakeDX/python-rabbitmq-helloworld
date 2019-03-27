#!/usr/bin/env python
import pika

#連接RMQ
user = 'guest'
password = 'guest'
host='localhost'
vhost='%2F'

rabbitmq_uri = 'amqp://{}:{}@{}:5672/{}'.format(user, password, host, vhost)

connection = pika.BlockingConnection(pika.connection.URLParameters(rabbitmq_uri))
channel = connection.channel()

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello_q1',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()