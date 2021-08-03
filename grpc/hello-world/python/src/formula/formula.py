#!/usr/bin/python3
import logging
import grpc
import os
from datetime import datetime
from formula import message_pb2
from formula import message_pb2_grpc

def run(text, name, surname):
    logging.basicConfig()
    client_request_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"{client_request_date} - Client Request: Text = \"{text}\", Name = \"{name}\", Surname = \"{surname}\"")

    # Configure channel
    channel = grpc.insecure_channel('localhost:50051')
    stub = message_pb2_grpc.MessageStub(channel)

    # Call the Message method from the message.proto file
    response = stub.Message(message_pb2.MessageRequest(text=text, name=name, surname=surname))
    server_response_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"{server_response_date} - Server Response: {response.message}")
