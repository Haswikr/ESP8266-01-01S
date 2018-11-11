
from machine import Timer, Pin
import time
import BreathLight
import WIFI
import Tcp
import sensor

def init_task():
  sensor.init_switch()
  try:
    init_WIFITimer()
  except:
    pass

def Init_wifiConnect():
  print(WIFI.Connect_WiFi_2())
  try:
    Tcp.TCP_Begin()
    init_TcpTimer()
    Send_login()
    time.sleep(0.5)
    Send_SensorData()
    init_TaskTimer()
  except:
    pass

def Send_login():
  Tcp.TCP_Send('M8IT25L3EL82OIKI')

def Send_SensorData():
  Tcp.TCP_Send("#{}#".format(sensor.get_SwitchData(0)))
  
def init_TaskTimer():
  tim3 = Timer(2)
  tim3.init(period=30000, mode=Timer.PERIODIC, callback=lambda t: Send_SensorData())

def init_TcpTimer():
  tim3 = Timer(3)
  tim3.init(period=50, mode=Timer.PERIODIC, callback=lambda t: Tcp.TCP_Recv())
  
def init_WIFITimer():
  tim3 = Timer(4)
  tim3.init(period=4000, mode=Timer.ONE_SHOT, callback=lambda t: Init_wifiConnect())

#init_task()

















