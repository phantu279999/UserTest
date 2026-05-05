# 🧪 Simple Automation Test Framework
> ⚠️ *This project is currently under development.*

---

## 📁 Configuration

### `config_actions.json`
This file defines the test cases and corresponding actions to automate.

- Each test case includes a list of actions (e.g., click, input, verify).
- Fully customizable with flexible action types and locators.

---

## Front-end Auto Config

### `frontend/fe-auto`
- React-powered interfaces can help users configure actions more easily.

```commandline
    npm install
    npm install lucide-react
    npm run dev
```

![img.png](frontend/fe-auto/src/assets/img.png)

---

## 🚀 How to Run Tests

### `main.py`

This script starts executing the automation test cases defined in `config_actions.json`.

### Example Output:
```bash
--------------- Start run |test_login| --------------
------------- Action 1 -------------  
True Passed  
------------- Action 2 -------------  
True Passed  
------------- Action 3 -------------  
True Passed  
------------- Action 4 -------------  
True Passed  
------------- Action 5 -------------  
True (title) Passed  

--------------- Start run |test_search| --------------
------------- Action 1 -------------  
True Passed  
------------- Action 2 -------------  
True Passed  
------------- Action 3 -------------  
True Passed  
------------- Action 4 -------------  
True (xpath_text) Passed  
```

---

## 🌐 Supported Environment Drivers

| Environment              | Description                             |
|--------------------------|-----------------------------------------|
| `chrome`                 | Run on Chrome in normal mode            |
| `chrome_headless`        | Run on Chrome in headless mode          |
| `chrome_mobile`          | Simulate mobile browser on Chrome       |
| `chrome_mobile_headless` | Mobile simulation in headless Chrome    |
| `firefox`                | Run on Firefox browser                  |
| `chrome_grid`            | Run on Remote mode + parallel + mul env |

> ✅ Default is `chrome`.

---

## 📜 License

This project is licensed by **Phan Anh Tu**.  
Use and contribute freely with credit.

---

Feel free to suggest more features or contribute with pull requests!
