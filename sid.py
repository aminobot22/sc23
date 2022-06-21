import json
from os import path
import json
import random
import os
from time import time as timestamp
#import requests
import names
from hashlib import sha1
from functools import reduce
from base64 import b85decode, b64decode
import random

import requests
import hmac
import platform,socket,re,uuid
import base64
from uuid import uuid4
# Empty list initialisation which will hold dictionaries from accounts.json
 

def sigg(data):
        key='f8e7a61ac3f725941e3ac7cae2d688be97f30b93'
        mac = hmac.new(bytes.fromhex(key), data.encode("utf-8"), sha1)
        digest = bytes.fromhex("42") + mac.digest()
        return base64.b64encode(digest).decode("utf-8")
def dev():
    hw=(names.get_full_name()+str(random.randint(0,10000000))+platform.version()+platform.machine()+names.get_first_name()+socket.gethostbyname(socket.gethostname())+':'.join(re.findall('..', '%012x' % uuid.getnode()))+platform.processor())
    identifier=sha1(hw.encode('utf-8')).digest()
    key='02b258c63559d8804321c5d5065af320358d366f'
    mac = hmac.new(bytes.fromhex(key), b"\x42" + identifier, sha1)
    return (f"42{identifier.hex()}{mac.hexdigest()}").upper()
def SID(email: str, password: str):
        headers = {
            "NDCDEVICEID": dev(),
            #"NDC-MSG-SIG": dev.device_id_sig,
            "Accept-Language": "en-US",
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/beyond1qlteue-user 5; com.narvii.amino.master/3.4.33562)",
            "Host": "service.narvii.com",
            "Accept-Encoding": "gzip",
            "Connection": "Keep-Alive"
        }
        
        data = json.dumps({
            "email": email,
            "v": 2,
            "secret": f"{password}",
            "deviceID": dev(),
            "clientType": 100,
            "action": "normal",
            "timestamp": int(timestamp() * 1000)
        })
        headers["NDC-MSG-SIG"]=sigg(data)
        sid=None
        proxies = {
   'http': 'socks5://dic:dick.py@3.39.171.7:52399',
   'https':'socks5://dic:dick.py@3.39.171.7:52399'}

        response = requests.post(f"https://service.narvii.com/api/v1/g/s/auth/login", headers=headers, data=data,proxies=proxies)
        
        if response.json()["api:message"]=="OK":
            sid=response.json()["sid"]
        else:
            print(response.text)
        
            
        return sid

 
def threadit(acc : dict): # Defining the 
    email=acc["email"] # Assigns the value 
    #device=acc["device"] # Assigns the value of "device" key inside device variable
    password=acc["secret"]
    sid=None# Assigns the value of "password" key inside password variable
    try:
      sid=SID(email,password)
    except Exception as j:
      print(j)
      pass
    return sid
            
 
