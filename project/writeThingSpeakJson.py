import random
import urllib.request
import threading
import requests

def thingspeak_write():
    val = "vijay"
    val2 = 75
    URL='https://api.thingspeak.com/update?api_key='
    KEY='V063BTV76TYE1I3V'
    HEADER='&field1={}&field2={}'.format(val,val2)
    new_URL=URL+KEY+HEADER
    print(new_URL)
    v = urllib.request.urlopen(new_URL)
    print(v)

thingspeak_write()
