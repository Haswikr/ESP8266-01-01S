
import json
import task
import sensor

def User_CallBack(c):
  c = c[2:-1]
  print(c)
  try:
    load_js = json.loads(c)
  except:
    print("JSON解析失败")
  try:
    function = load_js['msg']
  except:
    function = None
  try:
    device = load_js['dev']
  except:
    device = None
  try:
    status = load_js['sta']
  except:
    status = None
  
  print(function) 
  print(device)
  print(status)
  
  try:
    if str(function) == "rec":
      task.Send_SensorData()
    elif (function) == "swt":
      try:
        sensor.switch_chage(int(device), int(status))
        task.Send_SensorData()
      except:
        print("开关操作错误")
  except:
    print("消息任务处理错误")

