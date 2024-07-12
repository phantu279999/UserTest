import os
import sys
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.base_selenium.setup_driver import setup_chrome


class BaseSelenium:
	def __init__(self):
		self._driver = setup_chrome()

	def get_domain(self, domain):
		self._driver.get(domain)

	def get_title(self):
		return self._driver.title

	def get_current_url(self):
		return self._driver.current_url

	def get_current_url_by_js(self):
		return self._driver.execute_script("return document.URL")

	def get_element_text(self, element):
		return element.text

	def get_page_source(self):
		return self._driver.page_source

	def get_element_attribute(self, element, attribute):
		return element.get_attribute(attribute)

	def close_driver(self):
		self._driver.close()

	def quit_driver(self):
		self._driver.quit()

	def refresh_page(self):
		self._driver.refresh()
		time.sleep(5)

	# ========================== EVENT CLICK ================================
	def click_to_element(self, element):
		element.click()

	def click_to_element_by_script(self, element):
		try:
			self._driver.execute_script("arguments[0].click();", element)
		except:
			raise Exception('You can\'t click to element by script')

	def click_to_element_switch_new_tab(self, element):
		try:
			self._driver.execute_script("$(arguments[0]).click();", element)
			self.switch_to_new_window()
		except:
			raise Exception('You can\'t click to element and switch to new tab')

	def double_click_element(self, element):
		actions = ActionChains(self._driver)
		actions.double_click(element)
		actions.perform()

	# ========================== EVENT INPUT ================================
	def input_to_element(self, element, value):
		element.send_keys(value)

	def input_enter_to_element(self, element, value):
		element.send_keys(value).send_keys(Keys.ENTER)

	def input_to_element_by_script(self, element, value):
		try:
			self._driver.execute_script(f"arguments[0].setAttribute('value', '{value}')", element)
		except:
			raise Exception('Input by js is not sucess. Please try')

	def click_element_input(self, element, value):
		try:
			element.click()
			element.send_keys(value)
		except:
			raise Exception('Click and Input by js is not sucess. Please try')

	def enter_to_element(self, element):
		try:
			element.send_keys(Keys.ENTER)
		except:
			raise Exception('Enter to element by js is not sucess. Please try')

	def double_enter_to_element(self, element):
		try:
			element.send_keys(Keys.ENTER)
			element.send_keys(Keys.ENTER)
		except:
			raise Exception('Double enter to element is failed. Please try')

	def clear_text_in_element(self, element):
		element.clear()

	# ========================== EVENT SWITCH ================================
	def switch_to_iframe(self, element):
		try:
			self._driver.switch_to.frame(element)
		except:
			raise ValueError('You provide is not switch success. please check again')

	def switch_to_new_window(self):
		try:
			self._driver.switch_to.window(self._driver.window_handles[-1])
		except:
			raise ValueError('')

	def switch_to_first_window(self):
		try:
			self._driver.switch_to.window(self._driver.window_handles[0])
		except:
			raise ValueError('')

	def switch_to_next_window(self):
		self._driver.switch_to.window(self._driver.current_window_handle)

	def switch_to_default_content(self):
		try:
			self._driver.switch_to.default_content()
		except:
			raise ValueError('')

	def open_news_window(self, link):
		self._driver.execute_script('window.open("{}","_blank");'.format(link))

	def scroll_to_element(self, element):
		try:
			self._driver.execute_script("arguments[0].scrollIntoView(true);", element)
		except:
			raise ValueError('Có thể bạn không thể di chuyển tới element. Vui lòng kiểm tra lại')

	def move_mouse_to_element(self, element):
		action = webdriver.ActionChains(self._driver)
		action.move_to_element(element)
		action.perform()

	def go_back(self):
		try:
			self._driver.execute_script('window.history.go(-1);')
		except:
			raise ValueError('Lỗi. Có thể bạn chưa trả về trang trước')

	def clear_popup_alert(self):
		try:
			Alert(self._driver).accept()
		except:
			pass

	def get_element(self, locator, locator_type='xpath'):
		if self.check_locator_type(locator_type) is False:
			return False
		try:
			return self._driver.find_element(locator_type, locator)
		except:
			raise AttributeError("You provide locator is not found or error. Please try again")

	def get_list_element(self, locator, locator_type='xpath'):
		if self.check_locator_type(locator_type) is False:
			return False
		try:
			return self._driver.find_elements(locator_type, locator)
		except:
			raise AttributeError("You provide locator is not found or error. Please try again")

	@staticmethod
	def get_path_photo(name_file, prefix):
		return os.path.join(f'/{prefix}', f"{name_file}.png")

	def screenshot(self, name_file, prefix):
		try:
			self._driver.save_screenshot(self.get_path_photo(name_file, prefix))
		except:
			raise Exception("")

	@staticmethod
	def is_element_display(element):
		return element.is_displayed()

	@staticmethod
	def check_locator_type(locator_type):
		locator_type = locator_type.strip().lower()
		if locator_type in ['xpath', 'id', 'name', 'tag_name', 'class_name', 'css_selector', 'link_text']:
			return True
		return False

	@staticmethod
	def sleep(sec):
		time.sleep(sec)
