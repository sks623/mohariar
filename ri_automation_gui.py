"""
RI Online Collection Entry - Professional Automation System with GUI
Created by: SUSHANT
"""

import customtkinter as ctk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import threading
import time
from datetime import datetime

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class RIAutomationGUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("RI Collection Automation - SUSHANT")
        self.root.geometry("1000x700")

        self.driver = None
        self.villages = []
        self.village_checkboxes = {}
        self.village_khata_inputs = {}
        self.is_running = False
        self.results = []

        self.create_gui()

    def create_gui(self):
        # Main container with glassmorphic effect
        main_frame = ctk.CTkFrame(self.root, corner_radius=20, fg_color=("gray90", "gray13"))
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # ========== HEADER WITH LOGO ==========
        header_frame = ctk.CTkFrame(main_frame, corner_radius=15, fg_color=("white", "gray20"))
        header_frame.pack(fill="x", padx=20, pady=(20, 10))

        logo_label = ctk.CTkLabel(
            header_frame,
            text="✨ DESIGNED BY SUSHANT ✨",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color=("#1f538d", "#3a7ebf")
        )
        logo_label.pack(pady=15)

        title_label = ctk.CTkLabel(
            header_frame,
            text="RI Online Collection Entry Automation",
            font=ctk.CTkFont(size=16)
        )
        title_label.pack(pady=(0, 15))

        # ========== INPUT SECTION ==========
        input_frame = ctk.CTkFrame(main_frame, corner_radius=15, fg_color=("white", "gray20"))
        input_frame.pack(fill="x", padx=20, pady=10)

        # Mobile Number Input
        mobile_label = ctk.CTkLabel(input_frame, text="📱 Mobile Number:", font=ctk.CTkFont(size=14, weight="bold"))
        mobile_label.grid(row=0, column=0, padx=20, pady=15, sticky="w")

        self.mobile_entry = ctk.CTkEntry(
            input_frame,
            placeholder_text="Enter mobile number",
            width=200,
            height=35,
            font=ctk.CTkFont(size=14)
        )
        self.mobile_entry.insert(0, "8984750096")
        self.mobile_entry.grid(row=0, column=1, padx=10, pady=15, sticky="w")

        # Login Button
        self.login_btn = ctk.CTkButton(
            input_frame,
            text="🔐 Login & Extract Villages",
            command=self.start_login_thread,
            width=220,
            height=35,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=("#1f538d", "#3a7ebf"),
            hover_color=("#174270", "#2d5f8f")
        )
        self.login_btn.grid(row=0, column=2, padx=20, pady=15)

        # ========== VILLAGE SELECTION SECTION ==========
        self.village_frame = ctk.CTkScrollableFrame(
            main_frame,
            corner_radius=15,
            fg_color=("white", "gray20"),
            height=200
        )
        self.village_frame.pack(fill="both", expand=True, padx=20, pady=10)

        village_header = ctk.CTkLabel(
            self.village_frame,
            text="📍 Select Villages (Optional: Enter specific Khata numbers)",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        village_header.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w")

        # ========== CONTROL BUTTONS ==========
        button_frame = ctk.CTkFrame(main_frame, corner_radius=15, fg_color=("white", "gray20"))
        button_frame.pack(fill="x", padx=20, pady=10)

        self.start_btn = ctk.CTkButton(
            button_frame,
            text="▶ START AUTOMATION",
            command=self.start_automation_thread,
            width=200,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color=("green", "darkgreen"),
            hover_color=("darkgreen", "green"),
            state="disabled"
        )
        self.start_btn.pack(side="left", padx=20, pady=15)

        self.stop_btn = ctk.CTkButton(
            button_frame,
            text="⏸ STOP",
            command=self.stop_automation,
            width=150,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color=("red", "darkred"),
            hover_color=("darkred", "red"),
            state="disabled"
        )
        self.stop_btn.pack(side="left", padx=10, pady=15)

        # ========== PROGRESS SECTION ==========
        progress_frame = ctk.CTkFrame(main_frame, corner_radius=15, fg_color=("white", "gray20"))
        progress_frame.pack(fill="x", padx=20, pady=10)

        self.progress_label = ctk.CTkLabel(
            progress_frame,
            text="⏳ Status: Ready",
            font=ctk.CTkFont(size=13)
        )
        self.progress_label.pack(padx=20, pady=(15, 5))

        self.progress_bar = ctk.CTkProgressBar(progress_frame, width=900, height=20)
        self.progress_bar.pack(padx=20, pady=(5, 15))
        self.progress_bar.set(0)

        # ========== RESULTS SECTION ==========
        results_frame = ctk.CTkFrame(main_frame, corner_radius=15, fg_color=("white", "gray20"))
        results_frame.pack(fill="both", expand=True, padx=20, pady=(10, 20))

        results_label = ctk.CTkLabel(
            results_frame,
            text="📊 Results",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        results_label.pack(padx=10, pady=(10, 5))

        self.results_text = ctk.CTkTextbox(
            results_frame,
            width=900,
            height=150,
            font=ctk.CTkFont(size=12),
            fg_color=("gray95", "gray15")
        )
        self.results_text.pack(padx=10, pady=(5, 15))

    def add_result(self, message, status="info"):
        timestamp = datetime.now().strftime("%H:%M:%S")
        color_prefix = ""

        if status == "success":
            icon = "✓"
        elif status == "error":
            icon = "✗"
        elif status == "warning":
            icon = "⚠"
        else:
            icon = "ℹ"

        self.results_text.insert("end", f"[{timestamp}] {icon} {message}\n")
        self.results_text.see("end")

    def update_progress(self, message, progress=None):
        self.progress_label.configure(text=f"⏳ {message}")
        if progress is not None:
            self.progress_bar.set(progress)

    def start_login_thread(self):
        thread = threading.Thread(target=self.login_and_extract_villages, daemon=True)
        thread.start()

    def login_and_extract_villages(self):
        try:
            self.login_btn.configure(state="disabled", text="⏳ Logging in...")
            self.add_result("Initializing browser...", "info")

            # Setup Chrome
            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_experimental_option("detach", True)

            self.driver = webdriver.Chrome(options=chrome_options)

            # Navigate to login
            self.add_result("Opening login page...", "info")
            self.driver.get("https://odishalandrevenue.nic.in/DefaultLogin.aspx")
            time.sleep(2)

            self.add_result("⚠ Please login manually in the browser", "warning")
            self.update_progress("Waiting for login...")

            # Wait for login
            timeout = 300
            start_time = time.time()

            while "DefaultLogin.aspx" in self.driver.current_url:
                # Handle login errors
                try:
                    WebDriverWait(self.driver, 0.5).until(EC.alert_is_present())
                    alert = self.driver.switch_to.alert
                    alert_text = alert.text
                    self.add_result(f"Login error: {alert_text}", "warning")
                    alert.accept()
                    start_time = time.time()
                except:
                    pass

                if time.time() - start_time > timeout:
                    self.add_result("Login timeout!", "error")
                    return
                time.sleep(1)

            self.add_result("✓ Login successful!", "success")
            time.sleep(2)

            # Navigate to RI Online Collection
            self.add_result("Navigating to RI Online Collection Entry...", "info")
            ri_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "RI Online Collection Entry"))
            )
            ri_link.click()
            time.sleep(3)

            # Handle popup if present
            try:
                WebDriverWait(self.driver, 5).until(EC.alert_is_present())
                alert = self.driver.switch_to.alert
                alert.accept()
            except:
                pass

            # Extract villages
            self.add_result("Extracting village list...", "info")
            self.update_progress("Extracting villages...")

            village_dropdown = self.driver.find_element(By.XPATH, "//select[contains(@id, 'Village') or contains(@id, 'village')]")
            select = Select(village_dropdown)
            options = select.options

            self.villages = []
            for option in options[1:]:  # Skip first --Select--
                village_name = option.text.strip()
                village_value = option.get_attribute("value")
                if village_name and village_value:
                    self.villages.append({"name": village_name, "value": village_value})

            self.add_result(f"✓ Found {len(self.villages)} villages", "success")

            # Populate GUI
            self.populate_village_list()

            self.login_btn.configure(text="✓ Villages Loaded", state="disabled")
            self.start_btn.configure(state="normal")
            self.update_progress("Ready to start automation", 0)

        except Exception as e:
            self.add_result(f"Error: {str(e)}", "error")
            self.login_btn.configure(state="normal", text="🔐 Login & Extract Villages")

    def populate_village_list(self):
        # Clear existing
        for widget in self.village_frame.winfo_children()[1:]:
            widget.destroy()

        self.village_checkboxes = {}
        self.village_khata_inputs = {}

        row = 1
        for village in self.villages:
            # Checkbox
            var = ctk.BooleanVar()
            checkbox = ctk.CTkCheckBox(
                self.village_frame,
                text=village["name"],
                variable=var,
                font=ctk.CTkFont(size=13)
            )
            checkbox.grid(row=row, column=0, padx=20, pady=5, sticky="w")
            self.village_checkboxes[village["value"]] = {"var": var, "name": village["name"]}

            # Khata input
            khata_label = ctk.CTkLabel(self.village_frame, text="Khata (optional):", font=ctk.CTkFont(size=12))
            khata_label.grid(row=row, column=1, padx=10, pady=5, sticky="w")

            khata_entry = ctk.CTkEntry(
                self.village_frame,
                placeholder_text="Leave empty for all",
                width=150,
                height=30
            )
            khata_entry.grid(row=row, column=2, padx=10, pady=5, sticky="w")
            self.village_khata_inputs[village["value"]] = khata_entry

            row += 1

    def start_automation_thread(self):
        thread = threading.Thread(target=self.run_automation, daemon=True)
        thread.start()

    def run_automation(self):
        try:
            self.is_running = True
            self.start_btn.configure(state="disabled")
            self.stop_btn.configure(state="normal")
            self.results_text.delete("1.0", "end")

            mobile_number = self.mobile_entry.get().strip()
            if not mobile_number:
                self.add_result("Please enter mobile number!", "error")
                return

            # Get selected villages
            selected_villages = []
            for village_value, data in self.village_checkboxes.items():
                if data["var"].get():
                    khata_input = self.village_khata_inputs[village_value].get().strip()
                    selected_villages.append({
                        "value": village_value,
                        "name": data["name"],
                        "specific_khata": khata_input if khata_input else None
                    })

            if not selected_villages:
                self.add_result("Please select at least one village!", "error")
                self.start_btn.configure(state="normal")
                self.stop_btn.configure(state="disabled")
                return

            self.add_result(f"Starting automation for {len(selected_villages)} village(s)", "success")
            self.add_result(f"Mobile Number: {mobile_number}", "info")

            total_processed = 0
            total_success = 0
            total_already_paid = 0
            total_errors = 0

            for idx, village in enumerate(selected_villages):
                if not self.is_running:
                    self.add_result("Automation stopped by user", "warning")
                    break

                progress = idx / len(selected_villages)
                self.update_progress(f"Processing {village['name']}...", progress)

                result = self.process_village(village, mobile_number)

                total_processed += result["processed"]
                total_success += result["success"]
                total_already_paid += result["already_paid"]
                total_errors += result["errors"]

            # Final summary
            self.update_progress("Automation Complete!", 1.0)
            self.add_result("=" * 50, "info")
            self.add_result("FINAL SUMMARY", "success")
            self.add_result(f"Total Khatas Processed: {total_processed}", "info")
            self.add_result(f"✓ Successful: {total_success}", "success")
            self.add_result(f"⚠ Already Paid: {total_already_paid}", "warning")
            self.add_result(f"✗ Errors: {total_errors}", "error")
            self.add_result("=" * 50, "info")

        except Exception as e:
            self.add_result(f"Fatal error: {str(e)}", "error")
        finally:
            self.is_running = False
            self.start_btn.configure(state="normal")
            self.stop_btn.configure(state="disabled")

    def process_village(self, village, mobile_number):
        result = {"processed": 0, "success": 0, "already_paid": 0, "errors": 0}

        try:
            self.add_result(f"📍 Processing village: {village['name']}", "info")

            # Select village
            village_dropdown = self.driver.find_element(By.XPATH, "//select[contains(@id, 'Village') or contains(@id, 'village')]")
            select = Select(village_dropdown)
            select.select_by_value(village["value"])
            time.sleep(3)

            # Get khata list
            khata_dropdown = self.driver.find_element(By.XPATH, "//select[contains(@id, 'Khata') or contains(@id, 'khata')]")
            select_khata = Select(khata_dropdown)
            khata_options = select_khata.options[1:]  # Skip --Select--

            # Filter if specific khata provided
            if village["specific_khata"]:
                khata_options = [opt for opt in khata_options if village["specific_khata"] in opt.text]
                self.add_result(f"  Filtering for Khata: {village['specific_khata']}", "info")

            self.add_result(f"  Found {len(khata_options)} khata(s) to process", "info")

            for khata in khata_options:
                if not self.is_running:
                    break

                khata_text = khata.text.strip()
                result["processed"] += 1

                status = self.process_single_khata(village["name"], khata_text, mobile_number)

                if status == "success":
                    result["success"] += 1
                    self.add_result(f"  ✓ {khata_text} - Success", "success")
                elif status == "already_paid":
                    result["already_paid"] += 1
                    self.add_result(f"  ⚠ {khata_text} - Already Paid", "warning")
                else:
                    result["errors"] += 1
                    self.add_result(f"  ✗ {khata_text} - Error", "error")

            self.add_result(f"✓ Completed {village['name']}: {result['success']} success, {result['already_paid']} paid, {result['errors']} errors", "success")

        except Exception as e:
            self.add_result(f"Error processing village {village['name']}: {str(e)}", "error")

        return result

    def process_single_khata(self, village_name, khata_text, mobile_number):
        try:
            # Re-select village (page may have refreshed)
            time.sleep(2)
            village_dropdown = self.driver.find_element(By.XPATH, "//select[contains(@id, 'Village') or contains(@id, 'village')]")
            Select(village_dropdown).select_by_visible_text(village_name)
            time.sleep(3)

            # Select khata
            khata_dropdown = self.driver.find_element(By.XPATH, "//select[contains(@id, 'Khata') or contains(@id, 'khata')]")
            Select(khata_dropdown).select_by_visible_text(khata_text)
            time.sleep(3)

            # Fill depositor details
            deposited_by = self.driver.find_element(By.XPATH, "//input[@type='text' and (contains(@id, 'Deposit') or contains(@id, 'deposit'))]")
            deposited_by.clear()
            deposited_by.send_keys("self")

            mobile = self.driver.find_element(By.XPATH, "//input[@type='text' and (contains(@id, 'Mobile') or contains(@id, 'mobile'))]")
            mobile.clear()
            mobile.send_keys(mobile_number)

            time.sleep(1)

            # Click Save
            save_button = self.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Save']")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_button)
            time.sleep(1)
            self.driver.execute_script("arguments[0].click();", save_button)
            time.sleep(2)

            # Click Yes on confirmation
            xpath_variations = [
                "//input[@type='submit' and @value='Yes']",
                "//button[text()='Yes']",
                "//*[text()='Yes']"
            ]

            yes_clicked = False
            for xpath in xpath_variations:
                try:
                    elements = self.driver.find_elements(By.XPATH, xpath)
                    for elem in elements:
                        if elem.is_displayed():
                            elem.click()
                            yes_clicked = True
                            break
                    if yes_clicked:
                        break
                except:
                    continue

            time.sleep(3)

            # Check for "Already Paid" popup
            try:
                # Try to find Already Paid message
                already_paid_xpaths = [
                    "//*[contains(text(), 'Already Paid') or contains(text(), 'already paid')]",
                    "//*[contains(text(), 'ALREADY PAID')]"
                ]

                for xpath in already_paid_xpaths:
                    try:
                        elem = self.driver.find_element(By.XPATH, xpath)
                        if elem.is_displayed():
                            # Found already paid message, click OK
                            ok_xpaths = [
                                "//button[text()='OK' or text()='Ok']",
                                "//input[@type='button' and (@value='OK' or @value='Ok')]",
                                "//input[@type='submit' and (@value='OK' or @value='Ok')]",
                                "//*[text()='OK' or text()='Ok']"
                            ]

                            for ok_xpath in ok_xpaths:
                                try:
                                    ok_elements = self.driver.find_elements(By.XPATH, ok_xpath)
                                    for ok_btn in ok_elements:
                                        if ok_btn.is_displayed():
                                            ok_btn.click()
                                            time.sleep(2)
                                            return "already_paid"
                                except:
                                    continue
                    except:
                        continue
            except:
                pass

            # Close receipt window if opened
            main_window = self.driver.current_window_handle
            all_windows = self.driver.window_handles

            if len(all_windows) > 1:
                for window in all_windows:
                    if window != main_window:
                        self.driver.switch_to.window(window)
                        self.driver.close()
                        break
                self.driver.switch_to.window(main_window)

            time.sleep(2)
            return "success"

        except Exception as e:
            return "error"

    def stop_automation(self):
        self.is_running = False
        self.add_result("Stopping automation...", "warning")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = RIAutomationGUI()
    app.run()
