from random import randint, uniform

class RandomTelemetry(object):
	"""generates random telemetry kv store"""
	@staticmethod
	def randomKV():

		bool_keys = ["DischargeEnable"]

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