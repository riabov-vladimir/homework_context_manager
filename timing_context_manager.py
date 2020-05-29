import datetime
import time


class Timing_CM:

	def __enter__(self):
		self.time_in = datetime.datetime.utcnow()
	# присваиваю переменной self.time_in время входа в блок контектстного менеджера

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.time_out = datetime.datetime.utcnow()
		# присваиваю переменной self.time_out время выхода из блока контектстного менеджера
		self.time_delta = self.time_out - self.time_in # длительность выполнения кода
		print(f'Начало выполнения кода - {self.time_in}')
		print(f'Конец выполнения кода - {self.time_out}')
		print(f'Длительность выполнения кода - {self.time_delta}')
		if exc_val is not None:
			print('finished with error', str(exc_val))


# with Timing_CM():
# 	time.sleep(3)
