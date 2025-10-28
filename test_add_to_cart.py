import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    """Setup and teardown for Chrome WebDriver."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()


def test_add_to_cart(driver):
    """Test adding 'Sauce Labs Backpack' to cart and verifying name & price"""
    wait = WebDriverWait(driver, 20)

    # 1️⃣ Navigate to login page
    driver.get("https://www.saucedemo.com/")

    # 2️⃣ Login with valid credentials
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3️⃣ Wait for inventory page to load
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))

    # 4️⃣ Add “Sauce Labs Backpack” to cart
    add_button = wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    add_button.click()

    # 5️⃣ Navigate to cart
    cart_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_link.click()

    # 6️⃣ Verify cart item name and price
    item_name = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    ).text
    item_price = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_price"))
    ).text

    # 7️⃣ Assertions
    assert item_name == "Sauce Labs Backpack", f"Expected 'Sauce Labs Backpack', got '{item_name}'"
    assert item_price == "$29.99", f"Expected '$29.99', got '{item_price}'"
