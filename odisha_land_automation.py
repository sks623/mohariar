"""
Odisha Land Revenue Portal Automation
This script opens the login page, waits for manual login, then allows automation
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def main():
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # Keep browser open after script ends
    chrome_options.add_experimental_option("detach", True)

    # Initialize the Chrome driver
    print("Initializing Chrome browser...")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to login page
        print("Opening Odisha Land Revenue login page...")
        driver.get("https://odishalandrevenue.nic.in/DefaultLogin.aspx")

        # Wait for page to load
        time.sleep(2)

        print("\n" + "="*60)
        print("PLEASE LOGIN MANUALLY NOW")
        print("1. Select your district")
        print("2. Enter User ID")
        print("3. Enter Password")
        print("4. Solve the captcha")
        print("5. Click Login button")
        print("="*60 + "\n")

        # Wait for login to complete
        print("Waiting for you to complete login...")

        # Keep checking if URL has changed (login successful)
        timeout = 300  # 5 minutes timeout
        start_time = time.time()

        while "DefaultLogin.aspx" in driver.current_url:
            if time.time() - start_time > timeout:
                print("Timeout waiting for login!")
                return
            time.sleep(1)

        print("\n[SUCCESS] Login successful! Taking over automation now...")

        # Get current URL to see where we landed
        current_url = driver.current_url
        print(f"Current page: {current_url}")

        # Wait a moment to ensure page is fully loaded
        time.sleep(2)

        # Now automation takes over
        print("\n" + "="*60)
        print("AUTOMATION ACTIVE - Tell me what to do next")
        print("="*60 + "\n")

        # Return the driver object so we can use it for further automation
        return driver

    except Exception as e:
        print(f"Error: {e}")
        driver.quit()
        return None

if __name__ == "__main__":
    driver = main()
    if driver:
        input("\nPress Enter to close browser...")
        driver.quit()
