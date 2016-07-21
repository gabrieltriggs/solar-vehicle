from random import randint, uniform

class RandomTelemetry(object):
	"""generates random telemetry kv store"""
	@staticmethod
	def randomKV():

		kv = {}

		kv["PackSOC"] = randint(0, 100)
		kv["AverageTemp"] = randint(0, 124)
		kv["HighTemp"] = randint(0, 124)
		kv["HighThermistor"] = randint(0, 124)
		kv["LowTemp"] = randint(0, 124)
		kv["LowThermistor"] = randint(0, 124)

		kv["PackSumVoltage"] = uniform(110, 145)
		kv["PackInsVoltage"] = uniform(110, 145)
		kv["PackCurrent"] = uniform(-50, 50)
		kv["CA"] = uniform(0, 15)
		kv["CM"] = uniform(-50, 50)
		kv["NC"] = uniform(-50, 70)
		kv["Vaux"] = uniform(15, 28)
		kv["MPH"] = uniform(0, 75)
		kv["RPM"] = uniform(0, 1600)
		kv["PackAmph"] = uniform(0, 32)

		kv["DischargeEnable"] = randint(0, 1)

		return kv

	@staticmethod
	def randomKVLine():

		kv = {}

		kv["PackSOC"] = "%d" % randint(0, 100)
		kv["AverageTemp"] = "%d" % randint(0, 124)
		kv["HighTemp"] = "%d" % randint(0, 124)
		kv["HighThermistor"] = "%d" % randint(0, 124)
		kv["LowTemp"] = "%d" % randint(0, 124)
		kv["LowThermistor"] = "%d" % randint(0, 124)

		kv["PackSumVoltage"] = "%f" % uniform(110, 145)
		kv["PackInsVoltage"] = "%f" % uniform(110, 145)
		kv["PackCurrent"] = "%f" % uniform(-50, 50)
		kv["CA"] = "%f" % uniform(0, 15)
		kv["CM"] = "%f" % uniform(-50, 50)
		kv["NC"] = "%f" % uniform(-50, 70)
		kv["Vaux"] = "%f" % uniform(15, 28)
		kv["MPH"] = "%f" % uniform(0, 75)
		kv["RPM"] = "%f" % uniform(0, 1600)
		kv["PackAmph"] = "%f" % uniform(0, 32)

		kv["DischargeEnable"] = "%d" % randint(0, 1)
		out = '@'
		outList = ["%s=%s" % (k, v) for k, v in kv.items()]
		out += '&'.join(outList) + '@'
		return out