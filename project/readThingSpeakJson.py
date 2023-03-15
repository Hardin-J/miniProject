import random
import urllib.request
import threading
import requests


def thingspeak_read():

    URL='https://api.thingspeak.com/channels/2064495/fields/1.json?api key='
    URL2='https://api.thingspeak.com/channels/2064495/fields/2.json?api key='
    KEY='XWIXMVEOS6M3HPRT'
    HEADER='&results=1'
    nUrl = URL+KEY+HEADER
    nUrl2 = URL2+KEY+HEADER
    #print(new_URL)
    
    getd = requests.get(nUrl).json() #gets url for name
    getd2 = requests.get(nUrl2).json() #get url for amount
    temp_id = 0
    entr yId = getd2['feeds'][0]['entry_id'] # get entry id of the transaction
    name = getd['feeds'][0]['field1']
    amt = getd2['feeds'][0]['field2']
    f = getd['feeds'] # taking feeds
    f2 = getd2['feeds']
    print(entryId)
    print(name)
    print(amt)
    n = []
    ent = []
    a= []
    for x in f:
        #print(x,end='\n\n')
        n.append(x['field1'])
        ent.append(x['entry_id'])
    for x in f2:
        a.append(x['field2'])
        ent.append(x['entry_id'])
    if ent[-2] == ent[-1]:
        print(n[-1])
    print(a[-1])

thingspeak_read()
