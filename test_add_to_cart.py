import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# Constants
BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
ITEM_NAME = "Sauce Labs Backpack"
EXPECTED_PRICE = "$29.99"

# Wait timeout
WAIT_TIMEOUT = 20


@pytest.fixture(scope="function")
def driver():
    """
    Setup and teardown for Chrome WebDriver.
    Ensures the browser is properly closed after test execution, regardless of pass or fail.
    """
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # Additional options for better stability
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    
    yield driver
    
    # Teardown: ensure browser is closed properly
    driver.quit()


def test_add_to_cart(driver):
    """
    Automated test for adding 'Sauce Labs Backpack' to cart and verifying name & price.
    
    Steps:
    1. Navigate to the login page
    2. Log in using provided credentials
    3. Identify the item named 'Sauce Labs Backpack'
    4. Add this item to the shopping cart
    5. Navigate to the shopping cart page
    6. Verify item name is 'Sauce Labs Backpack'
    7. Verify item price is $29.99
    """
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    
    # Step 1: Navigate to login page
    driver.get(BASE_URL)
    
    # Step 2: Login with credentials
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    username_field.clear()
    username_field.send_keys(USERNAME)
    
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_field.clear()
    password_field.send_keys(PASSWORD)
    
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()
    
    # Step 3: Verify successful login by waiting for inventory page
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
    
    # Step 4: Add 'Sauce Labs Backpack' to cart
    add_to_cart_button = wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    add_to_cart_button.click()
    
    # Step 5: Navigate to shopping cart
    cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_icon.click()
    
    # Step 6 & 7: Verify cart contents - item name and price
    item_name_element = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    )
    actual_item_name = item_name_element.text
    
    item_price_element = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_price"))
    )
    actual_item_price = item_price_element.text
    
    # Assertions with descriptive error messages
    assert actual_item_name == ITEM_NAME, \
        f"Item name verification failed. Expected: '{ITEM_NAME}', Actual: '{actual_item_name}'"
    
    assert actual_item_price == EXPECTED_PRICE, \
        f"Item price verification failed. Expected: '{EXPECTED_PRICE}', Actual: '{actual_item_price}'"
