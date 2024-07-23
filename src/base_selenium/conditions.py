from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.config import settings


class Conditions:

	@staticmethod
	def presence_of_element_located(driver, locator, locator_type="xpath"):
		"""
			An element is present in the DOM.
		"""
		try:
			wait = WebDriverWait(driver, settings.IMPLICITLY_WAIT)
			element = wait.until(EC.presence_of_element_located((locator_type, locator)))
			return element
		except Exception as ex:
			print(ex)
		return False

	@staticmethod
	def visibility_of_element_located(driver, locator, locator_type="xpath"):
		"""
			An element is visible.
		"""
		try:
			wait = WebDriverWait(driver, settings.IMPLICITLY_WAIT)
			element = wait.until(EC.visibility_of_element_located((locator_type, locator)))
			return element
		except Exception as ex:
			print(ex)
		return False

	@staticmethod
	def element_to_be_clickable(driver, locator, locator_type="xpath"):
		"""
			An element is visible and enabled.
		"""
		try:
			wait = WebDriverWait(driver, settings.IMPLICITLY_WAIT)
			element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
			return element
		except Exception as ex:
			print(ex)
		return False

	@staticmethod
	def text_to_be_present_in_element(driver, locator, text, locator_type="xpath"):
		"""
			A given text is present in an element.
		"""
		try:
			wait = WebDriverWait(driver, settings.IMPLICITLY_WAIT)
			element = wait.until(EC.text_to_be_present_in_element((locator_type, locator), text))
			return element
		except Exception as ex:
			print(ex)
		return False

	@staticmethod
	def title_is(driver, text):
		"""
			The title matches a given title.
		"""
		try:
			wait = WebDriverWait(driver, settings.IMPLICITLY_WAIT)
			return wait.until(EC.title_is((text)))
		except Exception as ex:
			print(ex)
		return False


	@staticmethod
	def title_contains(driver, text):
		"""
			The title contains a given text.
		"""
		try:
			wait = WebDriverWait(driver, settings.IMPLICITLY_WAIT)
			return wait.until(EC.title_contains((text)))
		except Exception as ex:
			print(ex)
		return False

	@staticmethod
	def alert_is_present(driver):
		"""
			An alert is present.
		"""
		try:
			wait = WebDriverWait(driver, settings.IMPLICITLY_WAIT)
			alert = wait.until(EC.alert_is_present())
			alert.accept()
			return True
		except Exception as ex:
			print(ex)
		return False

