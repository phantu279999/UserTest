import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

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

	def get_element_text(self, element):
		return element.text

	def get_page_source(self):
		return self._driver.page_source

	def get_element_attribute(self, element, attribute):
		return element.get_attribute(attribute)

	def switch_to_iframe(self, element):
		try:
			self._driver.switch_to.frame(element)
		except:
			raise ValueError('Có thể bạn không chuyển được sang iframe. Vui lòng kiểm tra lại')

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

	def switch_to_new_window(self):
		try:
			self._driver.switch_to.window(self._driver.window_handles[-1])
		except:
			raise ValueError('Có thể bạn không chuyển sang cửa sổ mới. Vui lòng kiểm tra lại')

	def get_element(self, xpath, locator='xpath'):
		try:
			return self._driver.find_element(locator, xpath)
		except:
			raise AttributeError('Đường dẫn xpath của bạn có thể sai. Vui lòng kiểm tra lại.')

	def element_is_display(self, element):
		return element.is_displayed()

	def sleep(self, sec):
		time.sleep(sec)