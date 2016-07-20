## hud.py
##
## Copyright 2016-7-20 Gabriel Triggs

from random_telemetry import RandomTelemetry as RT
from hud import Hud
from time import sleep
from Tkinter import TclError

def main():
	hud = Hud()

	while True:
		# wrapping this all in a try-catch should handle file-opening/-closing timeline nicely
		# i.e. catch TclError(possibly tclError): close file
		#
		# var parsing and file writing will need to be wrapped in classes
		sleep(0.5)
		kv = RT.randomKV()
		print kv
		try:
			hud.updateHud(kv)
			hud.update_idletasks()
			hud.update()
		except TclError: #possibly tclError
			print "HUD was closed"
			break

if __name__ == '__main__':
	main()