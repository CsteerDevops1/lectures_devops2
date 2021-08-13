#!/usr/bin/env python3

import json, random 

data = {}
data['tasks'] = []

idUser = 0
i = 0

open('data.txt', 'w').close()

for seq in range(100):
   idUser += 1
   taskNumber = random.randint(10**8, 10**9)
   data['tasks'].append({
       'id': str(idUser),
       'taskNumber': str(taskNumber),
       'taskStatus': 'Ready to start',
       'taskWorker': '',
       'taskResult': ''
   })

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
