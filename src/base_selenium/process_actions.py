
from src.base_selenium.base_selenium import BaseSelenium


class ProcessActions(BaseSelenium):

	def __init__(self):
		BaseSelenium.__init__(self)

	def _get_domain(self):
		...

	def _open_new_tab(self):
		...

	def _click(self):
		...

	def _input(self):
		...

	def _input_enter(self):
		...

	def _enter(self):
		...

	def _switch_to_frame(self):
		...

	def _switch_to_next_tab(self):
		...

	def _switch_to_last_tab(self):
		...

	def _switch_to_first_tab(self):
		...

	def _move(self):
		...

	def _move_click(self):
		...

	def _drag_and_drop(self):
		...

	def _clear(self):
		...

	def _clear_and_input(self):
		...

