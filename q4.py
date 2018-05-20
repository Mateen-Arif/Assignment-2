import os
import psutil 
import time

pID=input("Enter Process id: ")
for process in psutil.process_iter():
	if(process.pid==pID):
		print "Process ID : (0)".format(process.pid)
		print "Process Name : (0)".format(process.name)
		print "Proess Status : (0)".format(process.status)
		print "Process Parent id : (0)".format(process.ppid)
		print "Proess creation time : (0)".format(process.creat_time)
		print "Proess Memory info : (0)".format(process.get_memory_info)
		print "Proess opened by process : (0)".format(process.get_opne_files)
