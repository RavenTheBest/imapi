import requests as rq
import random
import re

def linklist(search):
  a = rq.get(f"https://unsplash.com/s/photos/{search}").text
  regex = r"https://images\S+.=80"
  c = re.findall(regex, a)
  return c
  
def single(search):
  list = linklist(search)
  return list[random.randint(0,len(list))]
  
