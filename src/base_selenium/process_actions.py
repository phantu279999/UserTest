
from base_selenium import BaseSelenium


class ProcessActions(BaseSelenium):

	def __init__(self):
		BaseSelenium.__init__(self)

		self.list_action_functions = {
			"get_domain": self.get_domain,
			"open_new_tab": self.open_new_tab,
			"click": self.click,
			"input": self.input,
			"input_enter": self.input_enter,
			"enter": self.enter,
			"switch_to_frame": self.switch_to_frame,
			"switch_to_next_tab": self.switch_to_next_tab,
			"switch_to_last_tab": self.switch_to_last_tab,
			"switch_to_first_tab": self.switch_to_first_tab,
			"move_to_element": self.move_element,
			"move_to_element_click": self.move_to_element_click,
			"drag_and_drop_element": self.drag_and_drop_element,
			"clear": self.clear_data_element,
			"clear_and_input": self.clear_and_input_element
		}

		self.list_result_functions = {
			"title": self.check_title,
			"xpath": self.check_xpath,
			"display": self.check_text_display,
			"xpath_text": self.check_text_xpath
		}