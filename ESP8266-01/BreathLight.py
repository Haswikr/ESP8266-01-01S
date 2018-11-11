
from machine import Timer, Pin, PWM
import WIFI
dt = 0
po = 0
dis = 14
PWM1_Handle = None
def led_breath():
  try:
    global dt, po
    if(po == 0) :
      dt += dis
      if(dt >= 980):
        po = 1
    else:
      dt -= dis
      if(dt <=0):
        po = 0
    PWM1_Handle.duty(dt)
  except:
    pass
  
def BreathLight_init():
  global PWM1_Handle
  try:
    PWM1_Handle = PWM(Pin(2), freq=1000, duty=dt)
    tim6 = Timer(6)
    tim6.init(period=500, mode=Timer.PERIODIC, callback=lambda t: led_breath())
  except:
    pass
 



