import pyttsx3
import glob
import pandas as pd
import os
import json
import urllib.request
import threading
import requests
from time import sleep


def phase():
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
                #print(temp_id)
                f.close()
                i_d, name, amt = thingspeak_read()
                if temp_id != i_d:
                        #print(type(temp_id) , type(i_d))
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
                sleep(0.25)
                        

def phase2():
	en = pyttsx3.init()
	en.setProperty('rate',120)
	en.setProperty('volume',1.0)
	
	while True:
		try:
			files = glob.glob('file/*', recursive=True)
			for single_file in files:
				with open(single_file, 'r') as f:
					#print(single_file)
					json_file = json.load(f)
					name = json_file['from']
					amount = json_file['amount']
					print(f'username {name} sent {amount} Recieved Successfully')
					en.say(f'username {name} sent {amount} Recieved Successfully')
					en.runAndWait()
					os.remove(single_file)
		except (FileNotFoundError,json.decoder.JSONDecodeError):
			print("file not found!")
		sleep(0.25)

# creating thread
t1 = threading.Thread(target=phase)
t2 = threading.Thread(target=phase2)

# starting thread 1
t1.start()
# starting thread 2
t2.start()
