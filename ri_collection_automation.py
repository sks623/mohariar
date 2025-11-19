"""
RI Online Collection Entry Automation
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

def main():
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach", True)

    print("Initializing Chrome browser...")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Step 1: Navigate to login page
        print("Opening Odisha Land Revenue login page...")
        driver.get("https://odishalandrevenue.nic.in/DefaultLogin.aspx")
        time.sleep(2)

        print("\n" + "="*60)
        print("STEP 1: PLEASE LOGIN MANUALLY NOW")
        print("1. Select your district")
        print("2. Enter User ID")
        print("3. Enter Password")
        print("4. Solve the captcha")
        print("5. Click Login button")
        print("="*60 + "\n")

        # Wait for login to complete
        print("Waiting for you to complete login...")
        timeout = 300
        start_time = time.time()

        while "DefaultLogin.aspx" in driver.current_url:
            if time.time() - start_time > timeout:
                print("Timeout waiting for login!")
                return None
            time.sleep(1)

        print("\n[SUCCESS] Login successful!")
        time.sleep(2)

        # Step 2: Click on RI Online Collection Entry
        print("\n" + "="*60)
        print("STEP 2: NAVIGATING TO RI ONLINE COLLECTION ENTRY")
        print("="*60 + "\n")

        # Find and click the RI Online Collection Entry link
        try:
            ri_link = driver.find_element(By.LINK_TEXT, "RI Online Collection Entry")
            ri_link.click()
            print("[SUCCESS] Clicked on 'RI Online Collection Entry'")
            time.sleep(3)  # Wait for page to load
        except Exception as e:
            print(f"[ERROR] Could not find/click RI Online Collection Entry link: {e}")
            return None

        # Step 3: Wait for user to select village
        print("\n" + "="*60)
        print("STEP 3: SELECT VILLAGE")
        print("="*60)
        print("\nPlease select your desired village from the dropdown.")
        print("The dropdown should be visible on the page.")

        # Wait for village dropdown to be present
        try:
            village_dropdown = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "ddlVillage"))
            )
            print("[SUCCESS] Village dropdown found!")
        except:
            # Try alternative selector
            try:
                village_dropdown = driver.find_element(By.XPATH, "//select[contains(@id, 'Village') or contains(@id, 'village')]")
                print("[SUCCESS] Village dropdown found!")
            except Exception as e:
                print(f"[WARNING] Could not locate village dropdown automatically: {e}")
                print("Please select village manually.")

        print("\nWaiting for you to select a village...")
        print("Once you've selected the village, press Enter in this terminal to continue...")
        input()

        print("\n[SUCCESS] Village selected! Continuing automation...")

        # Return driver for next steps
        return driver

    except Exception as e:
        print(f"Error: {e}")
        driver.quit()
        return None

if __name__ == "__main__":
    driver = main()
    if driver:
        print("\n" + "="*60)
        print("READY FOR NEXT STEP")
        print("="*60)
        print("\nWhat should I do next?")
        print("Tell me the next automation steps...")

        input("\n\nPress Enter to close browser...")
        driver.quit()
