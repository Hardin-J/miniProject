import pandas as pd
import os
import json
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
        entryId = getd2['feeds'][0]['entry_id'] # get entry id of the transaction
        name = getd['feeds'][0]['field1']
        amt = getd2['feeds'][0]['field2']
        return (entryId,name,amt)

def write_json(file,i_d):
        i_d = str(i_d)
        with open("file/speak"+i_d+".json", "w") as outfile:
            outfile.write(file)


while True:
    
    f = open("temp_id.txt", "r")
    temp_id = f.read()
    temp_id = int(temp_id)
    print(temp_id)
    f.close()

    i_d, name, amt = thingspeak_read()
    if temp_id != i_d:
        print(type(temp_id) , type(i_d))
        a = {"from": name ,"amount":amt}
        b = json.dumps(a)
        write_json(b,i_d)
        d = open("temp_id.txt", "w")
        l = i_d
        d.write(str(l))
        d.close()
        print("File saved Successfully")
    else:
        print("File not saved")
    

