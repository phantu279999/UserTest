from src.config import settings

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionFireFox

"""
Headless Mode:

options.add_argument("--headless")
Runs the browser in headless mode (without a GUI).
Window Size and Position:

options.add_argument("--start-maximized")
Maximizes the browser window.
options.add_argument("--window-size=1920,1080")
Sets the window size to 1920x1080 pixels.
options.add_argument("--window-position=0,0")
Sets the window position.
Security and Certificates:

options.add_argument('--ignore-certificate-errors')
Ignores certificate errors.
options.add_argument('--ignore-ssl-errors')
Ignores SSL errors.
options.add_argument('--disable-web-security')
Disables web security.
User Agent:

options.add_argument('user-agent=Your User Agent Here')
Sets a custom user agent.
Proxy Settings:

options.add_argument('--proxy-server=your-proxy-server')
Sets a proxy server.
Performance and Debugging:

options.add_argument('--disable-gpu')
Disables GPU hardware acceleration.
options.add_argument('--disable-extensions')
Disables extensions.
options.add_argument('--disable-popup-blocking')
Disables popup blocking.
options.add_argument('--disable-infobars')
Disables the infobar that shows "Chrome is being controlled by automated test software".
options.add_argument('--remote-debugging-port=9222')
Enables remote debugging on the specified port.
Performance Tweaks:

options.add_argument('--no-sandbox')
Disables the sandbox mode (often required for running in Docker).
options.add_argument('--disable-dev-shm-usage')
Overcomes limited resource problems.
Browser Preferences:

options.add_argument('--incognito')
Opens the browser in incognito mode.
options.add_argument('--disable-blink-features=AutomationControlled')
Disables the "automation controlled" feature.
Miscellaneous:

options.add_argument('--disable-software-rasterizer')
Disables software rasterizer.
options.add_argument('--no-proxy-server')
Disables proxy settings.
options.add_argument('--allow-running-insecure-content')
Allows running insecure content.
options.add_argument('--disable-logging')
Disables logging.
options.add_argument('--log-level=3')
Sets the logging level (3 is for severe only)."""

def set_chrome_options(
		headless=False,
		page_load_strategy=False,
		start_screen_max=False,
		ingore_certifi_errors=False,
		ingore_ssl_errors=False,
		disable_web_security=False,
		user_agent=False,
		proxy_server=False,
		disable_gpu=False,
		disable_extensions=False,
		disable_popup_blocking=False,
		disable_infobars=False,
		remote_debugging_port=False,
		no_sandbox=False,
		disable_dev_shm_usage=False,
		incognito=False,
		disable_blink_features=False,
		disable_software_rasterizer=False,
		no_proxy_server=False,
		allow_running_insecure_content=False,
		disable_logging=False,
		log_level=False,
		mobile_emulation=False,
		exclude_switches=False,
):
	options = Options()
	if headless is True:
		options.add_argument("--headless")
	if page_load_strategy is True:
		options.page_load_strategy = settings.PAGE_LOAD_STRATEGY
	if start_screen_max is True:
		options.add_argument("--start-maximized")
	if ingore_certifi_errors is True:
		# Ignores certificate errors.
		options.add_argument("--ignore-certificate-errors")
	if ingore_ssl_errors is True:
		# Ignores SSL errors.
		options.add_argument('--ignore-ssl-errors')
	if disable_web_security is True:
		# Disables web security.
		options.add_argument('--disable-web-security')

	if user_agent:
		# Sets a custom user agent.
		options.add_argument('user-agent={}'.format(user_agent))

	if proxy_server:
		# Sets a proxy server.
		options.add_argument('--proxy-server={}'.format(proxy_server))

	if disable_gpu is True:
		# Disables GPU hardware acceleration.
		options.add_argument('--disable-gpu')

	if disable_extensions:
		# Disables extensions.
		options.add_argument('--disable-extensions')
	if disable_popup_blocking is True:
		# Disables popup blocking.
		options.add_argument('--disable-popup-blocking')
	if disable_infobars is True:
		# Disables the infobar that shows "Chrome is being controlled by automated test software".
		options.add_argument('--disable-infobars')
	if remote_debugging_port:
		# Enables remote debugging on the specified port.
		options.add_argument('--remote-debugging-port={}'.format(remote_debugging_port))
	if no_sandbox:
		# Disables the sandbox mode (often required for running in Docker).
		options.add_argument('--no-sandbox')
	if disable_dev_shm_usage is True:
		# Overcomes limited resource problems.
		options.add_argument('--disable-dev-shm-usage')

	# ====================== Browser Preferences ======================
	if incognito:
		# Opens the browser in incognito mode.
		options.add_argument('--incognito')
	if disable_blink_features:
		# Disables the "automation controlled" feature.
		options.add_argument('--disable-blink-features={}'.format(settings.DISABLE_BLICK_FEATURES))

	# ====================== Miscellaneous ======================
	if disable_software_rasterizer:
		# Disables software rasterizer.
		options.add_argument('--disable-software-rasterizer')
	if no_proxy_server:
		# Disables proxy settings.
		options.add_argument('--no-proxy-server')

	if allow_running_insecure_content:
		# Allows running insecure content.
		options.add_argument('--allow-running-insecure-content')

	if disable_logging:
		# Disables logging.
		options.add_argument('--disable-logging')
	if log_level:
		# Sets the logging level (3 is for severe only).
		options.add_argument('--log-level={}'.format(settings.LOG_LEVEL))

	if mobile_emulation:
		mobile_emulation = {
			"deviceName": settings.NAME_DEVICE_MOBILE
		}
		options.add_experimental_option('mobileEmulation', mobile_emulation)

	if exclude_switches is True:
		options.add_experimental_option('excludeSwitches', ['enable-logging'])

	return options


def set_firefox_options(
	headless=False,
	page_load_strategy=False,
):
	options = OptionFireFox()
	if headless:
		options.headless = True
	if page_load_strategy:
		options.page_load_strategy = settings.PAGE_LOAD_STRATEGY
	return options
