#!/usr/bin/python3
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.base_selenium.process_actions import ProcessActions


driver = 'chrome_headless'


if __name__ == '__main__':
	process_actions = ProcessActions(driver)
	process_actions.app_run()
