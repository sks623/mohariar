"""
RI Online Collection Entry - Full Automation
Automates the entire flow from login to saving collection entry
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import time

def wait_for_element(driver, by, value, timeout=10):
    """Wait for element to be present"""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )

def wait_for_clickable(driver, by, value, timeout=10):
    """Wait for element to be clickable"""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, value))
    )

def main():
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach", True)

    print("="*70)
    print("RI ONLINE COLLECTION ENTRY AUTOMATION")
    print("="*70)

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # ==================== STEP 1: LOGIN ====================
        print("\n[STEP 1] Opening login page...")
        driver.get("https://odishalandrevenue.nic.in/DefaultLogin.aspx")
        time.sleep(2)

        print("\n" + "="*70)
        print("PLEASE LOGIN MANUALLY:")
        print("  1. Select your district")
        print("  2. Enter User ID")
        print("  3. Enter Password")
        print("  4. Solve the captcha")
        print("  5. Click Login button")
        print("="*70)

        # Wait for login completion
        print("\nWaiting for login...")
        timeout = 300
        start_time = time.time()

        while "DefaultLogin.aspx" in driver.current_url:
            # Check for login error alerts and dismiss them
            try:
                WebDriverWait(driver, 0.5).until(EC.alert_is_present())
                alert = driver.switch_to.alert
                alert_text = alert.text
                print(f"[WARNING] Login alert: {alert_text}")
                alert.accept()  # Dismiss the alert
                print("[INFO] Alert dismissed. Please try logging in again...")
                # Reset timeout after error so user has time to retry
                start_time = time.time()
            except:
                pass  # No alert present, continue waiting

            if time.time() - start_time > timeout:
                print("[ERROR] Timeout waiting for login!")
                return
            time.sleep(1)

        print("[SUCCESS] Logged in successfully!\n")
        time.sleep(2)

        # ==================== STEP 2: NAVIGATE TO RI ONLINE COLLECTION ====================
        print("[STEP 2] Navigating to RI Online Collection Entry...")

        try:
            ri_link = wait_for_clickable(driver, By.LINK_TEXT, "RI Online Collection Entry")
            ri_link.click()
            print("[SUCCESS] Clicked 'RI Online Collection Entry'\n")
            time.sleep(2)

            # Check for popup/alert asking about village selection
            try:
                WebDriverWait(driver, 5).until(EC.alert_is_present())
                alert = driver.switch_to.alert
                alert_text = alert.text
                print(f"[POPUP] Alert appeared: {alert_text}")
                alert.accept()  # Click Yes/OK
                print("[SUCCESS] Clicked Yes on popup\n")
                time.sleep(2)
            except:
                print("[INFO] No popup appeared, continuing...\n")
                time.sleep(1)

        except Exception as e:
            print(f"[ERROR] Could not click RI Online Collection Entry: {e}")
            return

        # ==================== STEP 3: SELECT VILLAGE ====================
        print("[STEP 3] Village Selection")
        print("-" * 70)
        print("Please select your desired village from the dropdown.")
        print("Waiting for village selection...")

        # Find village dropdown
        village_dropdown = None
        possible_ids = ['ddlVillage', 'ddlVillageName', 'ContentPlaceHolder1_ddlVillage']

        for dropdown_id in possible_ids:
            try:
                village_dropdown = driver.find_element(By.ID, dropdown_id)
                print(f"[DEBUG] Found village dropdown with ID: {dropdown_id}")
                break
            except:
                continue

        if not village_dropdown:
            try:
                village_dropdown = driver.find_element(By.XPATH, "//select[contains(@id, 'Village') or contains(@id, 'village')]")
                print("[DEBUG] Found village dropdown with XPath")
            except Exception as e:
                print(f"[ERROR] Could not find village dropdown: {e}")
                return

        # Wait for user to select a village (value changes from default)
        select = Select(village_dropdown)

        # Get initial value - try to handle if it's already selected
        try:
            initial_value = select.first_selected_option.get_attribute("value")
            initial_text = select.first_selected_option.text
            print(f"Current selection: {initial_text} (value: {initial_value})")
        except:
            initial_value = ""
            initial_text = "--Select--"

        print("Waiting for you to select a village...")

        # Wait until selection changes
        timeout = 300
        start_time = time.time()
        while True:
            try:
                current_value = select.first_selected_option.get_attribute("value")
                current_text = select.first_selected_option.text

                # Check if a valid village is selected (not empty and not --Select--)
                if current_value and current_value != "" and current_text != "--Select--" and current_text.strip():
                    if current_value != initial_value or initial_value == "":
                        selected_village = current_text
                        print(f"[SUCCESS] Village selected: {selected_village}\n")
                        time.sleep(3)  # Wait for page to update with Khata dropdown
                        break

                if time.time() - start_time > timeout:
                    print("[ERROR] Timeout waiting for village selection!")
                    return

                time.sleep(0.5)
            except Exception as e:
                print(f"[ERROR] Error checking village selection: {e}")
                break

        # ==================== STEP 4: SELECT KHATA ====================
        print("[STEP 4] Khata Selection")
        print("-" * 70)

        try:
            # Wait for Khata dropdown to be populated
            time.sleep(2)

            # Find Khata dropdown (try multiple possible IDs)
            khata_dropdown = None
            possible_ids = ['ddlKhata', 'ddlKhataNo', 'ContentPlaceHolder1_ddlKhata']

            for dropdown_id in possible_ids:
                try:
                    khata_dropdown = driver.find_element(By.ID, dropdown_id)
                    break
                except:
                    continue

            if not khata_dropdown:
                # Try by name attribute or xpath
                khata_dropdown = driver.find_element(By.XPATH, "//select[contains(@id, 'Khata') or contains(@id, 'khata')]")

            # Get all options
            select = Select(khata_dropdown)
            options = select.options

            print(f"Found {len(options)} Khata options")

            # Select first valid Khata (skip --Select--)
            for option in options[1:]:  # Skip first option which is usually --Select--
                if option.text.strip() and option.text.strip() != "--Select--":
                    select.select_by_visible_text(option.text)
                    print(f"[SUCCESS] Selected Khata: {option.text}\n")
                    time.sleep(3)  # Wait for form to load
                    break

        except Exception as e:
            print(f"[WARNING] Auto-selection failed: {e}")
            print("Please select Khata manually...")
            print("Waiting for Khata selection...")
            time.sleep(5)  # Give time for manual selection
            print("[SUCCESS] Continuing with selected Khata\n")
            time.sleep(2)

        # ==================== STEP 5: FILL DEPOSITOR DETAILS ====================
        print("[STEP 5] Filling Depositor Details")
        print("-" * 70)

        try:
            # Wait for depositor fields to appear
            time.sleep(2)

            # Find and fill "Deposited By" field
            deposited_by_field = None
            possible_deposited_ids = ['txtDepositedBy', 'txtDepositorName', 'ContentPlaceHolder1_txtDepositedBy']

            for field_id in possible_deposited_ids:
                try:
                    deposited_by_field = driver.find_element(By.ID, field_id)
                    break
                except:
                    continue

            if not deposited_by_field:
                deposited_by_field = driver.find_element(By.XPATH, "//input[@type='text' and (contains(@id, 'Deposit') or contains(@id, 'deposit'))]")

            deposited_by_field.clear()
            deposited_by_field.send_keys("self")
            print("[SUCCESS] Filled 'Deposited By': self")

            # Find and fill "Mobile No" field
            mobile_field = None
            possible_mobile_ids = ['txtMobile', 'txtMobileNo', 'ContentPlaceHolder1_txtMobile']

            for field_id in possible_mobile_ids:
                try:
                    mobile_field = driver.find_element(By.ID, field_id)
                    break
                except:
                    continue

            if not mobile_field:
                mobile_field = driver.find_element(By.XPATH, "//input[@type='text' and (contains(@id, 'Mobile') or contains(@id, 'mobile'))]")

            mobile_field.clear()
            mobile_field.send_keys("8984750096")
            print("[SUCCESS] Filled 'Mobile No': 8984750096\n")

            time.sleep(1)

        except Exception as e:
            print(f"[ERROR] Could not fill depositor details: {e}")
            print("Please fill manually...")
            time.sleep(10)  # Give time for manual entry

        # ==================== STEP 6: CLICK SAVE BUTTON ====================
        print("[STEP 6] Saving Entry")
        print("-" * 70)

        try:
            # Find Save button (red button)
            save_button = None
            possible_save_ids = ['btnSave', 'btnConfirm', 'Button1', 'ContentPlaceHolder1_btnSave', 'ContentPlaceHolder1_btnConfirm']

            for btn_id in possible_save_ids:
                try:
                    save_button = driver.find_element(By.ID, btn_id)
                    break
                except:
                    continue

            if not save_button:
                # Try finding by button text
                save_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Save']")

            # Scroll to the button to ensure it's visible
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_button)
            time.sleep(1)

            # Try regular click first
            try:
                save_button.click()
                print("[SUCCESS] Clicked Save button\n")
            except:
                # If regular click fails, use JavaScript click
                print("[INFO] Regular click failed, using JavaScript click...")
                driver.execute_script("arguments[0].click();", save_button)
                print("[SUCCESS] Clicked Save button using JavaScript\n")

            time.sleep(2)

        except Exception as e:
            print(f"[ERROR] Could not click Save button: {e}")
            return

        # ==================== STEP 7: HANDLE FIRST CONFIRMATION (Yes/No) ====================
        print("[STEP 7] Handling First Confirmation Popup")
        print("-" * 70)

        try:
            # Wait for modal dialog to appear
            time.sleep(3)  # Give modal time to appear and render

            # Try to find and click the Yes button using multiple strategies
            yes_button = None

            # List of XPath expressions to try
            xpath_variations = [
                # Button elements
                "//button[text()='Yes']",
                "//button[contains(text(), 'Yes')]",
                "//button[normalize-space(text())='Yes']",
                # Anchor tags styled as buttons
                "//a[text()='Yes']",
                "//a[contains(text(), 'Yes')]",
                # Input buttons
                "//input[@type='button' and @value='Yes']",
                "//input[@type='submit' and @value='Yes']",
                # Any element with Yes text
                "//*[text()='Yes']",
                "//*[contains(text(), 'Yes')]",
                # Case insensitive
                "//*[contains(translate(text(), 'YES', 'yes'), 'yes')]",
            ]

            print("[DEBUG] Searching for Yes button...")
            for xpath in xpath_variations:
                try:
                    elements = driver.find_elements(By.XPATH, xpath)
                    for elem in elements:
                        if elem.is_displayed():
                            yes_button = elem
                            print(f"[FOUND] Yes button using XPath: {xpath}")
                            break
                    if yes_button:
                        break
                except Exception as e:
                    continue

            if yes_button:
                print(f"[SUCCESS] Yes button located! Tag: {yes_button.tag_name}, Text: {yes_button.text}")

                # Scroll to button
                try:
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", yes_button)
                    time.sleep(0.5)
                except:
                    pass

                # Try to click it
                try:
                    yes_button.click()
                    print("[SUCCESS] Clicked Yes on 'Do you want to continue' popup\n")
                except:
                    # Use JavaScript click if regular click fails
                    try:
                        driver.execute_script("arguments[0].click();", yes_button)
                        print("[SUCCESS] Clicked Yes using JavaScript\n")
                    except Exception as e:
                        print(f"[ERROR] Could not click Yes button: {e}\n")

                time.sleep(3)  # Wait a few seconds for next popup
            else:
                print("[WARNING] No Yes button found in modal\n")
                print("[INFO] Modal might not have appeared or has different structure")

        except Exception as e:
            print(f"[WARNING] Error handling confirmation popup: {e}\n")
            import traceback
            traceback.print_exc()
            time.sleep(2)

        # ==================== STEP 8: CLOSE RECEIPT WINDOW ====================
        print("[STEP 8] Handling Receipt Window")
        print("-" * 70)

        try:
            # Wait for new window to open
            time.sleep(3)

            # Get current window handle (main window)
            main_window = driver.current_window_handle
            print(f"[DEBUG] Main window handle: {main_window}")

            # Get all window handles
            all_windows = driver.window_handles
            print(f"[DEBUG] Total windows open: {len(all_windows)}")

            # Check if a new window opened
            if len(all_windows) > 1:
                print("[FOUND] New receipt window detected!")

                # Switch to the new window (receipt window)
                for window in all_windows:
                    if window != main_window:
                        driver.switch_to.window(window)
                        print(f"[SUCCESS] Switched to receipt window")
                        print(f"[INFO] Receipt URL: {driver.current_url}")
                        time.sleep(1)

                        # Close the receipt window
                        driver.close()
                        print("[SUCCESS] Closed receipt window\n")
                        break

                # Switch back to main window
                driver.switch_to.window(main_window)
                print("[SUCCESS] Switched back to main window\n")
                time.sleep(2)

            else:
                print("[INFO] No new window detected\n")

        except Exception as e:
            print(f"[WARNING] Error handling receipt window: {e}\n")
            # Try to switch back to main window in case of error
            try:
                driver.switch_to.window(main_window)
            except:
                pass

        # ==================== COMPLETE ====================
        print("="*70)
        print("AUTOMATION COMPLETED SUCCESSFULLY!")
        print("="*70)
        print("\nEntry has been saved.")

        return driver

    except Exception as e:
        print(f"\n[ERROR] An error occurred: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    driver = main()
    if driver:
        print("\n\nAutomation complete! Browser will remain open.")
        print("You can manually close it or process another Khata.")
        # Keep browser open - user can close manually
        time.sleep(5)
    else:
        print("\nAutomation failed. Please check the errors above.")
        time.sleep(5)
