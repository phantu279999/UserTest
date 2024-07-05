import json
from src.base_selenium.process_actions import ProcessActions


if __name__ == '__main__':
	process_actions = ProcessActions()
	data = {}
	with open("config_actions.json", "r") as f:
		data = json.loads(f.read())

	for test_case in data['run']:
		for action in data[test_case]['action']:
			print(action)

