#!/usr/bin/env python
import pika
import time
import os
import json
from connection import get_query 
import datetime

time.sleep(40)

########### CONNEXIÓN A RABBIT MQ #######################
HOST = os.environ['RABBITMQ_HOST']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channel = connection.channel()

#El consumidor utiliza el exchange 'nestor'
channel.exchange_declare(exchange='nestor', exchange_type='topic', durable=True)

#Se crea un cola temporaria exclusiva para este consumidor (búzon de correos)
result = channel.queue_declare(queue="db_querys", exclusive=True, durable=True)
queue_name = result.method.queue

#La cola se asigna a un 'exchange'
channel.queue_bind(exchange='nestor', queue=queue_name, routing_key="db_querys")


##########################################################


########## ESPERA Y HACE UN BUSQUEDA WIKIPEDIA CUANDO RECIBE UN MENSAJE ####

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    if str(body).startswith("b'[sql]"):
        query = str(body)[7:-1]
        print("sql -> " + query)

        fields_names, data = get_query(query)
        
        n = len(fields_names)
        res = "\n"
        for i in fields_names: res += (i + " | \t")
        for i in data:
            res += "\n"
            for j in range(n):
                val = i[j]
                if type(i[j]) is datetime.datetime: val = i[j].strftime("%m/%d/%Y")
                res += "{:<2} | ".format(i[j])

        print(res) 
        ########## PUBLICA EL RESULTADO COMO EVENTO EN RABBITMQ ##########
        channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body="[sql][result]" + res)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

###########################################################
