import json
import os
import requests
import aminos
import threading
import platform,socket,re,uuid
import names
import random
from hashlib import sha1
import hmac
from sid_set import real , bots
from time import sleep
import heroku3
from sid import threadit
from os import path
THIS_FOLDER = path.dirname(path.abspath(__file__))
import json # accounts.json file path
key=os.environ["key"]
apps=os.environ["app"]
command=os.environment ["command"]
chat="8a8fa84b-1efc-4d75-bc30-8f31738f9fc5"
com="195570892"
def restart():
    heroku_conn = heroku3.from_key(key)
    botapp= heroku_conn.apps()[apps]
    botapp.restart()

lines=[]
def bb():
    
    emailfile=path.join(THIS_FOLDER,"vc.json")
    with open(emailfile) as f:
      dic = json.load(f)
    print(f"{len(dic)} accounts loaded")
    for amp in dic:
        ss=threadit(amp)
        lines.append(ss)
        print("saved")


bb()

def dev():
    hw=(names.get_full_name()+str(random.randint(0,10000000))+platform.version()+platform.machine()+names.get_first_name()+socket.gethostbyname(socket.gethostname())+':'.join(re.findall('..', '%012x' % uuid.getnode()))+platform.processor())
    identifier=sha1(hw.encode('utf-8')).digest()
    key='02b258c63559d8804321c5d5065af320358d366f'
    mac = hmac.new(bytes.fromhex(key), b"\x42" + identifier, sha1)
    return (f"42{identifier.hex()}{mac.hexdigest()}").upper()
def vc_bot(sid,comId,chatId):
    header = {
        "NDCAUTH": f"sid={sid}",
        "NDCDEVICEID":dev()
    }
    ws = aminos.Wss(header)
    ws.launch()
    wsClient = ws.getClient()
    sleep(3)
    wsClient.joinVideoChatAsSpectator(comId,chatId)

def end(sid,comId,chatId):
  header = {
    "NDCAUTH": f"sid={sid}",
    "NDCDEVICEID":dev()
}
  ws = aminos.Wss(header)
  ws.launch()
  wsClient = ws.getClient()
  wsClient.endVoiceChat(comId,chatId)


if command=="ok":
    while True:
        for sid in lines:
            sleep(1)
            try: vc_bot(sid,com,chat)
            except: pass
            
else:
    pass
