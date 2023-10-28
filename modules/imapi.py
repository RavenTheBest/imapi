import requests as rq
import random
import re

def linklist(search):
  try:
    b = rq.get(f"https://unsplash.com/s/photos/{search}")
  except:
    return "Error occured"
    
  if b.status_code == 200:
    a = b.text
  regex = r"https://images\S+.=80"
  c = re.findall(regex, a)
  return c
  
def single(search):
  list = linklist(search)
  return list[random.randint(0,len(list))]
  
def download(search, ex):
  if ex == None:
    ex = "png"
  url = single(search)
  try:
    img = rq.get(url).content
    open(f"{search}.{ex}", "wb").write(img)
    return search+"."+ex
  except:
    return "Error occured"
