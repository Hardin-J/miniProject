import json
import os
import glob

files = glob.glob('file/*', recursive=True)

for single_file in files:
    with open(single_file, 'r') as f:
        try:
            json_file = json.load(f)
            name = json_file['from']
            amount = json_file['amount']
        except:
            pass
    print(f'username {name} sent {amount} Recieved Successfully')
