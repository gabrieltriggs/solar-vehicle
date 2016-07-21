## hud.py
##
## Copyright 2016-7-20 Gabriel Triggs

from rt import RandomTelemetry as RT
from hud import Hud
from time import sleep
from Tkinter import TclError
import serial
from log import Logger

def parseLineToKV(line):
	inLine = line[1:].rstrip().rstrip('@')
	varAssignments = inLine.split('&')
	kvLists = map(lambda str: str.split('='), varAssignments)
	kvStrings = {xs[0]: xs[1] for xs in kvLists}

	kv = {}
	kv["PackSOC"] = int(kvStrings["PackSOC"])
	kv["AverageTemp"] = int(kvStrings["AverageTemp"])
	kv["HighTemp"] = int(kvStrings["HighTemp"])
	kv["HighThermistor"] = int(kvStrings["HighThermistor"])
	kv["LowTemp"] = int(kvStrings["LowTemp"])
	kv["LowThermistor"] = int(kvStrings["LowThermistor"])

	kv["PackSumVoltage"] = float(kvStrings["PackSumVoltage"])
	kv["PackInsVoltage"] = float(kvStrings["PackInsVoltage"])
	kv["PackCurrent"] = float(kvStrings["PackCurrent"])
	kv["CA"] = float(kvStrings["CA"])
	kv["CM"] = float(kvStrings["CM"])
	kv["NC"] = float(kvStrings["NC"])
	kv["Vaux"] = float(kvStrings["Vaux"])
	kv["MPH"] = float(kvStrings["MPH"])
	kv["RPM"] = float(kvStrings["RPM"])
	kv["PackAmph"] = float(kvStrings["PackAmph"] )

	kv["DischargeEnable"] = int(kvStrings["DischargeEnable"])

	return kv

def parseLineToStringKV(line):
	inLine = line[1:].rstrip().rstrip('@')
	varAssignments = inLine.split('&')
	kvLists = map(lambda str: str.split('='), varAssignments)
	kv = {xs[0]: xs[1] for xs in kvLists}
	return kv

def strfkv(kv):
	out = ""
	for k, v in kv.items():
		out += (k + ' = ' + v + '\n')
	return out

def main():
	hud = Hud()
	# ser = serial.Serial(port = '/dev/ttyUSB0',
	# 					baudrate = 9600,
	# 					parity = serial.PARITY_NONE,
	# 					stopbits = serial.STOPBITS_ONE,
	# 					bytesize = serial.EIGHTBITS,
	# 					timeout = 1)
	logger = 0
	kv = {}
	stringKV = {}
	firstPass = True

	while True:
		# wrapping this all in a try-catch should handle file-opening/-closing timeline nicely
		# i.e. catch TclError(possibly tclError): close file
		#
		# var parsing and file writing will need to be wrapped in classes
		sleep(0.5)
		#kv = RT.randomKV()
		#print kv
		try:
			#inLine = ser.readline()
			inLine = RT.randomKVLine()
			if inLine[0] == '@':
				newKV = parseLineToKV(inLine)
				newStringKV = parseLineToStringKV(inLine)
				if firstPass:
					keys = sorted(newStringKV.keys())
					logger = Logger(keys)
					firstPass = False

				if newKV != kv:
					kv = newKV
					stringKV = newStringKV
					hud.updateHud(kv)
					hud.update_idletasks()
					hud.update()
					logger.logKV(stringKV)
					print strfkv(stringKV)

		except TclError: #possibly tclError
			print "HUD was closed"
			logger.close()
			break
		except err:
			print err
			break

if __name__ == '__main__':
	main()