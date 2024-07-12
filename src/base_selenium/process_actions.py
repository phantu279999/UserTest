import json

from src.base_selenium.base_selenium import BaseSelenium


class ProcessActions(BaseSelenium):

	def __init__(self):
		BaseSelenium.__init__(self)

	def app_run(self):
		data = {}
		with open("config_actions.json", "r") as f:
			data = json.loads(f.read())

		for test_case in data['run']:
			for action in data[test_case]['action']:
				res = self.process_action(action)
				if res is False:
					print("action position {} error")
				if 'time_sleep_action' in data[test_case]:
					self.sleep(data[test_case]['time_sleep_action'])

	def process_action(self, obj):
		if 'type' not in obj:
			return False

		if obj['type'] == 'get_domain':
			self._get_domain(obj)
		elif obj['type'] == 'click':
			self._click(obj)
		elif obj['type'] == 'open_new_tab':
			self._open_new_tab(obj)
		elif obj['type'] == 'input':
			self._input(obj)
		elif obj['type'] == 'input_enter':
			self._input_enter(obj)
		elif obj['type'] == 'enter':
			self._enter(obj)
		elif obj['type'] == 'switch_to_frame':
			self._switch_to_frame(obj)
		elif obj['type'] == 'switch_to_next_tab':
			self._switch_to_next_tab(obj)
		elif obj['type'] == 'switch_to_last_tab':
			self._switch_to_last_tab(obj)
		elif obj['type'] == 'switch_to_first_tab':
			self._switch_to_first_tab(obj)
		elif obj['type'] == 'move':
			self._move(obj)
		elif obj['type'] == 'move_click':
			self._move_click(obj)
		elif obj['type'] == 'drag_and_drop':
			self._drag_and_drop(obj)
		elif obj['type'] == 'clear':
			self._clear(obj)
		elif obj['type'] == 'clear_and_input':
			self._clear_and_input(obj)

	def _get_domain(self, obj):
		if 'value' not in obj:
			return False
		self.get_domain(obj['value'])

	def _open_new_tab(self, obj):
		if 'value' not in obj:
			return False
		self.open_news_window(obj['value'])

	def _click(self, obj):
		if 'locator' not in obj:
			return False
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.click_to_element(element)

	def _input(self, obj):
		if 'locator' not in obj:
			return False
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.input_to_element(element, obj['value'])

	def _input_enter(self, obj):
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.input_enter_to_element(element, obj['value'])

	def _enter(self, obj):
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.enter_to_element(element)

	def _switch_to_frame(self, obj):
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.switch_to_iframe(element)

	def _switch_to_next_tab(self, obj):
		self.switch_to_next_window()

	def _switch_to_last_tab(self, obj):
		self.switch_to_new_window()

	def _switch_to_first_tab(self, obj):
		self.switch_to_first_window()

	def _move(self, obj):
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.move_mouse_to_element(element)

	def _move_click(self, obj):
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.move_mouse_to_element(element)
		self.click_to_element(element)

	def _drag_and_drop(self, obj):
		...

	def _clear(self, obj):
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.clear_text_in_element(element)

	def _clear_and_input(self, obj):
		element = self.get_element(obj['locator'], obj.get('locator_type', 'xpath'))
		self.clear_text_in_element(element)
		self.input_to_element(element, obj['value'])

