
from src.base_selenium.base_selenium import BaseSelenium


class ProcessActions(BaseSelenium):

	def __init__(self):
		BaseSelenium.__init__(self)

	def process_action(self, obj):
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
		self.get_domain(obj['value'])

	def _open_new_tab(self, obj):
		...

	def _click(self, obj):
		...

	def _input(self, obj):
		...

	def _input_enter(self, obj):
		...

	def _enter(self, obj):
		...

	def _switch_to_frame(self, obj):
		...

	def _switch_to_next_tab(self, obj):
		...

	def _switch_to_last_tab(self, obj):
		...

	def _switch_to_first_tab(self, obj):
		...

	def _move(self, obj):
		...

	def _move_click(self, obj):
		...

	def _drag_and_drop(self, obj):
		...

	def _clear(self, obj):
		...

	def _clear_and_input(self, obj):
		...

