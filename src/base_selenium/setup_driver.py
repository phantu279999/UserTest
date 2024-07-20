from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionFireFox
from selenium import webdriver
from src.config import settings

import chromedriver_autoinstaller

# auto download chromedriver
chromedriver_autoinstaller.install()


def custome_chrome():
	option = Options()
	option.page_load_strategy = settings.PAGE_LOAD_STRATEGY

	driver = webdriver.Chrome(options=option)
	driver.implicitly_wait(settings.IMPLICITLY_WAIT)
	driver.set_page_load_timeout(settings.LOAD_TIME_OUT)
	driver.maximize_window()

	return driver


def custome_chrome_headless():
	options_chrome = Options()
	options_chrome.page_load_strategy = "eager"
	options_chrome.add_argument("--start-maximized")
	options_chrome.add_argument("--headless")
	options_chrome.add_argument('--ignore-certificate-errors')
	options_chrome.add_argument('--ignore-ssl-errors')
	options_chrome.add_experimental_option('excludeSwitches', ['enable-logging'])

	driver = webdriver.Chrome(options=options_chrome)
	driver.implicitly_wait(settings.IMPLICITLY_WAIT)

	return driver


def custom_version_mobile():
	mobile_emulation = {
		"deviceName": settings.NAME_DEVICE_MOBILE
	}
	# mobile_emulation = {
	#     "deviceMetrics": {"width": 640, "height": 640, "pixelRatio": 3.0},
	#     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
	# }
	option = Options()
	option.add_argument("--start-maximized")
	option.add_argument('--ignore-certificate-errors')
	option.add_argument('--ignore-ssl-errors')
	option.add_experimental_option('mobileEmulation', mobile_emulation)
	option.add_experimental_option('excludeSwitches', ['enable-logging'])
	option.page_load_strategy = settings.PAGE_LOAD_STRATEGY
	driver = webdriver.Chrome(options=option)
	driver.implicitly_wait(10)

	return driver


def custom_version_mobile_headless():
	mobile_emulation = {
		"deviceName": settings.NAME_DEVICE_MOBILE
	}
	option = Options()
	option.add_argument("--headless")
	option.add_argument("--start-maximized")
	option.add_argument('--ignore-certificate-errors')
	option.add_argument('--ignore-ssl-errors')
	option.add_experimental_option('mobileEmulation', mobile_emulation)
	option.add_experimental_option('excludeSwitches', ['enable-logging'])
	option.page_load_strategy = settings.PAGE_LOAD_STRATEGY
	driver = webdriver.Chrome(options=option)
	driver.implicitly_wait(10)

	return driver


def custome_firefox():
	option_firefox = OptionFireFox()
	option_firefox.page_load_strategy = settings.PAGE_LOAD_STRATEGY
	# option_firefox.headless = True
	driver = webdriver.Firefox(options=option_firefox)
	driver.maximize_window()

	return driver
