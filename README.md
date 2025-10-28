# 🧪 SauceDemo E-Commerce Automated Testing

Automated test solution for the SauceDemo e-commerce platform using **Pytest** and **Selenium WebDriver**.

**Website:** [https://www.saucedemo.com](https://www.saucedemo.com)

---

## 📋 Challenge Overview

This project implements an automated test that verifies the complete "Add to Cart" workflow on the SauceDemo e-commerce website. The test performs end-to-end validation of the shopping cart functionality.

### Test Scenario

The automated test script performs the following steps:

1. ✅ Navigate to the SauceDemo login page
2. ✅ Log in using provided credentials (standard_user / secret_sauce)
3. ✅ Locate the item "Sauce Labs Backpack" on the inventory page
4. ✅ Add the item to the shopping cart
5. ✅ Navigate to the shopping cart page
6. ✅ Verify the item name is exactly "Sauce Labs Backpack"
7. ✅ Verify the item price is exactly $29.99
8. ✅ Ensure browser is properly closed after test completion (pass or fail)

---

## 🧰 Technologies & Tools

| Component | Technology |
|-----------|-----------|
| **Programming Language** | Python 3.x |
| **Test Framework** | Pytest |
| **Web Automation** | Selenium WebDriver 4.x |
| **Driver Management** | WebDriver Manager |
| **Browser** | Google Chrome |
| **Element Locators** | ID, Class Name (robust and maintainable) |
| **Synchronization** | Explicit waits (WebDriverWait) |

---

## ✨ Key Features

- **Robust Locator Strategy:** Uses reliable ID-based locators for critical elements
- **Explicit Waits:** Implements WebDriverWait with appropriate conditions for reliable synchronization
- **No Static Delays:** Avoids hardcoded sleeps; uses smart wait conditions
- **Clean Code:** Well-structured with constants, clear comments, and descriptive variable names
- **Proper Fixtures:** Ensures browser cleanup with pytest fixtures
- **Assertive Error Messages:** Provides meaningful failure messages for debugging

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.7 or higher
- Google Chrome browser installed
- pip (Python package installer)

### Installation Steps

#### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/pytest-selenium-saucedemo.git
cd pytest-selenium-saucedemo
```

#### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- `selenium==4.25.0`
- `pytest==8.3.3`
- `webdriver-manager==4.0.2`

#### 3. Run the Tests
```bash
pytest -v
```

**Alternative for Windows:**
```bash
python -m pytest -v
```

### Expected Output

When running successfully, you should see:
```
============================= test session starts =============================
platform win32 -- Python 3.x, pytest-8.3.3
collecting ... collected 1 item

test_add_to_cart.py::test_add_to_cart PASSED                             [100%]

============================= 1 passed in ~25s ==============================
```

---

## 📁 Project Structure

```
pytest-selenium-saucedemo/
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── test_add_to_cart.py       # Main test script
└── .pytest_cache/            # Pytest cache (auto-generated)
```

---

## 🎯 Test Execution Flow

The test follows this precise workflow:

1. **Browser Initialization:** Chrome WebDriver starts in maximized mode
2. **Login:** Navigates to login page and authenticates
3. **Item Selection:** Locates "Sauce Labs Backpack" using robust ID locator
4. **Add to Cart:** Clicks add button and verifies button state change
5. **Cart Navigation:** Opens shopping cart page
6. **Verification:** Validates both item name and price assertions
7. **Cleanup:** Browser automatically closes regardless of test outcome

---

## 🔍 Code Quality Highlights

- **Constants:** All values (URLs, credentials, expected results) are defined as constants at module level
- **Explicit Waits:** Every interaction uses appropriate WebDriverWait conditions
- **Clear Text:** Input fields are cleared before typing to avoid data corruption
- **URL Verification:** Checks URL changes to confirm navigation
- **State Verification:** Verifies button state changes to confirm actions
- **Meaningful Assertions:** Assertion messages clearly describe expected vs actual values

---

## 📝 Notes

- The test uses ID-based locators where possible, as they are the most stable and performant
- Explicit waits ensure the test doesn't rely on arbitrary timing
- The WebDriver Manager automatically handles ChromeDriver installation and versioning
- Browser is automatically closed via pytest fixture, ensuring cleanup even on failures
