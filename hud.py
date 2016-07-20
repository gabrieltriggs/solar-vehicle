## hud.py
##
## Copyright 2016-7-20 Gabriel Triggs

from Tkinter import *
from random_telemetry import RandomTelemetry as RT

# fooValue is a Tkinter variable string representation of foo
# fooLabel is the non-changing label for foo, e.g. "Current:"
# fooValueLabel is the changing label for foo's value, e.g. "123.4 A"

class Hud:
	def __init__(self):
		self.hudWidth = 1252
		self.hudHeight = 681
		# fonts.google.com -> inconsolata regular and bold
		self.fontName = "Inconsolata"

		self.root = Tk()
		self.root.title("Team Sunergy Solar Vehicle HUD")
		self.centerWindow()
		self.populateHud()

	def centerWindow(self):
		screenWidth = self.root.winfo_screenwidth()
		screenHeight = self.root.winfo_screenheight()
		x = (screenWidth - self.hudWidth) / 2
		y = (screenHeight - self.hudHeight) / 2
		self.root.geometry('%dx%d+%d+%d' % (self.hudWidth, self.hudHeight, x, y))

	def mainloop(self):
		self.root.mainloop()

	def populateHud(self):
		root = self.root
		fontName = self.fontName

		# pack pane
		self.packHeaderLabel = Label(root, text = "Pack", font = (fontName, 36, "bold"))
		self.packHeaderLabel.place(x = 372, y = 47)

		self.chargeLabel = Label(root, text = "Charge:", font = (fontName, 24))
		self.chargeLabel.place(x = 122, y = 137)
		self.chargeValue = StringVar()
		self.chargeValue.set("000%")
		self.chargeValueLabel = Label(root, textvariable = self.chargeValue, font = (fontName, 24))
		self.chargeValueLabel.place(x = 215, y = 137)

		self.ampHoursLabel = Label(root, text = "Amp Hours:", font = (fontName, 24))
		self.ampHoursLabel.place(x = 88, y = 196)
		self.ampHoursValue = StringVar()
		self.ampHoursValue.set("000.0 Ah")
		self.ampHoursValueLabel = Label(root, textvariable = self.ampHoursValue, font = (fontName, 24))
		self.ampHoursValueLabel.place(x = 228, y = 196)

		self.currentLabel = Label(root, text = "Current:", font = (fontName, 24))
		self.currentLabel.place(x = 114, y = 255)
		self.currentValue = StringVar()
		self.currentValue.set("000.0 A")
		self.currentValueLabel = Label(root, textvariable = self.currentValue, font = (fontName, 24))
		self.currentValueLabel.place(x = 215, y = 255)

		self.summedVoltageLabel = Label(root, text = "Summed Voltage:", font = (fontName, 24))
		self.summedVoltageLabel.place(x = 448, y = 137)
		self.summedVoltageValue = StringVar()
		self.summedVoltageValue.set("000.0 V")
		self.summedVoltageValueLabel = Label(root, textvariable = self.summedVoltageValue, font = (fontName, 24))
		self.summedVoltageValueLabel.place(x = 643, y = 137)

		self.instantaneousVoltageLabel = Label(root, text = "Instantaneous Voltage:", font = (fontName, 24))
		self.instantaneousVoltageLabel.place(x = 364, y = 196)
		self.instantaneousVoltageValue = StringVar()
		self.instantaneousVoltageValue.set("000.0 V")
		self.instantaneousVoltageValueLabel = Label(root, textvariable = self.instantaneousVoltageValue, font = (fontName, 24))
		self.instantaneousVoltageValueLabel.place(x = 643, y = 196)

		self.auxPackVoltageLabel = Label(root, text = "Aux Pack Voltage:", font = (fontName, 24))
		self.auxPackVoltageLabel.place(x = 424, y = 255)
		self.auxPackVoltageValue = StringVar()
		self.auxPackVoltageValue.set("000.0 V")
		self.auxPackVoltageValueLabel = Label(root, textvariable = self.auxPackVoltageValue, font = (fontName, 24))
		self.auxPackVoltageValueLabel.place(x = 655, y = 255)

		# temperature pane
		self.temperatureHeaderLabel = Label(root, text = "Temperature", font = (fontName, 36, "bold"))
		self.temperatureHeaderLabel.place(x = 940, y = 47)

		self.packLabel = Label(root, text = "Pack:", font = (fontName, 36))
		self.packLabel.place(x = 875, y = 136)
		self.packAverageTempValue = StringVar()
		self.packAverageTempValue.set("000 F")
		self.packAverageTempValueLabel = Label(root, textvariable = self.packAverageTempValue, font = (fontName, 36))
		self.packAverageTempValueLabel.place(x = 983, y = 136)
		self.packHighTempValue = StringVar()
		self.packHighTempValue.set("000 F")
		self.packHighTempValueLabel = Label(root, textvariable = self.packHighTempValue, font = (fontName, 24), fg = "red")
		self.packHighTempValueLabel.place(x = 1109, y = 130)
		self.packLowTempValue = StringVar()
		self.packLowTempValue.set("000 F")
		self.packLowTempValueLabel = Label(root, textvariable = self.packLowTempValue, font = (fontName, 24), fg = "blue")
		self.packLowTempValueLabel.place(x = 1109, y = 164)

		self.thermistorLabel = Label(root, text = "Thermistor:", font = (fontName, 36))
		self.thermistorLabel.place(x = 875, y = 243)
		self.thermistorHighTempValue = StringVar()
		self.thermistorHighTempValue.set("000 F")
		self.thermistorHighTempValueLabel = Label(root, textvariable = self.thermistorHighTempValue, font = (fontName, 30), fg = "red")
		self.thermistorHighTempValueLabel.place(x = 1094, y = 230)
		self.thermistorLowTempValue = StringVar()
		self.thermistorLowTempValue.set("000 F")
		self.thermistorLowTempValueLabel = Label(root, textvariable = self.thermistorLowTempValue, font = (fontName, 30), fg = "blue")
		self.thermistorLowTempValueLabel.place(x = 1094, y = 271)

		# current pane
		self.currentHeaderLabel = Label(root, text = "Current", font = (fontName, 36, "bold"))
		self.currentHeaderLabel.place(x = 168, y = 397)

		self.arrayLabel = Label(root, text = "Array:", font = (fontName, 24))
		self.arrayLabel.place(x = 151, y = 487)
		self.arrayValue = StringVar()
		self.arrayValue.set("000.0 A")
		self.arrayValueLabel = Label(root, textvariable = self.arrayValue, font = (fontName, 24))
		self.arrayValueLabel.place(x = 243, y = 487)

		self.motorLabel = Label(root, text = "Motor:", font = (fontName, 24))
		self.motorLabel.place(x = 147, y = 546)
		self.motorValue = StringVar()
		self.motorValue.set("000.0 A")
		self.motorValueLabel = Label(root, textvariable = self.motorValue, font = (fontName, 24))
		self.motorValueLabel.place(x = 231, y = 546)

		self.netLabel = Label(root, text = "Net:", font = (fontName, 24))
		self.netLabel.place(x = 171, y = 606)
		self.netValue = StringVar()
		self.netValue.set("000.0 A")
		self.netValueLabel = Label(root, textvariable = self.netValue, font = (fontName, 24))
		self.netValueLabel.place(x = 231, y = 606)

		# miscellany
		self.mphValue = StringVar()
		self.mphValue.set("00.0 MPH")
		self.mphValueLabel = Label(root, textvariable = self.mphValue, font = (fontName, 96))
		self.mphValueLabel.place(x = 434, y = 397)

		self.rpmValue = StringVar()
		self.rpmValue.set("0000.0 RPM")
		self.rpmValueLabel = Label(root, textvariable = self.rpmValue, font = (fontName, 48))
		self.rpmValueLabel.place(x = 506, y = 516)

		self.dischargeLabel = Label(root, text = "Discharge", font = (fontName, 36, "bold"))
		self.dischargeLabel.place(x = 958, y = 397)
		self.enableLabel = Label(root, text = "Enable", font = (fontName, 36, "bold"))
		self.enableLabel.place(x = 985, y = 439)
		self.dischargeEnableValue = StringVar()
		self.dischargeEnableValue.set("OFF")
		self.dischargeEnableValueLabel = Label(root, textvariable = self.dischargeEnableValue, font = (fontName, 36))
		self.dischargeEnableValueLabel.place(x = 1012, y = 513)

	def update(self):
		self.root.update()

	def update_idletasks(self):
		self.root.update_idletasks()

	def updateHud(self, kv):
		#TODO exit immediately if kv is empty

		def celciusToFahrenheit(celcius):
			return int(celcius * 9.0 / 5.0 + 32.0)

		def formatFloat(f):
			# alternative if this isn't supported by python version on raspi
			# return "%.9f" % num
			return "{:.1f}".format(f)

		def formatTemp(t):
			# alternative if this isn't supported by python version on raspi
			# return "%d" % t
			return "{:3d} F".format(t)

		# pack pane
		charge = kv["PackSOC"]
		self.chargeValue.set("{:3d}%".format(charge))
		if charge >= 75:
			self.chargeValueLabel.config(fg = "green")
		elif charge >= 50:
			self.chargeValueLabel.config(fg = "orange")
		else:
			self.chargeValueLabel.config(fg = "red")

		ampHours = kv["PackAmph"]
		self.ampHoursValue.set("{:4.1f} Ah".format(ampHours))
		current = kv["PackCurrent"]
		self.currentValue.set("{: 5.1f} A".format(current))
		summedVoltage = kv["PackSumVoltage"]
		self.summedVoltageValue.set("{:5.1f} V".format(summedVoltage))
		instantaneousVoltage = kv["PackInsVoltage"]
		self.instantaneousVoltageValue.set("{:5.1f} V".format(instantaneousVoltage))
		auxPackVoltage = kv["Vaux"]
		self.auxPackVoltageValue.set("{:4.1f} V".format(auxPackVoltage))

		# temperature pane
		packAverageTemp = celciusToFahrenheit(kv["AverageTemp"])
		self.packAverageTempValue.set(formatTemp(packAverageTemp))
		if packAverageTemp <= 120:
			self.packAverageTempValueLabel.config(fg = "green")
		elif packAverageTemp <= 180:
			self.packAverageTempValueLabel.config(fg = "orange")
		else:
			self.packAverageTempValueLabel.config(fg = "red")
		
		packHighTemp = celciusToFahrenheit(kv["HighTemp"])
		self.packHighTempValue.set(formatTemp(packHighTemp))
		packLowTemp = celciusToFahrenheit(kv["LowTemp"])
		self.packLowTempValue.set(formatTemp(packLowTemp))
		thermistorHighTemp = celciusToFahrenheit(kv["HighThermistor"])
		self.thermistorHighTempValue.set(formatTemp(thermistorHighTemp))
		thermistorLowTemp = celciusToFahrenheit(kv["LowThermistor"])
		self.thermistorLowTempValue.set(formatTemp(thermistorLowTemp))

		# current pane
		array = kv["CA"]
		self.arrayValue.set("{:4.1f} A".format(array))
		motor = kv["CM"]
		self.motorValue.set("{: 5.1f} A".format(motor))
		net = kv["NC"]
		self.netValue.set("{: 5.1f} A".format(net))

		# miscellany
		#TODO: change color based on speed
		mph = kv["MPH"]
		self.mphValue.set("{:4.1f} MPH".format(mph))
		if mph <= 60:
			self.mphValueLabel.config(fg = "green")
		elif mph <= 65:
			self.mphValueLabel.config(fg = "orange")
		else:
			self.mphValueLabel.config(fg = "red")

		rpm = kv["RPM"]
		self.rpmValue.set("{:6.1f} RPM".format(rpm))
		dischargeEnable = kv["DischargeEnable"]
		self.dischargeEnableValue.set("ON" if dischargeEnable else "OFF")

def main():
	hud = Hud()
	hud.mainloop()

if __name__ == '__main__':
	main()