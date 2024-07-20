#!/usr/bin/python3
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.base_selenium.process_actions import ProcessActions


if __name__ == '__main__':
	process_actions = ProcessActions()
	process_actions.app_run()
