from src.config import settings

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionFireFox


def set_chrome_options(
		start_maximized=False,  # User Interface and Experience
		window_size=False,
		dark_mode=False,
		incognito=False,
		disable_save_password_bubble=False,
		disable_single_click_autofill=False,
		disable_translate=False,
		disable_prompt_on_repost=False,
		ingore_certifi_errors=False,  # Security and Privacy
		ingore_ssl_errors=False,
		disable_web_security=False,
		safebrowsing_disable_download_protection=False,
		disable_gpu=False,  # Performance and Debugging
		disable_extensions=False,
		disable_popup_blocking=False,
		disable_infobars=False,
		remote_debugging_port=False,
		disable_browser_side_navigation=False,
		allow_file_access_from_files=False,  # File and Network Handling
		dns_prefetch_disable=False,
		user_agent=False,  # Miscellaneous
		proxy_server=False,
		page_load_strategy=False,
		headless=False,
		no_sandbox=False,
		disable_dev_shm_usage=False,
		disable_blink_features=False,
		disable_software_rasterizer=False,
		no_proxy_server=False,
		allow_running_insecure_content=False,
		disable_logging=False,
		log_level=False,
		mobile_emulation=False,
		exclude_switches=False,
		disable_3d_apis=False,
		disable_renderer_backgrounding=False,
		disable_background_networking=False,
		disable_notifications=False,
		mute_audio=False,
		disable_features=False,
):
	options = Options()

	if start_maximized is True:
		options.add_argument("--start-maximized")
	if window_size:
		options.add_argument("--window-size={},{}".format(settings.WINDOW_SIZE[0], settings.WINDOW_SIZE[1]))
	if dark_mode:
		options.add_argument("--enable-features=WebContentsForceDark")
	if incognito:
		# Opens the browser in incognito mode.
		options.add_argument('--incognito')
	if disable_save_password_bubble:
		options.add_argument("--disable-save-password-bubble")
	if disable_single_click_autofill:
		# Disables single click autofill.
		options.add_argument("--disable-single-click-autofill")
	if disable_translate:
		# Disables the translate prompt.
		options.add_argument("--disable-translate")
	if disable_prompt_on_repost:
		# Disables the prompt on form resubmission.
		options.add_argument("--disable-prompt-on-repost")

	if ingore_certifi_errors is True:
		# Ignores certificate errors.
		options.add_argument("--ignore-certificate-errors")
	if ingore_ssl_errors is True:
		# Ignores SSL errors.
		options.add_argument('--ignore-ssl-errors')
	if disable_web_security is True:
		# Disables web security.
		options.add_argument('--disable-web-security')
	if safebrowsing_disable_download_protection:
		options.add_argument("--safebrowsing-disable-download-protection")

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
		options.add_argument('--remote-debugging-port={}'.format(settings.REMOTE_DEBUGGING_PORT))
	if disable_browser_side_navigation:
		options.add_argument("--disable-browser-side-navigation")

	if allow_file_access_from_files:
		options.add_argument("--allow-file-access-from-files")
	if dns_prefetch_disable:
		options.add_argument("--dns-prefetch-disable")

	if headless is True:
		options.add_argument("--headless")
	if page_load_strategy is True:
		options.page_load_strategy = settings.PAGE_LOAD_STRATEGY
	if user_agent:
		# Sets a custom user agent.
		from fake_useragent import UserAgent
		ua = UserAgent()
		options.add_argument('user-agent={}'.format(ua.random))
	if proxy_server:
		# Sets a proxy server.
		options.add_argument('--proxy-server={}'.format(settings.PROXY_SERVER))
	if no_sandbox:
		# Disables the sandbox mode (often required for running in Docker).
		options.add_argument('--no-sandbox')
	if disable_dev_shm_usage is True:
		# Overcomes limited resource problems.
		options.add_argument('--disable-dev-shm-usage')
	if disable_blink_features:
		# Disables the "automation controlled" feature.
		options.add_argument('--disable-blink-features={}'.format(settings.DISABLE_BLICK_FEATURES))
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
	if disable_3d_apis:
		options.add_argument("--disable-3d-apis")
	if disable_renderer_backgrounding:
		options.add_argument("--disable-renderer-backgrounding")
	if disable_background_networking:
		options.add_argument("--disable-background-networking")
	if disable_notifications:
		options.add_argument("--disable-notifications")
	if mute_audio:
		options.add_argument("--mute-audio")
	if disable_features:
		options.add_argument("--disable-features=%s" % ",".join(settings.DISABLE_FEATURES))

	# options.add_argument("--safebrowsing-disable-download-protection")
	# options.add_argument("--disable-browser-side-navigation")
	# options.add_argument("--disable-save-password-bubble")
	# options.add_argument("--disable-single-click-autofill")
	# options.add_argument("--allow-file-access-from-files")
	# options.add_argument("--disable-prompt-on-repost")
	# options.add_argument("--dns-prefetch-disable")
	# options.add_argument("--disable-translate")
	# options.add_argument("--disable-backgrounding-occluded-windows")
	# options.add_argument("--disable-client-side-phishing-detection")
	# options.add_argument("--disable-oopr-debug-crash-dump")
	# options.add_argument("--disable-top-sites")
	# options.add_argument("--ash-no-nudges")
	# options.add_argument("--no-crash-upload")
	# options.add_argument("--deny-permission-prompts")
	# options.add_argument(
	# 	'--simulate-outdated-no-au="Tue, 03 Oct 2055 00:00:00 GMT"'
	# )
	# options.add_argument("--disable-ipc-flooding-protection")
	# options.add_argument("--disable-password-generation")
	# options.add_argument("--disable-domain-reliability")
	# options.add_argument("--disable-component-update")
	# options.add_argument("--disable-breakpad")
	# options.add_argument("--test-type")
	# options.add_argument("--no-first-run")
	# options.add_argument("--allow-insecure-localhost")
	# options.add_argument(
	# 	"--disable-autofill-keyboard-accessory-view[8]"
	# )
	# options.add_argument("--homepage=about:blank")
	# options.add_argument("--dom-automation")
	# options.add_argument("--disable-hang-monitor")


	return options


def set_firefox_options(
	headless=False,
	page_load_strategy=False,
	window_size=False, # User Interface and Experience
	incognito=False,
	disable_save_password_bubble=False,
	disable_single_click_autofill=False,
	disable_translate=False,
	disable_prompt_on_repost=False,
	ignore_certifi_errors=False,  # Security and Privacy
	ignore_ssl_errors=False,
	disable_web_security=False,
	safebrowsing_disable_download_protection=False,
	disable_gpu=False,  # Performance and Debugging
	disable_extensions=False,
	disable_popup_blocking=False,
	disable_infobars=False,
	remote_debugging_port=False,
	disable_browser_side_navigation=False,
	allow_file_access_from_files=False,  # File and Network Handling
	dns_prefetch_disable=False,
	user_agent=False,  # Miscellaneous
	proxy_server=False,
	no_sandbox=False,
	disable_dev_shm_usage=False,
	disable_blink_features=False,
	disable_software_rasterizer=False,
	no_proxy_server=False,
	allow_running_insecure_content=False,
	disable_logging=False,
	log_level=False,
	disable_3d_apis=False,
	disable_renderer_backgrounding=False,
	disable_background_networking=False,
	disable_notifications=False,
	mute_audio=False,
	disable_features=False,
):
	options = OptionFireFox()

	if headless:
		options.headless = True
	if page_load_strategy:
		options.page_load_strategy = settings.PAGE_LOAD_STRATEGY
	if window_size:
		options.add_argument("--width={}".format(settings.WINDOW_SIZE[0]))
		options.add_argument("--height={}".format(settings.WINDOW_SIZE[1]))
	if incognito:
		options.add_argument('--incognito')
	if disable_save_password_bubble:
		options.add_argument("--disable-save-password-bubble")
	if disable_single_click_autofill:
		options.add_argument("--disable-single-click-autofill")
	if disable_translate:
		options.add_argument("--disable-translate")
	if disable_prompt_on_repost:
		options.add_argument("--disable-prompt-on-repost")
	if ignore_certifi_errors:
		options.add_argument("--ignore-certificate-errors")
	if ignore_ssl_errors:
		options.add_argument('--ignore-ssl-errors')
	if disable_web_security:
		options.add_argument('--disable-web-security')
	if safebrowsing_disable_download_protection:
		options.add_argument("--safebrowsing-disable-download-protection")
	if disable_gpu:
		options.add_argument('--disable-gpu')
	if disable_extensions:
		options.add_argument('--disable-extensions')
	if disable_popup_blocking:
		options.add_argument('--disable-popup-blocking')
	if disable_infobars:
		options.add_argument('--disable-infobars')
	if remote_debugging_port:
		options.add_argument('--remote-debugging-port={}'.format(settings.REMOTE_DEBUGGING_PORT))
	if disable_browser_side_navigation:
		options.add_argument("--disable-browser-side-navigation")
	if allow_file_access_from_files:
		options.add_argument("--allow-file-access-from-files")
	if dns_prefetch_disable:
		options.add_argument("--dns-prefetch-disable")
	if user_agent:
		from fake_useragent import UserAgent
		ua = UserAgent()
		options.add_argument('user-agent={}'.format(ua.random))
	if proxy_server:
		options.add_argument('--proxy-server={}'.format(settings.PROXY_SERVER))
	if no_sandbox:
		options.add_argument('--no-sandbox')
	if disable_dev_shm_usage:
		options.add_argument('--disable-dev-shm-usage')
	if disable_blink_features:
		options.add_argument('--disable-blink-features={}'.format(settings.DISABLE_BLICK_FEATURES))
	if disable_software_rasterizer:
		options.add_argument('--disable-software-rasterizer')
	if no_proxy_server:
		options.add_argument('--no-proxy-server')
	if allow_running_insecure_content:
		options.add_argument('--allow-running-insecure-content')
	if disable_logging:
		options.add_argument('--disable-logging')
	if log_level:
		options.add_argument('--log-level={}'.format(settings.LOG_LEVEL))
	if disable_3d_apis:
		options.add_argument("--disable-3d-apis")
	if disable_renderer_backgrounding:
		options.add_argument("--disable-renderer-backgrounding")
	if disable_background_networking:
		options.add_argument("--disable-background-networking")
	if disable_notifications:
		options.add_argument("--disable-notifications")
	if mute_audio:
		options.add_argument("--mute-audio")
	if disable_features:
		options.add_argument("--disable-features=%s" % ",".join(settings.DISABLE_FEATURES))

	return options
