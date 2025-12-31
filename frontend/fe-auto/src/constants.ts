import { ActionType, LocatorType, ResultType } from './types';
import type { TestCase } from './types';

export const ACTION_TYPES = Object.values(ActionType);
export const LOCATOR_TYPES = Object.values(LocatorType);
export const RESULT_TYPES = Object.values(ResultType);

export const DEFAULT_TEST_CASE: TestCase = {
  time_sleep_action: 1,
  action: [],
};

export const INITIAL_JSON_EXAMPLE = {
  "run": [
    "test_login"
  ],
  "test_login": {
    "time_sleep_action": 1,
    "action": [
      {
        "name": "Navigate",
        "value": "http://testphp.vulnweb.com/",
        "type": "get_domain"
      },
      {
        "locator": "//input[@value=\"login\"]",
        "locator_type": "xpath",
        "type": "input",
        "value": "testuser",
        "sleep": 1,
        "result": {
          "type": "title",
          "value": "user info"
        }
      }
    ]
  }
};