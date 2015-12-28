#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

message = "info: Hello World!".encode("utf-8")
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % (message,))
connection.close()