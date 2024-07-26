import os
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.base_selenium.base_selenium import BaseSelenium


class ProcessActions(BaseSelenium):

	def __init__(self, driver='chrome'):
		BaseSelenium.__init__(self, driver)

	def write_result_to_file(self, result):
		...

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

		for test_case in data['run']:
			print("--------------- Start run |{}| --------------".format(test_case))
			step = 1
			for action in data[test_case]['action']:
				print("------------- Action {} -------------".format(action['name'] if 'name' in action else step))
				res = self.process_action(action)
				result.append({
					"case_test": test_case,
					"status": res['status'],
					"message": res['msg']
				})
				print(res['status'], res['msg'])

				if 'time_sleep_action' in data[test_case]:
					self.sleep(data[test_case]['time_sleep_action'])
				if 'sleep' in action:
					self.sleep(action['sleep'])
				step += 1

		self.write_result_to_file(result)
		return result

	def process_action(self, obj):
		if 'type' not in obj:
			return {
				'status': False,
				"msg": "Not found 'type' in action"
			}

		if obj['type'] == 'get_domain':
			return self._get_domain(obj)
		elif obj['type'] == 'click':
			return self._click(obj)
		elif obj['type'] == 'open_new_tab':
			return self._open_new_tab(obj)
		elif obj['type'] == 'input':
			return self._input(obj)
		elif obj['type'] == 'input_enter':
			return self._input_enter(obj)
		elif obj['type'] == 'enter':
			return self._enter(obj)
		elif obj['type'] == 'switch_to_frame':
			return self._switch_to_frame(obj)
		elif obj['type'] == 'switch_to_next_tab':
			return self._switch_to_next_tab(obj)
		elif obj['type'] == 'switch_to_last_tab':
			return self._switch_to_last_tab(obj)
		elif obj['type'] == 'switch_to_first_tab':
			return self._switch_to_first_tab(obj)
		elif obj['type'] == 'move':
			return self._move(obj)
		elif obj['type'] == 'move_click':
			return self._move_click(obj)
		elif obj['type'] == 'drag_and_drop':
			return self._drag_and_drop(obj)
		elif obj['type'] == 'clear':
			return self._clear(obj)
		elif obj['type'] == 'clear_and_input':
			return self._clear_and_input(obj)

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
