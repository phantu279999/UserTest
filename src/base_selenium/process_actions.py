import os
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.base_selenium.base_selenium import BaseSelenium


class ProcessActions(BaseSelenium):

	def __init__(self):
		BaseSelenium.__init__(self)

	def app_run(self):
		data = {}
		with open("config_actions.json", "r") as f:
			data = json.loads(f.read())
		if not data:
			print("Can't read the file .json. Please try again")
			return

		for test_case in data['run']:
			print("--------------- Start run |{}| --------------".format(test_case))
			step = 1
			for action in data[test_case]['action']:
				print("------------- Action {} -------------".format(step))
				res = self.process_action(action)
				if res is False:
					print("action position {} error")
				if res:
					print(res['status'], res['msg'])
				if 'time_sleep_action' in data[test_case]:
					self.sleep(data[test_case]['time_sleep_action'])
				step += 1

	def process_action(self, obj):
		if 'type' not in obj:
			return False

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
			return False
		self.get_domain(obj['value'])

		return self.process_result(obj)

	def _open_new_tab(self, obj):
		if 'value' not in obj:
			return False
		self.open_news_window(obj['value'])

		return self.process_result(obj)

	def _click(self, obj):
		if 'locator' not in obj:
			return False
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.click_to_element(element)

		return self.process_result(obj)

	def _input(self, obj):
		if 'locator' not in obj:
			return False
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.input_to_element(element, obj['value'])

		return self.process_result(obj)

	def _input_enter(self, obj):
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.input_enter_to_element(element, obj['value'])

		return self.process_result(obj)

	def _enter(self, obj):
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.enter_to_element(element)

		return self.process_result(obj)

	def _switch_to_frame(self, obj):
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.switch_to_iframe(element)

		return self.process_result(obj)

	def _switch_to_next_tab(self, obj):
		self.switch_to_next_window()

		return self.process_result(obj)

	def _switch_to_last_tab(self, obj):
		self.switch_to_new_window()

		return self.process_result(obj)

	def _switch_to_first_tab(self, obj):
		self.switch_to_first_window()

		return self.process_result(obj)

	def _move(self, obj):
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.move_mouse_to_element(element)

		return self.process_result(obj)

	def _move_click(self, obj):
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.move_mouse_to_element(element)
		self.click_to_element(element)

		return self.process_result(obj)

	def _drag_and_drop(self, obj):


		return self.process_result(obj)

	def _clear(self, obj):
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.clear_text_in_element(element)

		return self.process_result(obj)

	def _clear_and_input(self, obj):
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.clear_text_in_element(element)
		self.input_to_element(element, obj['value'])

		return self.process_result(obj)

	def process_result(self, obj):
		res = {}
		if 'result' not in obj:
			return None
		self.clear_popup_alert()
		if 'type' not in obj['result']:
			res['status'] = False
			res['msg'] = "Not found \'type\' in result"
		elif obj['result']['type'] == 'title':
			status, msg = self.process_result_title(obj)
			res['status'] = status
			res['msg'] = msg
		elif obj['result']['type'] == 'xpath':
			status, msg = self.process_result_xpath(obj)
			res['status'] = status
			res['msg'] = msg
		elif obj['result']['type'] == 'display':
			status, msg = self.process_result_display(obj)
			res['status'] = status
			res['msg'] = msg
		elif obj['result']['type'] == 'xpath_text':
			status, msg = self.process_result_xpath_text(obj)
			res['status'] = status
			res['msg'] = msg
		else:
			res['status'] = False
			res['msg'] = "Not found \'type\' in result"
		return res

	def process_result_title(self, obj):
		if 'value' not in obj['result']:
			status = False
			msg = '(title)Not found \'value\'Check result need two fields: type, value'
		else:
			current_title = self.get_title()
			desired_title = obj['result']['value']
			if current_title.strip() == desired_title.strip():
				status = True
				msg = "(title)Passed"
			else:
				status = False
				msg = '(title)You provide title is not equal with current page title'

		return status, msg

	def process_result_xpath(self, obj):
		if 'xpath' not in obj['result']:
			status = False
			msg = '(xpath)Not found \'xpath\'Check result need two fields: type, xpath'
		else:
			element = self.get_element(obj['result']['xpath'])
			if element:
				status = True
				msg = "(xpath)Passed"
			else:
				status = False
				msg = '(xpath)You provide xpath not found in current page. Please check again'

		return status, msg

	def process_result_display(self, obj):
		if 'xpath' not in obj['result']:
			status = False
			msg = '(display)Not found \'xpath\'Check result need two fields: type, xpath'
		else:
			element = self.get_element(obj['result']['xpath'])
			if element:
				if self.is_element_display(element):
					status = True
					msg = "(display)Passed"
				else:
					status = False
					msg = '(display)You provide xpath not display in current page. Please check again'
			else:
				status = False
				msg = '(display)You provide xpath not found in current page. Please check again'

		return status, msg

	def process_result_xpath_text(self, obj):
		if ('xpath' not in obj['result']) or ('value' not in obj['result']):
			status = False
			msg = '(xpath_text)Not found \'xpath\' or \'value\' Check result need two fields: type, xpath, value'
		else:
			element = self.get_element(obj['result']['xpath'])
			if element:
				xpath_text = self.get_element_text(element)
				disired_text = obj['result']['value']
				if xpath_text.strip() == disired_text.strip():
					status = True
					msg = "(xpath_text)Passed"
				else:
					status = False
					msg = '(xpath_text)You provide text is not equal with xpath text'
			else:
				status = False
				msg = '(xpath_text)You provide xpath not found in current page. Please check again'
		return status, msg
