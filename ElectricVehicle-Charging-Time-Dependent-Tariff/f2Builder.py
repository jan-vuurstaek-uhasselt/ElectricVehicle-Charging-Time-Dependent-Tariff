#! /usr/bin/python

import os
import sys

if len(sys.argv) == 2:
	finalPath = ""
	currentPath = os.path.dirname(os.path.abspath(__file__))

	if sys.argv[1].lower() == "windows":
		currentPathWithoutC = currentPath.replace("C:", "")
		finalPath = currentPathWithoutC.replace("\\", "/")
	elif sys.argv[1].lower() == "linux":
		finalPath = currentPath
	else:
		print ("Usage: python f2Builder.py (Windows|Linux)")
		sys.exit(0)

	f2File = finalPath + "/Config/f2.properties"
	
	f = open(f2File, 'w')
	f.write("# Automatically generated by Python\n")
	f.write("f2=" + finalPath + "/Feathers2/\n")
	f.write("config=" + finalPath + "/Config/\n")
	f.write("data=" + finalPath + "/Data/\n")
	f.write("extData=" + finalPath + "/Data/\n")
	f.close()
else:
	print ("Usage: python f2Builder.py (Windows|Linux)")