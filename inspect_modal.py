"""
Diagnostic script to inspect the modal and find the Yes button
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to login page
    print("Opening login page...")
    driver.get("https://odishalandrevenue.nic.in/DefaultLogin.aspx")
    time.sleep(2)

    print("\nPlease login...")
    # Wait for login
    while "DefaultLogin.aspx" in driver.current_url:
        time.sleep(1)

    print("Logged in! Clicking RI Online Collection Entry...")
    time.sleep(2)

    # Click RI Online Collection Entry
    ri_link = driver.find_element(By.LINK_TEXT, "RI Online Collection Entry")
    ri_link.click()
    time.sleep(3)

    print("Please select village manually and press Enter here...")
    input()

    print("Please select Khata manually and press Enter here...")
    input()

    print("Filling depositor details...")
    # Fill depositor fields
    deposited_by = driver.find_element(By.XPATH, "//input[@type='text' and (contains(@id, 'Deposit') or contains(@id, 'deposit'))]")
    deposited_by.send_keys("self")

    mobile = driver.find_element(By.XPATH, "//input[@type='text' and (contains(@id, 'Mobile') or contains(@id, 'mobile'))]")
    mobile.send_keys("8984750096")

    print("Clicking Save button...")
    save_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Save']")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_button)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", save_button)

    print("\n" + "="*70)
    print("SAVE BUTTON CLICKED - WAITING FOR MODAL...")
    print("="*70)
    time.sleep(3)

    # Now inspect all buttons on the page
    print("\nSearching for all buttons on the page...")

    all_buttons = driver.find_elements(By.TAG_NAME, "button")
    print(f"\nFound {len(all_buttons)} <button> elements:")
    for i, btn in enumerate(all_buttons):
        try:
            text = btn.text
            is_displayed = btn.is_displayed()
            btn_id = btn.get_attribute("id")
            btn_class = btn.get_attribute("class")
            print(f"{i+1}. Text: '{text}' | Displayed: {is_displayed} | ID: {btn_id} | Class: {btn_class}")
        except:
            pass

    # Check for input buttons
    input_buttons = driver.find_elements(By.XPATH, "//input[@type='button' or @type='submit']")
    print(f"\nFound {len(input_buttons)} <input> buttons:")
    for i, btn in enumerate(input_buttons):
        try:
            value = btn.get_attribute("value")
            is_displayed = btn.is_displayed()
            btn_id = btn.get_attribute("id")
            print(f"{i+1}. Value: '{value}' | Displayed: {is_displayed} | ID: {btn_id}")
        except:
            pass

    # Check for anchor tags that look like buttons
    links = driver.find_elements(By.TAG_NAME, "a")
    print(f"\nChecking {len(links)} <a> tags for button-like elements:")
    for i, link in enumerate(links):
        try:
            text = link.text
            is_displayed = link.is_displayed()
            if is_displayed and text and ("yes" in text.lower() or "no" in text.lower() or "ok" in text.lower()):
                link_id = link.get_attribute("id")
                link_class = link.get_attribute("class")
                print(f"  FOUND: Text: '{text}' | ID: {link_id} | Class: {link_class}")
        except:
            pass

    print("\n" + "="*70)
    print("INSPECTION COMPLETE")
    print("="*70)
    print("\nNow manually click the Yes button and observe what happens...")
    input("\nPress Enter to close...")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
finally:
    pass  # Keep browser open
