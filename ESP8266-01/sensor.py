
from machine import Pin
import time
switch_1 = None
m = [1, 0]

def init_switch():
  global switch_1
  switch_1 = Pin(0, Pin.OUT, value = 1)
  
def switch_chage(i, s):

  if i in [0]:
    switch_1.value(m[s])
    print("Time=1")
    time.sleep(0.5)
    switch_1.value(m[0])

def get_SwitchData(n):
  if n in [0]:
    return m[int(switch_1.value())]





