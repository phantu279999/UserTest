# This is helper using tool
<hr>

### Structure of config test actions

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
        "type": "get_domain",
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

#### Explain above file json

***run***: this will decide the configuration of the below testcases, It decides which test cases are run.
<br>
***testcase***(test_login): name of testcase, It's contain chain actions.

    time_sleep_action: Using for each action sleep time
    action: [actions of testcase]


## Explain Elements
<hr>

#### Element action:
    name
    type
    locator
    locator_type
    value
    sleep
    result
    locator_type_2
    locator_2

#### Type action:
    get_domain,
    open_new_tab,
    click,
    input,
    input_enter,
    enter,
    switch_to_frame,
    switch_to_next_tab,
    switch_to_last_tab,
    switch_to_first_tab,
    move,
    move_click,
    drag_and_drop,
    clear,
    clear_and_input

#### Type locator
if not provide type, It's default is xpath

    id
    xpath
    link text
    partial link text
    name
    tag name
    class name
    css selector


#### Type result
Check result of executed action

    title
    xpath
    display
    xpath_text
    url
    alert
    status


***title***: Check title of current page.
<br>
***xpath***: Check xpath is exits.
<br>
***display***: Check xpath is display.
<br>
***xpath_text***: Check text of text.
<br>
***url***: Check current url.
<br>
***alert***: Check alert is display.
<br>
***status***: Check status of current page.
<br>

**Example**:

```json
"result": {
  "type": "xpath_text",
  "value": "searched for: test",
  "xpath": "//div[@id=\"content\"]//h2"
}
```