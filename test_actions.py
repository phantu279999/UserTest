from src.base_selenium.process_actions import ProcessActions


class TestAction:

	def __init__(self):
		ProcessActions().__init__(self)

	def get_domain(self, domain):
		...

	def open_new_tab(self, domain):
		...

	def click(self, domain):
		...

	def input(self, domain, text):
		...

	def input_enter(self, domain):
		...

	def enter(self, domain):
		...

	def switch_to_frame(self, domain):
		...

	def switch_to_next_tab(self, domain):
		...

	def switch_to_last_tab(self, domain):
		...

	def switch_to_first_tab(self, domain):
		...

	def move(self, domain):
		...

	def move_click(self, domain):
		...

	def drag_and_drop(self, domain):
		...

	def clear(self, domain):
		...

	def clear_and_input(self, domain):
		...

	def assert_title(self, text):
		...

	def test_login(self):
		self.get_domain("http://testphp.vulnweb.com/")
		self.click("//a[@href='login.php']")
		self.input("//input[@name=\"uname\"]", "test")
		self.input("//input[@name=\"pass\"]", "test")
		self.click("//input[@value=\"login\"]")
		return self.assert_title("user info")
