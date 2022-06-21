import json
import os

import requests
import aminos
import threading
from replit import db
import platform,socket,re,uuid
import names
import random
from hashlib import sha1
import hmac
from sid_set import real , bots
from time import sleep
def restart():
    import sys
    print("argv was",sys.argv)
    print("sys.executable was", sys.executable)
    print("restart now")

    #import os
    os.execv(sys.executable, ['python'] + sys.argv)


def dev():
    hw=(names.get_full_name()+str(random.randint(0,10000000))+platform.version()+platform.machine()+names.get_first_name()+socket.gethostbyname(socket.gethostname())+':'.join(re.findall('..', '%012x' % uuid.getnode()))+platform.processor())
    identifier=sha1(hw.encode('utf-8')).digest()
    key='02b258c63559d8804321c5d5065af320358d366f'
    mac = hmac.new(bytes.fromhex(key), b"\x42" + identifier, sha1)
    return (f"42{identifier.hex()}{mac.hexdigest()}").upper()


def header(sid):
          headers = {
            "NDCDEVICEID": dev(),
            "Accept-Language": "en-US",
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": 'Dalvik/2.1.0 (Linux; U; Android 7.1; LG-UK495 Build/MRA58K; com.narvii.amino.master/3.4.33587)',
            "Host": "service.narvii.com",
            "Accept-Encoding": "gzip",
            "Connection": "Keep-Alive"}
          headers["NDCAUTH"] = f"sid={sid}"
          return headers
          
def live(sid,comId,chatId):
    header = {
    "NDCAUTH": f"sid={sid}",
    "NDCDEVICEID":dev()
}
    ws = aminos.Wss(header)
    ws.launch()
    wsClient = ws.getClient()
    wsClient.reputations(comId,chatId)
    
def vc_bot(sid,comId,chatId):
    header = {
    "NDCAUTH": f"sid={sid}",
    "NDCDEVICEID":dev()
}
    ws = aminos.Wss(header)
    ws.launch()
    wsClient = ws.getClient()
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


def info(sid,comId,chatId):
	response= requests.get(f"https://service.narvii.com/api/v1/x{comId}/s/chat/thread/{chatId}/avchat-reputation", headers=header(sid))
	return response.json()

def collect(sid,comId,chatId):
	response= requests.post(f"https://service.narvii.com/api/v1/x{comId}/s/chat/thread/{chatId}/avchat-reputation", headers=header(sid))
	return response.json()

def livee(comId,chatId):
	lines = []
	with open('vc.txt') as f:
	   	line = f.readlines()
	   	for l in line:
	   		lines.append(l.strip())
	for sid in lines:
		try: vc_bot(sid,comId,chatId)
		except: pass

def end_bot(comId,chatId):
	lines = []
	with open('vc.txt') as f:
	   	line = f.readlines()
	   	for l in line:
	   		lines.append(l.strip())
	for sid in lines:
		vc_bot(sid,comId,chatId)    

ll = []
with open('vc.txt') as h:
  linef= h.readlines()
  for lll in linef:
    ll.append(lll.strip())
	  
reals = []
with open('real.txt') as f:
  line = f.readlines()
  for l in line:
    reals.append(l.strip())
#g=["AnsiMSI6IG51bGwsICIwIjogMiwgIjMiOiAwLCAiMiI6ICJlOWRlZGQzOS03YzVlLTQ1MzItYTYyMi1hYmI0ZWQyMDI5M2QiLCAiNSI6IDE2NTMwNjY0OTMsICI0IjogIjEwNi4yMTEuMjQuMjEiLCAiNiI6IDEwMH05ARtzw4sixkwWllqUYK029MrX9g"]
com=["195570892"]

#com2="162738504"
#chatId=""
#db[com1]="92590aff-135e-4e05-b5ca-1e443eb552a5"
#db[com1]="8e5e9de7-fb00-4d5a-b53a-45b2c92e8acf"

for sid in ll:
  for _ in range(1):
    keys="195570892"
    chat="b1999466-e212-410d-9980-02254f5616b8"
    com=str(keys)
    #print(com)
    live(sid,int(keys),chat)
    c=info(sid,int(keys),chat)
    print(com)
    if c['api:statuscode']==1627:
      #del db[com]
      print(c['api:message'])
    if c['api:statuscode']==0:
      live(sid,int(keys),chat)
      
      try: threading.Thread(target=livee,args=[com,chat]).start()
      except: pass
      duplicates=[]
      while True:
        
        live(sid,int(keys),chat)
        p=info(sid,int(keys),chat)
        try:
          repp=p["availableReputation"]
          print(repp)
          duplicates.append(int(repp))
          if p["availableReputation"]>=10:
            
            collect(sid,com,chat)
            duplicates.clear()
            #db[sid]=reps+50
            #print(p["reputation"])
            #print(reps)
          x=duplicates.count(repp)
          if x >=6:
            collect(sid,com,chat)
            duplicates.clear()
        except:
          pass
        
        if p['api:statuscode']==1627:
          print(p['api:message'])
          
          #del db[str(keys)]
          print("deleted")
          break
    end(sid,com,chat)
  end(sid,com,chat)
  sleep(3)
  
exit()
#real()
#bots()
#restart()

