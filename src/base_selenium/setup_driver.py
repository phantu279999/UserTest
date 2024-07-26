from selenium import webdriver
import chromedriver_autoinstaller

from src.config import settings
from src.base_selenium.setup_options import set_chrome_options, set_firefox_options

# auto download chromedriver
chromedriver_autoinstaller.install()


def custome_chrome():
	options_chrome = set_chrome_options(
		page_load_strategy=True,
		start_maximized=True,
		disable_extensions=True,
		disable_gpu=True,
		no_sandbox=True,
		disable_dev_shm_usage=True,
		incognito=True,
		disable_background_networking=True,
		disable_notifications=True,
		disable_infobars=True,
		mute_audio=True,
	)

	driver = webdriver.Chrome(options=options_chrome)
	driver.implicitly_wait(settings.IMPLICITLY_WAIT)
	driver.set_page_load_timeout(settings.LOAD_TIME_OUT)

	return driver


def custome_chrome_headless():
	options_chrome = set_chrome_options(
		headless=True,
		ingore_certifi_errors=True,
		ingore_ssl_errors=True,
		start_maximized=True,
		page_load_strategy=True,
		exclude_switches=True,
		disable_extensions=True,
		disable_gpu=True,
		no_sandbox=True,
		disable_dev_shm_usage=True,
		incognito=True,
		disable_background_networking=True,
		disable_notifications=True,
		disable_infobars=True,
		mute_audio=True,
	)

	driver = webdriver.Chrome(options=options_chrome)
	driver.implicitly_wait(settings.IMPLICITLY_WAIT)

	return driver


def custom_version_mobile():
	# mobile_emulation = {
	#     "deviceMetrics": {"width": 640, "height": 640, "pixelRatio": 3.0},
	#     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
	# }
	option = set_chrome_options(
		mobile_emulation=True, start_maximized=True, ingore_certifi_errors=True,
		ingore_ssl_errors=True, exclude_switches=True, page_load_strategy=True
	)
	driver = webdriver.Chrome(options=option)
	driver.implicitly_wait(settings.IMPLICITLY_WAIT)

	return driver


def custom_version_mobile_headless():
	option = set_chrome_options(
		mobile_emulation=True, start_maximized=True, ingore_certifi_errors=True,
		ingore_ssl_errors=True, exclude_switches=True, page_load_strategy=True, headless=True,
	)
	driver = webdriver.Chrome(options=option)
	driver.implicitly_wait(settings.IMPLICITLY_WAIT)

	return driver


def custome_firefox():
	option_firefox = set_firefox_options(
		page_load_strategy=True,
		disable_extensions=True,
		disable_gpu=True,
		no_sandbox=True,
		disable_dev_shm_usage=True,
		incognito=True,
		disable_background_networking=True,
		disable_notifications=True,
		disable_infobars=True,
		mute_audio=True,
	)
	driver = webdriver.Firefox(options=option_firefox)
	driver.maximize_window()

	return driver
