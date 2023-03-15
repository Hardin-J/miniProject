import pandas as pd
import os
import json


na = str(input("Enter name: "))
no = int(input("Enter number: "))
a = {"from": na ,"amount":no}
print(a)
b = json.dumps(a)


def write_json(file):
    fr = open("temp_id.txt","r")
    i_d = fr.read()        
    with open("sample"+i_d+".json", "w") as outfile:
        outfile.write(file)


def read_json():
    while True:
        try:
            file = str(input("Enter file name:"))
            print(file)
            with open(file,"r") as f:
                fi = json.load(f)
                return fi
                break
        except (FileNotFoundError,OSError,json.decoder.JSONDecodeError):
            print("File not found: try some other file")
            
write_json(b)
#op = read_json()
#print(op)
