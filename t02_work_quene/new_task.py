#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host="localhost"))
channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True) # write unhandled message to disk

message = "Hello World!...".encode("utf-8")
channel.basic_publish(exchange="",
                      routing_key="task_queue",
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent %r" % (message,))
connection.close()