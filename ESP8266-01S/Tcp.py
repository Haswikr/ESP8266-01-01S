
import network
import socket
import time
import sys
import Recive
from machine import Timer

#WiFi密码以及服务器连接信息配置
host = "112.74.142.132"
port = 8647


def TCP_Begin():
  global s
  s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  try:
    s.connect((host,port))
    print ("服务器已连接")
  except:
    print ("服务器连接失败 Please Check PORT or IPaddress")
  s.setblocking(False)

def TCP_Send(text):
  try:
    s.send(text)
    print("数据发送成功:"+text)
  except:
    print ("数据发送错误 Try to Resend")
    try:
      s.send(text)
      print("数据发送成功:"+text)
    except:
      print ("数据发送错误 Try to Reconnect...")
      TCP_Begin()
      try:
        s.send(text)
        print("数据发送成功:"+text)
      except:
        print ("数据发送失败！")
        pass

def TCP_Recv():
    try:
      RecvBuf=s.recv(1024)
    except :
      pass
    else:
      if not len(RecvBuf):
        pass
      #print("收到数据:" + str(RecvBuf))
      print("收到数据")
      Recive.User_CallBack(str(RecvBuf))
      




