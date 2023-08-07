import requests


def delete(url, headers, json=None, verify=True):
    return requests.delete(url, json=json, headers=headers, verify=verify)


def get(url, headers, verify=True):
    return requests.get(url, headers=headers, verify=verify)


def post(url, headers, json=None, files=None, data=None, verify=True):
    return requests.post(url, json=json, files=files, data=data, headers=headers, verify=verify)


def put(url, headers, json=None, data=None, verify=True):
    return requests.put(url, json=json, data=data, headers=headers, verify=verify)


def patch(url, headers, json=None, data=None, verify=True):
    return requests.patch(url, json=json, data=data, headers=headers, verify=verify)


"""
from datetime import datetime
import requests

from Utils.constants import general


def delete(url, headers):
    timestamp = datetime.now()
    resp = requests.delete(url, headers=headers)
    if general.csv_write:
        general.csv_write.add_row(['DELETE', url, (datetime.now() - timestamp)])
    return resp


def get(url, headers):
    timestamp = datetime.now()
    resp = requests.get(url, headers=headers)
    if general.csv_write:
        general.csv_write.add_row(['GET', url, (datetime.now() - timestamp)])
    return resp


def post(url, headers, json=None, files=None, data=None):
    timestamp = datetime.now()
    resp = requests.post(url, json=json, files=files, data=data, headers=headers)
    if general.csv_write:
        general.csv_write.add_row(['POST', url, (datetime.now() - timestamp)])
    return resp


def put(url, headers, json=None, data=None):
    timestamp = datetime.now()
    resp = requests.put(url, json=json, data=data, headers=headers)
    if general.csv_write:
        general.csv_write.add_row(['PUT', url, (datetime.now() - timestamp)])
    return resp
"""
