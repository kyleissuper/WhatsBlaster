#!/usr/local/bin/python

from WhatsBlaster import WhatsBlaster

W = WhatsBlaster()

print('Reading a message to send')

with open('message.txt', 'r') as message_file:
        message = message_file.read().strip()

print('Reading recipient list')
with open('recipient_list.txt', 'r') as recipient_list:
    for recipient in recipient_list:
        print W.send_message(recipient.strip(), message)

W.close()
