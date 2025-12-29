#!/usr/bin/python3
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.base_selenium.process_actions import ProcessActions


# driver = 'firefox'
# driver = 'chrome_headless'
# driver = 'chrome'
driver = 'chrome_grid'


if __name__ == '__main__':
	process_actions = ProcessActions(driver)
	try:
		result = process_actions.app_run()
		if not result:
			sys.exit(1)

		has_fail = any(step["status"] is False for step in result)
		if has_fail:
			print("TEST FAILED")
			sys.exit(1)
		else:
			print("TEST PASSED")
			sys.exit(0)
	except:
		sys.exit(1)
	finally:
		process_actions.quit_driver()
