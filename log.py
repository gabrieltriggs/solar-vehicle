from datetime import datetime

class Logger():
	def __init__(self, keys):
		filename = datetime.now().strftime("logs/%Y-%m-%d@%H-%M-%S.csv")
		self.file = open(filename, 'a')
		self.sortedKeys = sorted(keys)
		headers = ','.join(self.sortedKeys)
		self.file.write(headers + '\n')

	def close(self):
		self.file.close()

	def logKV(self, kv):
		values = []
		for key in self.sortedKeys:
			values.append(kv[key])
		outLine = ','.join(values)
		self.file.write(outLine + '\n')