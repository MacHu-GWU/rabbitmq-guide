#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="topic_logs",
                         type="topic")

routing_key = "blue.red"
message = " ".join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange="topic_logs",
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()