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
ey=os.environ["key"]
apps=os.environ["app"]

def restart():
    heroku_conn = heroku3.from_key(key)
    botapp= heroku_conn.apps()[apps]
    botapp.restart()

lines=[]
def bb():
    
    emailfile=path.join(THIS_FOLDER,"real.json")
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

def sendactive(sid,comId):
    header = {
    "NDCAUTH": f"sid={sid}",
    "NDCDEVICEID":dev()
}
    ws = aminos.Wss(header)
    ws.launch()
    rang=30
    wsClient = ws.sendActive(comId,rang)
    return wsClient
    
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

def livee(comId,chatId,remove):
  #lines = []
  #with open('vc.txt') as f:
    #line = f.readlines()
    #for l in line:
      #lines.append(l.strip())
  for sid in lines:
    if sid !=remove:
      try: vc_bot(sid,comId,chatId)
      except: pass

def end_bot(comId,chatId):
  
  for sid in lines:
    vc_bot(sid,comId,chatId)    


	  

#g=["AnsiMSI6IG51bGwsICIwIjogMiwgIjMiOiAwLCAiMiI6ICJlOWRlZGQzOS03YzVlLTQ1MzItYTYyMi1hYmI0ZWQyMDI5M2QiLCAiNSI6IDE2NTMwNjY0OTMsICI0IjogIjEwNi4yMTEuMjQuMjEiLCAiNiI6IDEwMH05ARtzw4sixkwWllqUYK029MrX9g"]
#com=["195570892"]


  
for sid in lines:
  for _ in range(1):
    keys="195570892"
    chat="8a8fa84b-1efc-4d75-bc30-8f31738f9fc5"
    com=str(keys)
    for _ in range(2):
      try: print(sendactive(sid,com))
      except: pass
    #print(com)
    try: live(sid,int(keys),chat)
    except: pass
    c=info(sid,int(keys),chat)
    print(com)
    if c['api:statuscode']==1627:
      #del db[com]
      print(c['api:message'])
    if c['api:statuscode']==0:
      try:
        live(sid,int(keys),chat)
        
        try: threading.Thread(target=livee,args=[com,chat,sid]).start()
        except: pass
        duplicates=[]
        while True:
          
          live(sid,int(keys),chat)
          p=info(sid,int(keys),chat)
          try:
            repp=p["availableReputation"]
            print(repp)
            duplicates.append(int(repp))
            if p["availableReputation"]>=50:
              
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
      except:
        pass
  try: end(sid,com,chat)
  except: pass
  #end(sid,com,chat)
  sleep(7)

#exit()
for i in range(7200):
    print(i)
    sleep(1)
restart()
