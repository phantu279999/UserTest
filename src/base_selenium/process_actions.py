import os
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.common.base_log import BaseLogger
from src.base_selenium.base_selenium import BaseSelenium


def with_result_check(func):
	def wrapper(self, obj):
		try:
			status = func(self, obj)
			return self.check_result.process_result(obj)
		except Exception as e:
			return {'status': False, 'msg': str(e)}
	return wrapper


class ProcessActions(BaseSelenium):

	def __init__(self, driver='chrome'):
		BaseSelenium.__init__(self, driver)
		self.logger = BaseLogger('test_case', log_file='log\\test_case.log')

		self.action_map = {
			'get_domain': self._get_domain,
			'click': self._click,
			'open_new_tab': self._open_new_tab,
			'input': self._input,
			'input_enter': self._input_enter,
			'enter': self._enter,
			'switch_to_frame': self._switch_to_frame,
			'switch_to_next_tab': self._switch_to_next_tab,
			'switch_to_last_tab': self._switch_to_last_tab,
			'switch_to_first_tab': self._switch_to_first_tab,
			'move': self._move,
			'move_click': self._move_click,
			'drag_and_drop': self._drag_and_drop,
			'clear': self._clear,
			'clear_and_input': self._clear_and_input
		}

	def write_result_to_file(self, result):
		with open('log/result_case_test.csv', 'w') as write_file:
			write_file.write("Case Test,Name Step,Status,Message\n")
			for row in result:
				write_file.write("{},{},{},{}\n".format(
					row['case_test'], row['name_step'], row['status'], row['message'])
				)

	@staticmethod
	def open_file_test_cases():
		data = {}
		try:
			with open("config_actions.json", "r") as f:
				data = json.loads(f.read())
			return data
		except json.decoder.JSONDecodeError as e:
			print(f"Error decoding JSON: {e}")
			return data
		except Exception as e:
			print("Error: {}".format(e))
			return data

	def app_run(self):
		result = []
		data = self.open_file_test_cases()

		if not data:
			print("Can't read the file .json. Please check again")
			return

		if 'run' not in data:
			print("Missing 'run' key in config_actions.json")
			return

		for test_case in data['run']:
			print("--------------- Start run |{}| --------------".format(test_case))
			step = 1
			for action in data[test_case]['action']:
				name_step = "Action {}".format(
					action['name'] if 'name' in action else step
				)
				res = self.process_action(action)
				result.append({
					"case_test": test_case,
					"name_step": name_step,
					"status": res['status'],
					"message": res['msg']
				})
				print(name_step, res['status'], res['msg'])
				if 'time_sleep_action' in data[test_case]:
					self.sleep(data[test_case]['time_sleep_action'])
				if 'sleep' in action:
					self.sleep(action['sleep'])

				if res['status']:
					self.logger.info(f"[{test_case}] Step: {name_step} - PASS: {res['msg']}")
				else:
					self.logger.error(f"[{test_case}] Step: {name_step} - FAIL: {res['msg']}")
				# self.logger.info((name_step, res['status'], res['msg']))
				step += 1

		self.write_result_to_file(result)
		return result

	def process_action(self, obj):
		if 'type' not in obj:
			return {
				'status': False,
				"msg": "Not found 'type' in action"
			}

		action_func = self.action_map.get(obj['type'])

		if not action_func:
			return {'status': False, 'msg': f"Action type '{obj['type']}' is not supported"}

		return action_func(obj)


	def _get_domain(self, obj):
		if 'value' not in obj:
			return {
				"status": False,
				"msg": "GET DOMAIN: Not found \'value\' in action"
			}
		self.get_domain(obj['value'])

		return self.check_result.process_result(obj)

	def _open_new_tab(self, obj):
		if 'value' not in obj:
			return {
				"status": False,
				"msg": "OPEN NEW TAB: Not found \'value\' in action"
			}
		self.open_news_window(obj['value'])

		return self.check_result.process_result(obj)

	def _click(self, obj):
		if 'locator' not in obj:
			return {
				"status": False,
				"msg": "CLICK: Not found \'locator\' in action"
			}
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.click_to_element(element)

		return self.check_result.process_result(obj)

	def _input(self, obj):
		if 'locator' not in obj:
			return {
				"status": False,
				"msg": "INPUT: Not found \'locator\' in action"
			}
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.input_to_element(element, obj['value'])

		return self.check_result.process_result(obj)

	def _input_enter(self, obj):
		if 'locator' not in obj:
			return {
				"status": False,
				"msg": "INPUT ENTER: Not found \'locator\' in action"
			}
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.input_enter_to_element(element, obj['value'])

		return self.check_result.process_result(obj)

	def _enter(self, obj):
		if 'locator' not in obj:
			return {
				"status": False,
				"msg": "ENTER: Not found \'locator\' in action"
			}
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.enter_to_element(element)

		return self.check_result.process_result(obj)

	def _switch_to_frame(self, obj):
		if 'locator' not in obj:
			return {
				"status": False,
				"msg": "SWITCH TO FRAME: Not found \'locator\' in action"
			}
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.switch_to_iframe(element)

		return self.check_result.process_result(obj)

	def _switch_to_next_tab(self, obj):
		self.go_forward()

		return self.check_result.process_result(obj)

	def _switch_to_last_tab(self, obj):
		self.switch_to_new_window()

		return self.check_result.process_result(obj)

	def _switch_to_first_tab(self, obj):
		self.switch_to_first_window()

		return self.check_result.process_result(obj)

	def _move(self, obj):
		if 'locator' not in obj:
			return {
				"status": False,
				"msg": "MOVE: Not found \'locator\' in action"
			}
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.move_mouse_to_element(element)

		return self.check_result.process_result(obj)

	def _move_click(self, obj):
		if 'locator' not in obj:
			return {
				"status": False,
				"msg": "MOVE CLICK: Not found \'locator\' in action"
			}
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.move_mouse_to_element(element)
		self.click_to_element(element)

		return self.check_result.process_result(obj)

	def _drag_and_drop(self, obj):
		if ('locator' not in obj) or ('locator_2' not in obj):
			return {
				"status": False,
				"msg": "CLEAR: Not found \'locator\' or 'locator_2' in action"
			}
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		element_2 = self.get_element(obj['locator_2'], obj.get('locator_type_2', 'xpath'))
		self.drag_and_drop_from_element1_to_element2(element, element_2)
		return self.check_result.process_result(obj)

	def _clear(self, obj):
		if 'locator' not in obj:
			return {
				"status": False,
				"msg": "CLEAR: Not found \'locator\' in action"
			}
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.clear_text_in_element(element)

		return self.check_result.process_result(obj)

	def _clear_and_input(self, obj):
		if 'locator' not in obj or 'value' not in obj:
			return {
				"status": False,
				"msg": "CLEAR AND INPUT: Not found \'locator\' or \'value\' in action"
			}
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.clear_text_in_element(element)
		self.input_to_element(element, obj['value'])

		return self.check_result.process_result(obj)
