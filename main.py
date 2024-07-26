#!/usr/bin/python3
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.base_selenium.process_actions import ProcessActions


# driver = 'firefox'
# driver = 'chrome_headless'
driver = 'chrome'


if __name__ == '__main__':
	process_actions = ProcessActions(driver)
	try:
		process_actions.app_run()
		process_actions.quit_driver()
	except:
		process_actions.quit_driver()
