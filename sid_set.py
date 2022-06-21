from sid import threadit
from os import path
THIS_FOLDER = path.dirname(path.abspath(__file__))
import json # accounts.json file path
 
dictlist=[] 
def clear(vc):
    file=open(vc,"r+")
    file.truncate(0)
    file.close()

def bots():
    dic=[]
    emailfile=path.join(THIS_FOLDER,"vc.json")
    vc="vc.txt"
    clear(vc)
    with open(emailfile) as f:
      dic = json.load(f)
    print(f"{len(dic)} accounts loaded")
    for amp in dic:
        ss=threadit(amp)
        with open("vc.txt","a") as d:
          d.write(f"{ss}\n")
        print("saved")

def real():
    dick=[]
    emailfile=path.join(THIS_FOLDER,"real.json")
    vc="real.txt"
    clear(vc)
    with open(emailfile) as f:
      dick = json.load(f)
    print(f"{len(dick)} accounts loaded")
    for amp in dick:
        ss=threadit(amp)
        with open("real.txt","a") as d:
          d.write(f"{ss}\n")
        print("saved")