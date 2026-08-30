import psutil
import time
while True:
 All_process = psutil.process_iter(['pid',"name","cpu_percent","memory_percent"])

 count = 0
 for proc in All_process:
  info = proc.info
  print("PID",info['pid'],"Name",info['name'],"Cpu %",info['cpu_percent'],"Memory%",info['memory_percent'])
  count = count+1
 print("Total Active Proceeses : ",count)
 time.sleep(3)
