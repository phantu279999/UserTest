
# Helper Tool Guide

---

## Structure of Config Test Actions

```json
{
  "run": [
    "test_login",
    "other_test_case"
  ],
  "test_login": {
    "time_sleep_action": 1,
    "action": [
      {
        "name": "",
        "value": "http://testphp.vulnweb.com/",
        "type": "get_domain"
      },
      {
        "locator": "//input[@value=\"login\"]",
        "locator_type": "xpath",
        "type": "input",
        "value": "Username",
        "sleep": 1,
        "result": {
          "type": "title",
          "value": "user info"
        }
      }
    ]
  },
  "other_test_case": {
    "time_sleep_action": 1,
    "action": [
      {
        "name": "",
        "value": "http://testphp.vulnweb.com/",
        "type": "get_domain"
      },
      {
        "locator": "//div[@id=\"content\"]//h2",
        "type": "click",
        "result": {
          "type": "xpath_text",
          "value": "searched for: test",
          "xpath": "//div[@id=\"content\"]//h2"
        }
      }
    ]
  }
}
```

---

## Explanation of the Above JSON

- `run`: Defines the test cases to be executed.
- `test_login`, `other_test_case`: Named test cases, each containing:
  - `time_sleep_action`: Delay time between actions.
  - `action`: An array of action objects with specific interactions and validations.

---

## Elements Reference

### Element Action Fields:
- `name`
- `type`
- `locator`
- `locator_type`
- `value`
- `sleep`
- `result`
- `locator_type_2`
- `locator_2`

---

### Type Action:
- `get_domain`
- `open_new_tab`
- `click`
- `input`
- `input_enter`
- `enter`
- `switch_to_frame`
- `switch_to_next_tab`
- `switch_to_last_tab`
- `switch_to_first_tab`
- `move`
- `move_click`
- `drag_and_drop`
- `clear`
- `clear_and_input`

---

### Type Locator:
> Default: `xpath`

- `id`
- `xpath`
- `link text`
- `partial link text`
- `name`
- `tag name`
- `class name`
- `css selector`

---

### Type Result:
Defines what the test should verify after each action.

- `title`: Check current page title.
- `xpath`: Check if xpath exists.
- `display`: Check if xpath element is visible.
- `xpath_text`: Check if the xpath element’s text equals value.
- `url`: Check if current URL equals value.
- `alert`: Check if an alert is displayed.
- `status`: Check if HTTP status code equals value.

**Example**:

```json
"result": {
  "type": "xpath_text",
  "value": "searched for: test",
  "xpath": "//div[@id=\"content\"]//h2"
}
```
