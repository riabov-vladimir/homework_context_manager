from timing_context_manager import Timing_CM
from example_a import txt_to_dict
from  example_a import get_shop_list_by_dishes
import time

with Timing_CM():
	cook_book = txt_to_dict('recipes.txt')
	print(get_shop_list_by_dishes(cook_book))
	# time.sleep(5)  # для проверки времени выполнения