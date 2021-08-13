#!/usr/bin/env python3
  
import requests
import sympy
import os

worker_name = os.getpid()
master_api_url = "http://localhost:8000"


def get_task():
    res = requests.get(f'{master_api_url}/get_task/', params={"worker_name": worker_name})
    return res.json()

def calculate(i):
    return bool(sympy.isprime(2**i-1))

def publish_answer(task, answer):
    res = requests.post(f'{master_api_url}/post_task/', params={"worker_name": worker_name, "answer": answer, "task": task})
    return

resp = get_task() # returns dict: {'task_to_solve': '620412436'}
task = int(resp['task_to_solve'])
task = int(resp['task_to_solve'])
answer = calculate(task)
publish_answer(task, answer)
