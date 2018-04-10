#encoding ：utf-8
from django.db import models
import json

MESSAGE_FILE='message.json'

def get_messages():
    fhandler = open(MESSAGE_FILE, 'rt')
    mytext = fhandler.read()
    fhandler.close()
    return json.loads(mytext)


