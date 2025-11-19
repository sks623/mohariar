"""
Helper script to find links on the current page
Run this after logging in
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def find_links():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to login page
        print("Opening login page...")
        driver.get("https://odishalandrevenue.nic.in/DefaultLogin.aspx")
        time.sleep(2)

        print("\n" + "="*60)
        print("PLEASE LOGIN MANUALLY")
        print("="*60 + "\n")

        # Wait for login
        while "DefaultLogin.aspx" in driver.current_url:
            time.sleep(1)

        print("[SUCCESS] Login successful!")
        time.sleep(2)

        # Find all links on the page
        print("\nSearching for links on the page...\n")

        # Find all <a> tags
        links = driver.find_elements(By.TAG_NAME, "a")

        print("="*60)
        print(f"FOUND {len(links)} LINKS:")
        print("="*60)

        ri_links = []
        for i, link in enumerate(links, 1):
            text = link.text.strip()
            href = link.get_attribute("href")
            if text:  # Only show links with visible text
                print(f"{i}. Text: '{text}'")
                if href:
                    print(f"   URL: {href}")
                print()

                # Check if it's the RI Online Collection Entry link
                if "ri" in text.lower() and ("online" in text.lower() or "collection" in text.lower() or "entry" in text.lower()):
                    ri_links.append((text, href))

        if ri_links:
            print("\n" + "="*60)
            print("FOUND RI ONLINE COLLECTION RELATED LINKS:")
            print("="*60)
            for text, href in ri_links:
                print(f"Text: {text}")
                print(f"URL: {href}\n")
        else:
            print("\n[INFO] No 'RI Online Collection Entry' link found.")
            print("Looking for partial matches...")

            # Try menu items
            menu_items = driver.find_elements(By.XPATH, "//*[contains(@class, 'menu') or contains(@class, 'nav')]//a")
            print(f"\nFound {len(menu_items)} menu items:")
            for item in menu_items:
                text = item.text.strip()
                if text:
                    print(f"- {text}")

        input("\n\nPress Enter to close browser...")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    find_links()
