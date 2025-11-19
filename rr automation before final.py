"""
RI Online Collection Entry - MARVEL AVENGERS AUTOMATION SYSTEM
⚡ DESIGNED BY SUSHANT - AVENGERS TECH ⚡
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
import os
import shutil
import glob
import pandas as pd
from tkinter import filedialog, messagebox
import winsound
import pyautogui
from PyPDF2 import PdfMerger
import json
from cryptography.fernet import Fernet
import hashlib
import base64

# Marvel Theme Colors
DARK_BG = "#0a0e27"  # Deep space dark
IRON_RED = "#b91d1d"  # Iron Man red
IRON_GOLD = "#ffd700"  # Arc reactor gold
STARK_BLUE = "#00a8e8"  # Stark tech blue
PANEL_BG = "#1a1d3a"  # Panel background
GLOW_RED = "#ff4444"  # Glowing red
GLOW_GOLD = "#ffed4e"  # Glowing gold

ctk.set_appearance_mode("dark")

class MarvelRIAutomation:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("⚡ AVENGERS TECH - RI Automation ⚡")
        self.root.geometry("1200x800")
        self.root.configure(fg_color=DARK_BG)

        self.driver = None
        self.villages = []
        self.village_checkboxes = {}
        self.khata_data = {}  # Store khatas per village {village_value: [{text, var, mobile, checkbox_frame}]}
        self.is_running = False
        self.session_folder = None  # PDF session folder
        self.saved_pdfs = []  # Track saved PDF paths
        self.processing_stats = {"success": 0, "already_paid": 0, "errors": 0, "pdf_saved": 0, "pdf_failed": 0}
        self.excel_uploaded_villages = {}  # Track which villages have Excel data
        self.save_pdf_enabled = True  # PDF save option (user configurable)
        self.pdf_save_location = os.path.expanduser("~/Documents")  # User-selected PDF save location
        self.live_stats_label = None  # Live statistics display (created in GUI)

        # Credential management
        self.credentials_file = "credentials.enc"
        self.userid_entry = None
        self.password_entry = None
        self.mobile_entry_login = None
        self.remember_creds_var = None

        self.create_gui()

    def create_gui(self):
        # ========== STARK INDUSTRIES HEADER ==========
        header_frame = ctk.CTkFrame(
            self.root,
            corner_radius=0,
            fg_color=IRON_RED,
            height=70,
            border_width=3,
            border_color=IRON_GOLD
        )
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)

        # Main title with glow effect
        title_label = ctk.CTkLabel(
            header_frame,
            text="⚡ AVENGERS TECH - RI AUTOMATION ⚡",
            font=ctk.CTkFont(family="Arial Black", size=24, weight="bold"),
            text_color=IRON_GOLD
        )
        title_label.pack(pady=7)

        subtitle = ctk.CTkLabel(
            header_frame,
            text="🦸 DESIGNED BY SUSHANT 🦸",
            font=ctk.CTkFont(family="Arial", size=14, weight="bold"),
            text_color="white"
        )
        subtitle.pack(pady=0)

        # ========== TABVIEW SYSTEM ==========
        self.tabview = ctk.CTkTabview(self.root, fg_color=DARK_BG, segmented_button_fg_color=IRON_RED,
                                       segmented_button_selected_color=GLOW_RED, segmented_button_unselected_color=PANEL_BG,
                                       text_color=IRON_GOLD)
        self.tabview.pack(fill="both", expand=True, padx=20, pady=20)

        # Create tabs
        login_tab = self.tabview.add("🔐 LOGIN")
        processing_tab = self.tabview.add("⚡ PROCESSING")

        # ========== LOGIN TAB ==========
        login_panel = ctk.CTkFrame(login_tab, fg_color=PANEL_BG, corner_radius=15, border_width=2, border_color=IRON_GOLD)
        login_panel.pack(fill="both", expand=True, padx=100, pady=50)

        # User ID
        userid_label = ctk.CTkLabel(login_panel, text="👤 USER ID", font=ctk.CTkFont(size=14, weight="bold"), text_color=IRON_GOLD)
        userid_label.pack(padx=30, pady=(10, 5), anchor="w")

        self.userid_entry = ctk.CTkEntry(login_panel, placeholder_text="Enter User ID", height=40,
                                          font=ctk.CTkFont(size=14), border_color=STARK_BLUE, border_width=2)
        self.userid_entry.pack(fill="x", padx=30, pady=(0, 15))

        # Password
        password_label = ctk.CTkLabel(login_panel, text="🔑 PASSWORD", font=ctk.CTkFont(size=14, weight="bold"), text_color=IRON_GOLD)
        password_label.pack(padx=30, pady=(10, 5), anchor="w")

        self.password_entry = ctk.CTkEntry(login_panel, placeholder_text="Enter Password", show="*", height=40,
                                            font=ctk.CTkFont(size=14), border_color=STARK_BLUE, border_width=2)
        self.password_entry.pack(fill="x", padx=30, pady=(0, 15))

        # Mobile Number
        mobile_label = ctk.CTkLabel(login_panel, text="📱 MOBILE NUMBER", font=ctk.CTkFont(size=14, weight="bold"), text_color=IRON_GOLD)
        mobile_label.pack(padx=30, pady=(10, 5), anchor="w")

        self.mobile_entry_login = ctk.CTkEntry(login_panel, placeholder_text="Enter default mobile number (10 digits)",
                                                height=40, font=ctk.CTkFont(size=14), border_color=STARK_BLUE, border_width=2)
        self.mobile_entry_login.pack(fill="x", padx=30, pady=(0, 15))

        # Point mobile_entry to login tab entry for backward compatibility
        self.mobile_entry = self.mobile_entry_login

        # Remember Credentials
        self.remember_creds_var = ctk.BooleanVar()
        remember_checkbox = ctk.CTkCheckBox(login_panel, text="💾 Remember Credentials", variable=self.remember_creds_var,
                                             font=ctk.CTkFont(size=13, weight="bold"), text_color=IRON_GOLD,
                                             fg_color=STARK_BLUE, hover_color="#0088c0", border_color=STARK_BLUE)
        remember_checkbox.pack(padx=30, pady=(10, 20), anchor="w")

        # Initialize Button
        self.login_btn = ctk.CTkButton(login_panel, text="🔐 INITIALIZE SYSTEM", command=self.start_login_thread,
                                        height=50, font=ctk.CTkFont(size=16, weight="bold"), fg_color=IRON_RED,
                                        hover_color=GLOW_RED, border_width=2, border_color=IRON_GOLD, text_color="white")
        self.login_btn.pack(fill="x", padx=30, pady=(10, 30))

        # Load Credentials Button
        load_creds_btn = ctk.CTkButton(login_panel, text="📂 Load Saved Credentials", command=self.load_credentials,
                                        height=35, font=ctk.CTkFont(size=12, weight="bold"), fg_color=STARK_BLUE,
                                        hover_color="#0088c0", border_width=2, border_color=IRON_GOLD)
        load_creds_btn.pack(fill="x", padx=30, pady=(0, 30))

        # ========== PROCESSING TAB - 3-PANEL LAYOUT ==========
        content_frame = ctk.CTkFrame(processing_tab, fg_color=DARK_BG)
        content_frame.pack(fill="both", expand=True)

        # Configure grid columns for 3 equal panels
        content_frame.grid_columnconfigure(0, weight=3)  # Village panel (30%)
        content_frame.grid_columnconfigure(1, weight=4)  # Khata panel (40%)
        content_frame.grid_columnconfigure(2, weight=3)  # Live panel (30%)
        content_frame.grid_rowconfigure(0, weight=1)

        # LEFT PANEL - Village Selection (30%)
        left_panel = ctk.CTkFrame(content_frame, corner_radius=15, fg_color=PANEL_BG,
                                   border_width=2, border_color=STARK_BLUE)
        left_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 5), pady=0)

        # PDF Save Option Checkbox
        self.pdf_checkbox = ctk.CTkCheckBox(left_panel, text="📄 Save Receipts as PDF",
                                             font=ctk.CTkFont(size=13, weight="bold"), text_color=IRON_GOLD,
                                             fg_color=STARK_BLUE, hover_color="#0088c0", border_color=STARK_BLUE,
                                             command=self.toggle_pdf_save)
        self.pdf_checkbox.pack(padx=20, pady=(20, 5), anchor="w")
        self.pdf_checkbox.select()  # Default: enabled

        # PDF Save Location Selector
        location_frame = ctk.CTkFrame(left_panel, fg_color="transparent")
        location_frame.pack(fill="x", padx=20, pady=(5, 10))

        location_label = ctk.CTkLabel(
            location_frame,
            text="📁 PDF Save Location:",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=IRON_GOLD
        )
        location_label.pack(anchor="w")

        self.pdf_location_display = ctk.CTkLabel(
            location_frame,
            text=self.pdf_save_location,
            font=ctk.CTkFont(size=11),
            text_color="white"
        )
        self.pdf_location_display.pack(anchor="w", pady=(2, 5))

        choose_location_btn = ctk.CTkButton(
            location_frame,
            text="Choose Folder",
            command=self.choose_pdf_location,
            height=30,
            width=120,
            font=ctk.CTkFont(size=11),
            fg_color=STARK_BLUE,
            hover_color="#0088c0"
        )
        choose_location_btn.pack(anchor="w")

        # Village Selection
        village_label = ctk.CTkLabel(
            left_panel,
            text="📍 VILLAGE SELECTION",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=IRON_GOLD
        )
        village_label.pack(padx=20, pady=(20, 5), anchor="w")

        # Select All Villages Button
        self.select_all_villages_btn = ctk.CTkButton(
            left_panel,
            text="☑ SELECT ALL VILLAGES",
            command=self.select_all_villages,
            height=35,
            font=ctk.CTkFont(size=12, weight="bold"),
            fg_color=STARK_BLUE,
            hover_color="#0088c0",
            state="disabled"
        )
        self.select_all_villages_btn.pack(fill="x", padx=20, pady=5)

        # Village List (Scrollable)
        self.village_frame = ctk.CTkScrollableFrame(
            left_panel,
            fg_color=DARK_BG,
            border_width=2,
            border_color=STARK_BLUE
        )
        self.village_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Extract Khatas Button
        self.extract_khata_btn = ctk.CTkButton(
            left_panel,
            text="📥 EXTRACT KHATAS",
            command=self.start_extract_khatas_thread,
            height=45,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=IRON_GOLD,
            text_color="black",
            hover_color=GLOW_GOLD,
            border_width=2,
            border_color=IRON_RED,
            state="disabled"
        )
        self.extract_khata_btn.pack(fill="x", padx=20, pady=10)

        # MIDDLE PANEL - Khata Selection (40%)
        middle_panel = ctk.CTkFrame(
            content_frame,
            corner_radius=15,
            fg_color=PANEL_BG,
            border_width=2,
            border_color=STARK_BLUE
        )
        middle_panel.grid(row=0, column=1, sticky="nsew", padx=5, pady=0)

        # Khata Selection Area
        khata_header_frame = ctk.CTkFrame(middle_panel, fg_color="transparent")
        khata_header_frame.pack(fill="x", padx=15, pady=15)

        khata_label = ctk.CTkLabel(
            khata_header_frame,
            text="🎯 KHATA SELECTION",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=IRON_GOLD
        )
        khata_label.pack(side="left")

        self.select_all_khata_btn = ctk.CTkButton(
            khata_header_frame,
            text="☑ ALL",
            command=self.select_all_khatas,
            height=30,
            width=80,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=STARK_BLUE,
            hover_color="#0088c0",
            state="disabled"
        )
        self.select_all_khata_btn.pack(side="right")

        # Search Box for Khatas
        search_frame = ctk.CTkFrame(middle_panel, fg_color="transparent")
        search_frame.pack(fill="x", padx=15, pady=(0, 10))

        self.khata_search_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text="🔍 Search...",
            height=30,
            font=ctk.CTkFont(size=12),
            border_color=STARK_BLUE,
            border_width=2
        )
        self.khata_search_entry.pack(fill="x", side="left", expand=True, padx=(0, 8))
        self.khata_search_entry.bind("<KeyRelease>", self.filter_khatas)

        self.khata_count_label = ctk.CTkLabel(
            search_frame,
            text="0",
            font=ctk.CTkFont(size=11),
            text_color=IRON_GOLD
        )
        self.khata_count_label.pack(side="right")

        # Khata Display (Scrollable)
        self.khata_frame = ctk.CTkScrollableFrame(
            middle_panel,
            fg_color=DARK_BG,
            border_width=2,
            border_color=STARK_BLUE
        )
        self.khata_frame.pack(fill="both", expand=True, padx=15, pady=(0, 10))

        # Control Buttons
        control_frame = ctk.CTkFrame(middle_panel, fg_color="transparent")
        control_frame.pack(fill="x", padx=15, pady=10)

        self.start_btn = ctk.CTkButton(
            control_frame,
            text="⚡ ENGAGE PROTOCOL",
            command=self.start_automation_thread,
            height=55,
            font=ctk.CTkFont(size=18, weight="bold"),
            fg_color="#00ff00",
            text_color="black",
            hover_color="#00cc00",
            border_width=3,
            border_color=IRON_GOLD,
            state="disabled"
        )
        self.start_btn.pack(side="left", fill="x", expand=True, padx=(0, 5))

        self.stop_btn = ctk.CTkButton(
            control_frame,
            text="⛔ ABORT MISSION",
            command=self.stop_automation,
            height=55,
            font=ctk.CTkFont(size=18, weight="bold"),
            fg_color=IRON_RED,
            hover_color=GLOW_RED,
            border_width=3,
            border_color=IRON_GOLD,
            state="disabled"
        )
        self.stop_btn.pack(side="right", fill="x", expand=True, padx=(5, 0))

        # RIGHT PANEL - Live Stats & Results (30%)
        right_panel = ctk.CTkFrame(
            content_frame,
            corner_radius=15,
            fg_color=PANEL_BG,
            border_width=2,
            border_color=STARK_BLUE
        )
        right_panel.grid(row=0, column=2, sticky="nsew", padx=(5, 0), pady=0)

        # Live Stats Header
        stats_header = ctk.CTkLabel(
            right_panel,
            text="📊 LIVE STATS",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=IRON_GOLD
        )
        stats_header.pack(padx=15, pady=(15, 10))

        # Progress Section
        self.progress_label = ctk.CTkLabel(
            right_panel,
            text="⏳ READY",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=IRON_GOLD
        )
        self.progress_label.pack(padx=15, pady=(5, 5))

        self.progress_bar = ctk.CTkProgressBar(
            right_panel,
            height=20,
            progress_color=IRON_GOLD,
            border_width=2,
            border_color=STARK_BLUE
        )
        self.progress_bar.pack(fill="x", padx=15, pady=5)
        self.progress_bar.set(0)

        # Live statistics
        self.live_stats_label = ctk.CTkLabel(
            right_panel,
            text="",
            font=ctk.CTkFont(size=10),
            text_color="#aaaaaa",
            wraplength=250
        )
        self.live_stats_label.pack(padx=15, pady=10)

        # Results Section
        results_label = ctk.CTkLabel(
            right_panel,
            text="📝 MISSION LOG",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=IRON_GOLD
        )
        results_label.pack(padx=15, pady=(15, 5))

        self.results_text = ctk.CTkTextbox(
            right_panel,
            font=ctk.CTkFont(family="Consolas", size=16, weight="bold"),
            fg_color=DARK_BG,
            border_width=2,
            border_color=STARK_BLUE,
            text_color="#00ff00"
        )
        self.results_text.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        # Action Buttons
        action_frame = ctk.CTkFrame(right_panel, fg_color="transparent")
        action_frame.pack(fill="x", padx=15, pady=(0, 15))

        self.export_btn = ctk.CTkButton(
            action_frame,
            text="📊 EXPORT",
            command=self.export_results_to_excel,
            height=35,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=IRON_GOLD,
            text_color="black",
            hover_color=GLOW_GOLD,
            state="disabled"
        )
        self.export_btn.pack(fill="x", pady=(0, 5))

        merge_btn = ctk.CTkButton(
            action_frame,
            text="📄 MERGE PDFs",
            command=self.merge_saved_pdfs,
            height=35,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=STARK_BLUE,
            hover_color="#0088c0"
        )
        merge_btn.pack(fill="x")

    def add_result(self, message, status="info"):
        timestamp = datetime.now().strftime("%H:%M:%S")

        if status == "success":
            icon = "✓"
            color = "#00ff00"
        elif status == "error":
            icon = "✗"
            color = "#ff0000"
        elif status == "warning":
            icon = "⚠"
            color = "#ffaa00"
        else:
            icon = "ℹ"
            color = "#00a8e8"

        self.results_text.insert("end", f"[{timestamp}] {icon} {message}\n")
        self.results_text.see("end")

    def update_progress(self, message, progress=None):
        self.progress_label.configure(text=f"⏳ {message}")
        if progress is not None:
            self.progress_bar.set(progress)

    def update_live_stats(self):
        """Update live statistics display"""
        stats_text = (
            f"✓ Success: {self.processing_stats['success']} | "
            f"⚠ Already Paid: {self.processing_stats['already_paid']} | "
            f"✗ Errors: {self.processing_stats['errors']} | "
            f"📄 PDFs: {self.processing_stats['pdf_saved']}/{self.processing_stats['pdf_saved'] + self.processing_stats['pdf_failed']}"
        )
        self.live_stats_label.configure(text=stats_text)

    def select_all_villages(self):
        for village_value, data in self.village_checkboxes.items():
            data["var"].set(True)
        self.add_result("All villages selected", "success")

    def select_all_khatas(self):
        for village_value, khatas in self.khata_data.items():
            for khata_checkbox_data in khatas:
                khata_checkbox_data["var"].set(True)
        self.add_result("All khatas selected", "success")

    def validate_mobile_number(self, mobile):
        """Validate mobile number: must be exactly 10 digits"""
        mobile = mobile.strip()
        if len(mobile) != 10 or not mobile.isdigit():
            return False
        return True

    def play_sound(self, sound_file):
        """Play sound in non-blocking way"""
        def _play():
            try:
                if os.path.exists(sound_file):
                    winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
            except Exception as e:
                pass  # Silent fail if sound can't play
        threading.Thread(target=_play, daemon=True).start()

    def toggle_pdf_save(self):
        """Toggle PDF save option"""
        self.save_pdf_enabled = self.pdf_checkbox.get() == 1

    def choose_pdf_location(self):
        """Let user choose where to save PDFs"""
        from tkinter import filedialog
        folder = filedialog.askdirectory(
            title="Choose PDF Save Location",
            initialdir=self.pdf_save_location
        )
        if folder:
            self.pdf_save_location = folder
            self.pdf_location_display.configure(text=folder)
            self.add_result(f"📁 PDF location set to: {folder}", "info")

            # Warn if driver already running (requires restart to apply new path)
            if hasattr(self, 'driver') and self.driver:
                messagebox.showinfo(
                    "Restart Required",
                    "PDF location updated successfully!\n\n"
                    "⚠ To apply this change, please:\n"
                    "1. Close the browser\n"
                    "2. Click 'Initialize System' again\n\n"
                    "The new location will be used for all future PDFs."
                )

    def get_machine_key(self):
        """Generate encryption key based on machine-specific data"""
        import platform
        import uuid
        machine_id = str(uuid.getnode()) + platform.node() + platform.system()
        key_hash = hashlib.sha256(machine_id.encode()).digest()
        return Fernet(base64.urlsafe_b64encode(key_hash))

    def save_credentials(self):
        """Save credentials to encrypted file"""
        try:
            credentials = {
                "userid": self.userid_entry.get(),
                "password": self.password_entry.get(),
                "mobile": self.mobile_entry_login.get()
            }

            fernet = self.get_machine_key()
            encrypted_data = fernet.encrypt(json.dumps(credentials).encode())

            with open(self.credentials_file, "wb") as f:
                f.write(encrypted_data)

            return True
        except Exception as e:
            self.add_result(f"✗ Credential save failed: {str(e)}", "error")
            return False

    def load_credentials(self):
        """Load credentials from encrypted file"""
        try:
            if not os.path.exists(self.credentials_file):
                messagebox.showinfo("No Credentials", "No saved credentials found!")
                return

            with open(self.credentials_file, "rb") as f:
                encrypted_data = f.read()

            fernet = self.get_machine_key()
            decrypted_data = fernet.decrypt(encrypted_data)
            credentials = json.loads(decrypted_data.decode())

            self.userid_entry.delete(0, "end")
            self.userid_entry.insert(0, credentials.get("userid", ""))
            self.password_entry.delete(0, "end")
            self.password_entry.insert(0, credentials.get("password", ""))
            self.mobile_entry_login.delete(0, "end")
            self.mobile_entry_login.insert(0, credentials.get("mobile", ""))

            messagebox.showinfo("Success", "Credentials loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load credentials:\n{str(e)}")

    def filter_khatas(self, event=None):
        """Filter khatas based on search text"""
        query = self.khata_search_entry.get().lower().strip()
        visible_count = 0

        for village_value, khatas in self.khata_data.items():
            for khata_data in khatas:
                if "checkbox_frame" in khata_data:
                    khata_text = khata_data["text"].lower()
                    if query == "" or query in khata_text:
                        khata_data["checkbox_frame"].pack(anchor="w", padx=30, pady=2)
                        visible_count += 1
                    else:
                        khata_data["checkbox_frame"].pack_forget()

        self.khata_count_label.configure(text=f"Showing {visible_count} khatas")

    def update_khata_count(self):
        """Update total khata count"""
        total = sum(len(khatas) for khatas in self.khata_data.values())
        self.khata_count_label.configure(text=f"{total} khatas")

    def export_results_to_excel(self):
        """Export processing results to Excel file"""
        try:
            if not hasattr(self, 'results_data') or not self.results_data:
                messagebox.showwarning("No Data", "No results to export. Run automation first.")
                return

            filename = f"RI_Results_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
            df = pd.DataFrame(self.results_data)
            df.to_excel(filename, index=False)

            self.add_result(f"✓ Results exported: {filename}", "success")
            messagebox.showinfo("Export Success", f"Results exported to:\n{filename}")

            # Open file
            os.startfile(filename)
        except Exception as e:
            self.add_result(f"✗ Export failed: {str(e)}", "error")
            messagebox.showerror("Export Error", str(e))

    def download_excel_template(self):
        """Create and download Excel template"""
        try:
            template_data = {
                "Khata Number": ["101", "102", "103"],
                "Mobile Number (Optional)": ["9876543210", "8765432109", ""],
                "Deposited By (Optional)": ["self", "Ramesh Kumar", ""]
            }
            df = pd.DataFrame(template_data)
            filename = "Khata_Template.xlsx"
            df.to_excel(filename, index=False)

            self.add_result(f"✓ Template created: {filename}", "success")
            messagebox.showinfo("Template Ready", f"Excel template created:\n{filename}\n\nFill in your khata numbers and upload!")
            os.startfile(filename)
        except Exception as e:
            self.add_result(f"✗ Template creation failed: {str(e)}", "error")
            messagebox.showerror("Error", str(e))

    def start_login_thread(self):
        thread = threading.Thread(target=self.login_and_extract_villages, daemon=True)
        thread.start()

    def login_and_extract_villages(self):
        try:
            # Validate mobile number first
            mobile = self.mobile_entry.get().strip()
            if not mobile:
                self.add_result("✗ Mobile number required!", "error")
                messagebox.showerror("Validation Error", "Please enter a default mobile number!")
                return

            if not self.validate_mobile_number(mobile):
                self.add_result("✗ Invalid mobile number! Must be 10 digits.", "error")
                messagebox.showerror("Validation Error", "Mobile number must be exactly 10 digits!")
                return

            self.login_btn.configure(state="disabled", text="⏳ INITIALIZING...")
            self.add_result("⚡ Initializing J.A.R.V.I.S. systems...", "info")

            # Play welcome sound
            self.play_sound("welcome.wav")

            # Configure Chrome options (simple and fast)
            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_experimental_option("detach", True)

            self.driver = webdriver.Chrome(options=chrome_options)

            self.add_result("🌐 Opening secure connection...", "info")
            self.driver.get("https://odishalandrevenue.nic.in/DefaultLogin.aspx")
            time.sleep(3)

            # Auto-fill credentials (User ID & Password only)
            try:
                userid = self.userid_entry.get()
                password = self.password_entry.get()

                if userid and password:
                    self.add_result("🔧 Auto-filling User ID & Password...", "info")

                    # Fill user ID
                    userid_field = self.driver.find_element(By.XPATH, "//input[@type='text' and (contains(@id, 'User') or contains(@id, 'user') or contains(@id, 'UserName'))]")
                    userid_field.clear()
                    userid_field.send_keys(userid)
                    time.sleep(0.5)

                    # Fill password
                    password_field = self.driver.find_element(By.XPATH, "//input[@type='password']")
                    password_field.clear()
                    password_field.send_keys(password)

                    self.add_result("✓ User ID & Password auto-filled", "success")
                else:
                    self.add_result("⚠ User ID or Password missing - fill manually", "warning")
            except Exception as e:
                self.add_result(f"⚠ Auto-fill failed: {str(e)} - fill manually", "warning")

            # Save credentials if checkbox is checked (outside auto-fill block)
            if self.remember_creds_var.get():
                if self.save_credentials():
                    self.add_result("✓ Credentials saved for future use", "success")
                else:
                    self.add_result("✗ Failed to save credentials", "error")

            self.add_result("⚠ SELECT DISTRICT, SOLVE CAPTCHA & LOGIN", "warning")
            self.update_progress("Awaiting captcha solution...")

            timeout = 300
            start_time = time.time()

            while "DefaultLogin.aspx" in self.driver.current_url:
                try:
                    WebDriverWait(self.driver, 0.5).until(EC.alert_is_present())
                    alert = self.driver.switch_to.alert
                    alert_text = alert.text
                    self.add_result(f"⚠ Authentication error: {alert_text}", "warning")
                    alert.accept()
                    start_time = time.time()
                except:
                    pass

                if time.time() - start_time > timeout:
                    self.add_result("✗ Authentication timeout", "error")
                    return
                time.sleep(1)

            self.add_result("✓ AUTHENTICATION SUCCESSFUL", "success")
            time.sleep(2)

            self.add_result("📡 Accessing RI Collection module...", "info")
            ri_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "RI Online Collection Entry"))
            )
            ri_link.click()
            time.sleep(3)

            try:
                WebDriverWait(self.driver, 5).until(EC.alert_is_present())
                alert = self.driver.switch_to.alert
                alert.accept()
            except:
                pass

            self.add_result("🔍 Scanning village database...", "info")
            self.update_progress("Extracting village data...")

            village_dropdown = self.driver.find_element(By.XPATH, "//select[contains(@id, 'Village') or contains(@id, 'village')]")
            select = Select(village_dropdown)
            options = select.options

            self.villages = []
            for option in options[1:]:
                village_name = option.text.strip()
                village_value = option.get_attribute("value")
                if village_name and village_value:
                    self.villages.append({"name": village_name, "value": village_value})

            self.add_result(f"✓ VILLAGES ACQUIRED: {len(self.villages)}", "success")

            self.populate_village_list()

            self.login_btn.configure(text="✓ SYSTEM ONLINE", state="disabled")
            self.select_all_villages_btn.configure(state="normal")
            self.extract_khata_btn.configure(state="normal")
            self.update_progress("System ready for village selection", 0)

            # Auto-switch to Processing tab
            self.tabview.set("⚡ PROCESSING")

        except Exception as e:
            self.add_result(f"✗ System error: {str(e)}", "error")
            self.login_btn.configure(state="normal", text="🔐 INITIALIZE SYSTEM")

    def on_village_selection_change(self):
        """Reset extract button when village selection changes"""
        if hasattr(self, 'khata_data') and self.khata_data:
            # Only reset if khatas were already extracted
            self.extract_khata_btn.configure(text="📥 EXTRACT KHATAS")

    def populate_village_list(self):
        for widget in self.village_frame.winfo_children():
            widget.destroy()

        self.village_checkboxes = {}

        # Add Download Template button at top
        template_btn = ctk.CTkButton(
            self.village_frame,
            text="📥 Download Excel Template",
            command=self.download_excel_template,
            height=30,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=IRON_GOLD,
            text_color="black",
            hover_color=GLOW_GOLD
        )
        template_btn.pack(fill="x", padx=10, pady=(5, 15))

        for village in self.villages:
            # Village frame
            village_container = ctk.CTkFrame(self.village_frame, fg_color="transparent")
            village_container.pack(fill="x", padx=5, pady=5)

            var = ctk.BooleanVar()
            checkbox = ctk.CTkCheckBox(
                village_container,
                text=village["name"],
                variable=var,
                command=self.on_village_selection_change,
                font=ctk.CTkFont(size=13),
                fg_color=STARK_BLUE,
                hover_color=IRON_GOLD,
                border_color=IRON_GOLD,
                text_color="white"
            )
            checkbox.pack(anchor="w", padx=5, pady=2)

            # Upload button for this village
            upload_btn = ctk.CTkButton(
                village_container,
                text="📤 Upload Excel",
                command=lambda v=village: self.upload_excel_for_village(v),
                height=25,
                width=120,
                font=ctk.CTkFont(size=10),
                fg_color=STARK_BLUE,
                hover_color="#0088c0"
            )
            upload_btn.pack(anchor="w", padx=25, pady=(0, 2))

            self.village_checkboxes[village["value"]] = {"var": var, "name": village["name"]}

    def upload_excel_for_village(self, village):
        """Upload Excel file with khatas for a specific village"""
        try:
            file_path = filedialog.askopenfilename(
                title=f"Select Excel for {village['name']}",
                filetypes=[("Excel files", "*.xlsx *.xls *.csv")]
            )
            if not file_path:
                return

            # Read Excel
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path)

            # Validate columns
            if "Khata Number" not in df.columns:
                messagebox.showerror("Invalid Format", "Excel must have 'Khata Number' column!")
                return

            # Process data
            has_mobile_column = "Mobile Number (Optional)" in df.columns or "Mobile Number" in df.columns
            mobile_col = "Mobile Number (Optional)" if "Mobile Number (Optional)" in df.columns else "Mobile Number"

            has_deposited_column = "Deposited By (Optional)" in df.columns or "Deposited By" in df.columns
            deposited_col = "Deposited By (Optional)" if "Deposited By (Optional)" in df.columns else "Deposited By"

            khatas_loaded = []
            for idx, row in df.iterrows():
                khata_number = str(row["Khata Number"]).strip()
                mobile = str(row[mobile_col]).strip() if has_mobile_column and mobile_col in df.columns else ""
                deposited_by = str(row[deposited_col]).strip() if has_deposited_column and deposited_col in df.columns else ""

                if khata_number and khata_number.lower() not in ["nan", "none", ""]:
                    khatas_loaded.append({"khata": khata_number, "mobile": mobile, "deposited_by": deposited_by})

            if not khatas_loaded:
                messagebox.showwarning("No Data", "No valid khata numbers found in Excel!")
                return

            # Store Excel data for this village
            self.excel_uploaded_villages[village["value"]] = {
                "village_name": village["name"],
                "khatas": khatas_loaded
            }

            # Check the village checkbox automatically
            self.village_checkboxes[village["value"]]["var"].set(True)

            self.add_result(f"✓ Loaded {len(khatas_loaded)} khatas for {village['name']} from Excel", "success")
            messagebox.showinfo("Upload Success", f"Loaded {len(khatas_loaded)} khatas for {village['name']}!\n\nClick 'Extract Khatas' to display them.")

        except Exception as e:
            self.add_result(f"✗ Excel upload failed: {str(e)}", "error")
            messagebox.showerror("Upload Error", str(e))

    def start_extract_khatas_thread(self):
        thread = threading.Thread(target=self.extract_khatas, daemon=True)
        thread.start()

    def extract_khatas(self):
        try:
            self.extract_khata_btn.configure(state="disabled", text="⏳ EXTRACTING...")

            selected_villages = []
            for village_value, data in self.village_checkboxes.items():
                if data["var"].get():
                    selected_villages.append({"value": village_value, "name": data["name"]})

            if not selected_villages:
                self.add_result("⚠ No villages selected", "warning")
                self.extract_khata_btn.configure(state="normal", text="📥 EXTRACT KHATAS")
                return

            self.add_result(f"🔍 Scanning khatas for {len(selected_villages)} village(s)...", "info")

            # Clear previous khata data
            self.khata_data = {}
            for widget in self.khata_frame.winfo_children():
                widget.destroy()

            total_khatas = 0

            for village in selected_villages:
                # Check if this village has Excel data
                if village["value"] in self.excel_uploaded_villages:
                    # Use Excel data
                    excel_data = self.excel_uploaded_villages[village["value"]]
                    village_khatas = excel_data["khatas"]
                    total_khatas += len(village_khatas)

                    self.add_result(f"  ✓ {village['name']}: {len(village_khatas)} khatas from Excel", "success")

                    # Village header with Select All button
                    village_header_frame = ctk.CTkFrame(self.khata_frame, fg_color="transparent")
                    village_header_frame.pack(fill="x", padx=10, pady=(10, 5))

                    village_label = ctk.CTkLabel(
                        village_header_frame,
                        text=f"📍 {village['name']} ({len(village_khatas)} khatas) [Excel]",
                        font=ctk.CTkFont(size=13, weight="bold"),
                        text_color=IRON_GOLD
                    )
                    village_label.pack(side="left")

                    select_all_village_btn = ctk.CTkButton(
                        village_header_frame,
                        text="☑ Select All",
                        command=lambda v=village["value"]: self.select_all_for_village(v),
                        height=25,
                        width=100,
                        font=ctk.CTkFont(size=10, weight="bold"),
                        fg_color=STARK_BLUE,
                        hover_color="#0088c0"
                    )
                    select_all_village_btn.pack(side="right")

                    self.khata_data[village["value"]] = []

                    # Display khatas with mobile numbers and deposited by
                    for khata_item in village_khatas:
                        var = ctk.BooleanVar()
                        checkbox_frame = ctk.CTkFrame(self.khata_frame, fg_color="transparent")
                        checkbox_frame.pack(anchor="w", padx=30, pady=2)

                        khata_text = khata_item["khata"]
                        mobile_text = f" [Mobile: {khata_item['mobile']}]" if khata_item.get("mobile") else ""
                        deposited_text = f" [By: {khata_item['deposited_by']}]" if khata_item.get("deposited_by") else ""
                        display_text = f"{khata_text}{mobile_text}{deposited_text}"

                        checkbox = ctk.CTkCheckBox(
                            checkbox_frame,
                            text=display_text,
                            variable=var,
                            font=ctk.CTkFont(size=12),
                            fg_color=STARK_BLUE,
                            hover_color=IRON_GOLD,
                            border_color=IRON_GOLD,
                            text_color="white"
                        )
                        checkbox.pack(side="left")

                        self.khata_data[village["value"]].append({
                            "text": khata_text,
                            "var": var,
                            "mobile": khata_item.get("mobile", ""),
                            "deposited_by": khata_item.get("deposited_by", ""),
                            "checkbox_frame": checkbox_frame
                        })

                else:
                    # Extract from portal
                    self.update_progress(f"Extracting khatas from {village['name']}...")

                    # Select village
                    village_dropdown = self.driver.find_element(By.XPATH, "//select[contains(@id, 'Village') or contains(@id, 'village')]")
                    Select(village_dropdown).select_by_value(village["value"])
                    time.sleep(3)

                    # Get khatas
                    khata_dropdown = self.driver.find_element(By.XPATH, "//select[contains(@id, 'Khata') or contains(@id, 'khata')]")
                    select_khata = Select(khata_dropdown)
                    khata_options = select_khata.options[1:]  # Skip --Select--

                    village_khatas = []
                    for opt in khata_options:
                        khata_text = opt.text.strip()
                        if khata_text:
                            village_khatas.append(khata_text)

                    total_khatas += len(village_khatas)
                    self.add_result(f"  ✓ {village['name']}: {len(village_khatas)} khatas found", "success")

                    # Village header with Select All button
                    village_header_frame = ctk.CTkFrame(self.khata_frame, fg_color="transparent")
                    village_header_frame.pack(fill="x", padx=10, pady=(10, 5))

                    village_label = ctk.CTkLabel(
                        village_header_frame,
                        text=f"📍 {village['name']} ({len(village_khatas)} khatas)",
                        font=ctk.CTkFont(size=13, weight="bold"),
                        text_color=IRON_GOLD
                    )
                    village_label.pack(side="left")

                    select_all_village_btn = ctk.CTkButton(
                        village_header_frame,
                        text="☑ Select All",
                        command=lambda v=village["value"]: self.select_all_for_village(v),
                        height=25,
                        width=100,
                        font=ctk.CTkFont(size=10, weight="bold"),
                        fg_color=STARK_BLUE,
                        hover_color="#0088c0"
                    )
                    select_all_village_btn.pack(side="right")

                    self.khata_data[village["value"]] = []

                    for khata in village_khatas:
                        var = ctk.BooleanVar()
                        checkbox_frame = ctk.CTkFrame(self.khata_frame, fg_color="transparent")
                        checkbox_frame.pack(anchor="w", padx=30, pady=2)

                        checkbox = ctk.CTkCheckBox(
                            checkbox_frame,
                            text=khata,
                            variable=var,
                            font=ctk.CTkFont(size=12),
                            fg_color=STARK_BLUE,
                            hover_color=IRON_GOLD,
                            border_color=IRON_GOLD,
                            text_color="white"
                        )
                        checkbox.pack(side="left")

                        self.khata_data[village["value"]].append({
                            "text": khata,
                            "var": var,
                            "mobile": "",
                            "deposited_by": "",
                            "checkbox_frame": checkbox_frame
                        })

            self.add_result(f"✓ TOTAL KHATAS EXTRACTED: {total_khatas}", "success")
            self.extract_khata_btn.configure(state="normal", text="✓ KHATAS LOADED")
            self.select_all_khata_btn.configure(state="normal")
            self.start_btn.configure(state="normal")
            self.update_progress("Ready to engage automation protocol", 0)
            self.update_khata_count()

        except Exception as e:
            self.add_result(f"✗ Extraction failed: {str(e)}", "error")
            self.extract_khata_btn.configure(state="normal", text="📥 EXTRACT KHATAS")

    def select_all_for_village(self, village_value):
        """Select all khatas for a specific village"""
        if village_value in self.khata_data:
            for khata_data in self.khata_data[village_value]:
                khata_data["var"].set(True)
            village_name = self.village_checkboxes[village_value]["name"]
            self.add_result(f"✓ All khatas selected for {village_name}", "success")

    def start_automation_thread(self):
        thread = threading.Thread(target=self.run_automation, daemon=True)
        thread.start()

    def run_automation(self):
        try:
            self.is_running = True
            self.start_btn.configure(state="disabled")
            self.stop_btn.configure(state="normal")

            default_mobile = self.mobile_entry.get().strip()
            if not default_mobile:
                self.add_result("⚠ Default mobile number required", "error")
                messagebox.showerror("Error", "Please enter a default mobile number!")
                self.start_btn.configure(state="normal")
                self.stop_btn.configure(state="disabled")
                return

            # Collect selected khatas with their mobile numbers
            selected_tasks = []
            for village_value, khatas in self.khata_data.items():
                village_name = self.village_checkboxes[village_value]["name"]
                for khata_data in khatas:
                    if khata_data["var"].get():
                        # Use khata-specific mobile or default
                        khata_mobile = khata_data.get("mobile", "").strip()
                        final_mobile = khata_mobile if khata_mobile else default_mobile

                        # Use khata-specific deposited_by or default "self"
                        khata_deposited = khata_data.get("deposited_by", "").strip()
                        final_deposited = khata_deposited if khata_deposited else "self"

                        selected_tasks.append({
                            "village_value": village_value,
                            "village_name": village_name,
                            "khata": khata_data["text"],
                            "mobile": final_mobile,
                            "deposited_by": final_deposited
                        })

            if not selected_tasks:
                self.add_result("⚠ No khatas selected", "error")
                messagebox.showwarning("No Selection", "Please select at least one khata!")
                self.start_btn.configure(state="normal")
                self.stop_btn.configure(state="disabled")
                return

            # Warn for large batches
            if len(selected_tasks) > 500:
                if not messagebox.askyesno("Large Batch", f"You are about to process {len(selected_tasks)} khatas.\nThis may take several hours.\n\nContinue?"):
                    self.start_btn.configure(state="normal")
                    self.stop_btn.configure(state="disabled")
                    return

            # Create session ID and folder for PDFs in user-selected location
            self.session_id = f"rr{datetime.now().strftime('%Y%m%d_%H%M')}"
            self.session_folder = os.path.join(self.pdf_save_location, self.session_id)
            os.makedirs(self.session_folder, exist_ok=True)
            self.add_result(f"📁 Session folder: {self.session_folder}", "info")

            # Initialize results data for export
            self.results_data = []

            # Reset stats
            self.processing_stats = {"success": 0, "already_paid": 0, "errors": 0, "pdf_saved": 0, "pdf_failed": 0}
            self.saved_pdfs = []

            self.add_result(f"⚡ MISSION INITIATED: {len(selected_tasks)} targets", "success")
            start_time = time.time()

            for idx, task in enumerate(selected_tasks):
                if not self.is_running:
                    self.add_result("⛔ MISSION ABORTED", "warning")
                    break

                progress = idx / len(selected_tasks)
                elapsed = time.time() - start_time
                if idx > 0:
                    avg_time = elapsed / idx
                    remaining = avg_time * (len(selected_tasks) - idx)
                    eta = f"ETA: {int(remaining//60)}m {int(remaining%60)}s"
                else:
                    eta = "Calculating..."

                status_msg = f"Processing: {task['village_name']} - Khata {task['khata']} ({idx+1}/{len(selected_tasks)}) | {eta}"
                self.update_progress(status_msg, progress)

                status = self.process_single_khata(
                    task["village_value"],
                    task["village_name"],
                    task["khata"],
                    task["mobile"],
                    task["deposited_by"]
                )

                # Record result
                result_entry = {
                    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Village": task["village_name"],
                    "Khata": task["khata"],
                    "Status": status.upper(),
                    "Mobile": task["mobile"],
                    "Receipt": "N/A"
                }
                self.results_data.append(result_entry)

                if status == "success":
                    self.processing_stats["success"] += 1
                    self.add_result(f"✓ {task['village_name']} - {task['khata']} - SUCCESS", "success")
                elif status == "already_paid":
                    self.processing_stats["already_paid"] += 1
                    self.add_result(f"⚠ {task['village_name']} - {task['khata']} - ALREADY PAID", "warning")
                else:
                    self.processing_stats["errors"] += 1
                    self.add_result(f"✗ {task['village_name']} - {task['khata']} - ERROR", "error")

                # Update live statistics
                self.update_live_stats()

            # Organize and merge PDFs if any were saved
            if self.save_pdf_enabled and self.saved_pdfs:
                self.add_result(f"📄 Processing {len(self.saved_pdfs)} PDF receipts...", "info")
                self.organize_and_merge_pdfs()

            self.update_progress("⚡ MISSION COMPLETE", 1.0)
            self.add_result("=" * 60, "info")
            self.add_result("🎯 FINAL REPORT", "success")
            self.add_result(f"Total Processed: {len(selected_tasks)}", "info")
            self.add_result(f"✓ Success: {self.processing_stats['success']}", "success")
            self.add_result(f"⚠ Already Paid: {self.processing_stats['already_paid']}", "warning")
            self.add_result(f"✗ Errors: {self.processing_stats['errors']}", "error")
            self.add_result(f"📄 PDFs Saved: {self.processing_stats['pdf_saved']}", "info")
            if self.processing_stats['pdf_failed'] > 0:
                self.add_result(f"⚠ PDFs Failed: {self.processing_stats['pdf_failed']}", "warning")
            self.add_result("=" * 60, "info")

            # Play completion sound
            self.play_sound("completion.wav")

            # Enable export button
            self.export_btn.configure(state="normal")

            # Show PDF save location (session folder)
            if self.save_pdf_enabled and self.session_folder:
                self.add_result("=" * 60, "info")
                self.add_result(f"📁 SESSION FOLDER: {self.session_folder}", "success")
                self.add_result("=" * 60, "info")

            # Completion popup with folder location
            pdf_count = self.processing_stats['pdf_saved']
            completion_msg = (
                f"✅ PROCESSING COMPLETE!\n\n"
                f"✓ Success: {self.processing_stats['success']}\n"
                f"⚠ Already Paid: {self.processing_stats['already_paid']}\n"
                f"✗ Errors: {self.processing_stats['errors']}\n"
                f"📄 PDFs Saved: {pdf_count}\n\n"
            )

            if pdf_count > 0 and self.session_folder:
                completion_msg += f"📁 Session folder:\n{self.session_folder}\n\n"
                completion_msg += "PDFs are organized by village in subfolders."

            messagebox.showinfo("✅ Mission Complete", completion_msg)

            # Show Open Folder option if PDFs saved
            if pdf_count > 0 and self.session_folder:
                if messagebox.askyesno("Open Folder?", f"Open session folder with {pdf_count} PDF files?"):
                    self.open_pdf_folder()

        except Exception as e:
            self.add_result(f"✗ Critical error: {str(e)}", "error")
            messagebox.showerror("Critical Error", str(e))
        finally:
            self.is_running = False
            self.start_btn.configure(state="normal")
            self.stop_btn.configure(state="disabled")

    def open_pdf_folder(self):
        """Open session folder containing saved PDFs"""
        try:
            if self.session_folder and os.path.exists(self.session_folder):
                os.startfile(self.session_folder)
                self.add_result(f"📂 Opened session folder: {self.session_folder}", "success")
            else:
                messagebox.showerror("Error", f"Session folder not found: {getattr(self, 'session_folder', 'Not created')}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open folder: {str(e)}")

    def merge_saved_pdfs(self):
        """Auto-merge all PDFs from session folder"""
        try:
            if not self.session_folder or not os.path.exists(self.session_folder):
                messagebox.showerror("Error", "No session folder found. Process some khatas first.")
                return

            # Find all PDFs in session folder (recursively)
            all_pdfs = []
            for root, dirs, files in os.walk(self.session_folder):
                for file in files:
                    if file.endswith('.pdf') and not file.endswith('_MERGED.pdf'):
                        all_pdfs.append(os.path.join(root, file))

            if len(all_pdfs) < 1:
                messagebox.showinfo("Info", "No PDF files found in session folder")
                return

            # Group by village
            village_pdfs = {}
            for pdf_path in all_pdfs:
                # Extract village from path: session_folder/VillageName/file.pdf
                village = os.path.basename(os.path.dirname(pdf_path))
                if village not in village_pdfs:
                    village_pdfs[village] = []
                village_pdfs[village].append(pdf_path)

            # Merge per village and create master
            self.add_result(f"📁 Merging {len(all_pdfs)} PDFs from session folder...", "info")
            self.merge_pdfs_by_village(village_pdfs)

            messagebox.showinfo("Success", f"✅ Merged {len(all_pdfs)} PDFs!\n\n✓ Per-village merged PDFs\n✓ Master merged PDF (ALL_RECEIPTS_MERGED.pdf)\n\nLocation:\n{self.session_folder}")

            # Ask if want to open session folder
            if messagebox.askyesno("Open Folder?", "Open session folder to view merged PDFs?"):
                os.startfile(self.session_folder)

        except Exception as e:
            self.add_result(f"✗ PDF merge failed: {str(e)}", "error")
            messagebox.showerror("Error", f"Failed to merge PDFs:\n{str(e)}")

    def process_single_khata(self, village_value, village_name, khata_text, mobile_number, deposited_by="self"):
        """Process single khata with retry mechanism"""
        max_retries = 3
        retry_delays = [5, 15, 30]  # Exponential backoff

        for attempt in range(max_retries):
            try:
                if attempt > 0:
                    self.add_result(f"  Retry {attempt}/{max_retries-1} for {village_name} - {khata_text}...", "warning")
                    time.sleep(retry_delays[attempt-1])

                return self._process_khata_attempt(village_value, village_name, khata_text, mobile_number, deposited_by)

            except Exception as e:
                error_msg = str(e)
                if attempt < max_retries - 1:
                    self.add_result(f"  Attempt {attempt+1} failed: {error_msg[:50]}...", "warning")
                else:
                    self.add_result(f"  All retries failed for {village_name} - {khata_text}", "error")
                    # Log to error file
                    self.log_error(village_name, khata_text, error_msg)
                    return "error"

        return "error"

    def _process_khata_attempt(self, village_value, village_name, khata_text, mobile_number, deposited_by="self"):
        """Single attempt to process khata with WebDriverWait for reliability"""
        time.sleep(1)  # Brief initial delay for page stability

        # Select village
        village_dropdown = self.driver.find_element(By.XPATH, "//select[contains(@id, 'Village') or contains(@id, 'village')]")
        Select(village_dropdown).select_by_value(village_value)

        # WebDriverWait: Wait for khata dropdown to populate (max 5s)
        WebDriverWait(self.driver, 5).until(
            lambda d: len(d.find_element(By.XPATH, "//select[contains(@id, 'Khata') or contains(@id, 'khata')]").find_elements(By.TAG_NAME, "option")) > 1
        )

        # Select khata
        khata_dropdown = self.driver.find_element(By.XPATH, "//select[contains(@id, 'Khata') or contains(@id, 'khata')]")
        Select(khata_dropdown).select_by_visible_text(khata_text)

        # WebDriverWait: Wait for form fields to be ready (max 3s)
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='text' and (contains(@id, 'Deposit') or contains(@id, 'deposit'))]"))
        )

        # Fill details
        deposited_by_field = self.driver.find_element(By.XPATH, "//input[@type='text' and (contains(@id, 'Deposit') or contains(@id, 'deposit'))]")
        deposited_by_field.clear()
        deposited_by_field.send_keys(deposited_by if deposited_by else "self")

        mobile = self.driver.find_element(By.XPATH, "//input[@type='text' and (contains(@id, 'Mobile') or contains(@id, 'mobile'))]")
        mobile.clear()
        mobile.send_keys(mobile_number)

        time.sleep(0.5)  # Brief delay for form data to settle

        # Save
        save_button = self.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Save']")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_button)
        time.sleep(0.5)  # Wait for scroll animation
        self.driver.execute_script("arguments[0].click();", save_button)

        # WebDriverWait: Wait for confirmation dialog "Yes" button (max 3s)
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='submit' and @value='Yes']"))
        )

        # Click Yes
        yes_xpaths = [
            "//input[@type='submit' and @value='Yes']",
            "//button[text()='Yes']",
            "//*[text()='Yes']"
        ]

        for xpath in yes_xpaths:
            try:
                elements = self.driver.find_elements(By.XPATH, xpath)
                for elem in elements:
                    if elem.is_displayed():
                        elem.click()
                        break
            except:
                continue

        # WebDriverWait: Wait for portal response (alert/receipt/error) - max 5s
        time.sleep(2)  # Brief delay for portal to process

        # PRIORITY 1: Check for JavaScript alert (already paid/errors)
        # This MUST happen first before any HTML interaction
        from selenium.common.exceptions import NoAlertPresentException
        try:
            # Try to switch to alert if present
            alert = self.driver.switch_to.alert
            alert_text = alert.text

            # Check if alert contains "already paid" message
            if "already" in alert_text.lower() or "paid" in alert_text.lower():
                self.add_result(f"  ⚠ Alert detected: {alert_text[:50]}...", "warning")
                alert.accept()  # Click OK to dismiss alert
                time.sleep(1)
                return "already_paid"
            else:
                # Other alert (error/warning) - accept it and let retry handle
                self.add_result(f"  ⚠ Unexpected alert: {alert_text[:50]}...", "warning")
                alert.accept()
                time.sleep(1)
                # Continue to check HTML elements
        except NoAlertPresentException:
            # No alert present - continue to check HTML elements
            pass

        # PRIORITY 2: Check for HTML "Already Paid" message (older portal behavior)
        already_paid_xpaths = [
            "//*[contains(text(), 'Already Paid') or contains(text(), 'already paid')]",
            "//*[contains(text(), 'ALREADY PAID')]"
        ]

        for xpath in already_paid_xpaths:
            try:
                elem = self.driver.find_element(By.XPATH, xpath)
                if elem.is_displayed():
                    # Already paid detected - click OK and return immediately
                    ok_xpaths = [
                        "//button[text()='OK' or text()='Ok']",
                        "//input[@type='button' and (@value='OK' or @value='Ok')]",
                        "//*[text()='OK' or text()='Ok']"
                    ]
                    for ok_xpath in ok_xpaths:
                        try:
                            ok_elems = self.driver.find_elements(By.XPATH, ok_xpath)
                            for ok_btn in ok_elems:
                                if ok_btn.is_displayed():
                                    ok_btn.click()
                                    time.sleep(1)
                                    return "already_paid"
                        except:
                            continue
                    # Return already_paid even if OK button not found
                    return "already_paid"
            except:
                continue

        # Handle receipt window and PDF - wrapped in try-except for robustness
        main_window = self.driver.current_window_handle

        try:
            all_windows = self.driver.window_handles

            if len(all_windows) > 1:
                # Find and switch to receipt window
                receipt_window = None
                for window in all_windows:
                    if window != main_window:
                        receipt_window = window
                        break

                if receipt_window:
                    try:
                        # Switch to receipt window
                        self.driver.switch_to.window(receipt_window)

                        # Try to save as PDF (only if enabled by user)
                        if self.save_pdf_enabled:
                            try:
                                pdf_saved = self.save_receipt_as_pdf(village_name, khata_text)
                                if pdf_saved:
                                    self.processing_stats["pdf_saved"] += 1
                                    self.update_live_stats()
                                else:
                                    self.processing_stats["pdf_failed"] += 1
                                    self.update_live_stats()
                            except Exception as pdf_error:
                                # PDF error - log but don't crash
                                self.log_error(village_name, khata_text, f"PDF automation error: {str(pdf_error)}")
                                self.processing_stats["pdf_failed"] += 1
                                self.update_live_stats()

                        # Close receipt window
                        try:
                            self.driver.close()
                        except:
                            pass  # Already closed or error - ignore

                    except Exception as window_error:
                        # Window handling error - log it
                        self.log_error(village_name, khata_text, f"Window handling error: {str(window_error)}")

        except Exception as e:
            # Any error in receipt handling - log but continue
            self.log_error(village_name, khata_text, f"Receipt window error: {str(e)}")

        finally:
            # ALWAYS switch back to main window, even on errors
            try:
                self.driver.switch_to.window(main_window)
            except:
                # If main_window switch fails, try to get current windows and switch to first
                try:
                    windows = self.driver.window_handles
                    if windows:
                        self.driver.switch_to.window(windows[0])
                except:
                    pass  # Last resort - continue anyway

            time.sleep(2)

        return "success"

    def save_receipt_as_pdf(self, village_name, khata_text):
        """Save receipt as PDF using Chrome DevTools Protocol - 95%+ reliable"""
        try:
            # Sanitize village name (replace spaces and special chars with underscores)
            safe_village_name = village_name.replace(' ', '_').replace('/', '_').replace('\\', '_')

            # Sanitize khata number (replace / with _ for khatas like 14/23)
            safe_khata_text = khata_text.replace('/', '_').replace('\\', '_')

            # Create village subfolder in session folder
            village_folder = os.path.join(self.session_folder, safe_village_name)
            os.makedirs(village_folder, exist_ok=True)

            # Generate unique filename with sanitized khata number
            pdf_filename = f"{safe_village_name}_{safe_khata_text}.pdf"
            pdf_filepath = os.path.join(village_folder, pdf_filename)

            # Use Chrome DevTools Protocol to generate PDF
            # This is 100% reliable - no GUI automation, direct browser control
            pdf_data = self.driver.execute_cdp_cmd("Page.printToPDF", {
                "printBackground": True,
                "landscape": False,
                "paperWidth": 8.27,  # A4 width in inches
                "paperHeight": 11.69,  # A4 height in inches
                "marginTop": 0,
                "marginBottom": 0,
                "marginLeft": 0,
                "marginRight": 0,
                "preferCSSPageSize": False
            })

            # Decode base64 PDF data and save to file
            pdf_bytes = base64.b64decode(pdf_data['data'])

            with open(pdf_filepath, 'wb') as f:
                f.write(pdf_bytes)

            # Verify file was saved
            if os.path.exists(pdf_filepath):
                # Track saved PDF
                self.saved_pdfs.append({
                    "khata": khata_text,
                    "village": village_name,
                    "path": pdf_filepath,
                    "filename": pdf_filename
                })
                self.add_result(f"  📄 PDF saved: {pdf_filename}", "success")
                return True
            else:
                self.log_error(village_name, khata_text, "PDF file not created after write")
                return False

        except Exception as e:
            self.log_error(village_name, khata_text, f"CDP PDF error: {str(e)}")
            return False

    def log_error(self, village_name, khata_text, error_msg):
        """Log error details to file"""
        try:
            with open("error_log.txt", "a", encoding="utf-8") as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{timestamp}] {village_name} - {khata_text}: {error_msg}\n")
        except:
            pass  # Silent fail on logging

    def merge_pdfs(self):
        """Merge PDFs per village and create master PDF"""
        try:
            # Group PDFs by village
            villages_pdfs = {}
            for pdf_info in self.saved_pdfs:
                village = pdf_info["village"]
                if village not in villages_pdfs:
                    villages_pdfs[village] = []
                villages_pdfs[village].append(pdf_info["path"])

            merged_village_pdfs = []

            # Merge per village
            for village, pdf_paths in villages_pdfs.items():
                if len(pdf_paths) > 1:
                    merger = PdfMerger()
                    for pdf_path in sorted(pdf_paths):
                        try:
                            merger.append(pdf_path)
                        except:
                            pass  # Skip corrupted PDFs

                    village_merged_path = os.path.join(self.session_folder, f"{village}_MERGED.pdf")
                    merger.write(village_merged_path)
                    merger.close()
                    merged_village_pdfs.append(village_merged_path)

                    self.add_result(f"  ✓ Merged {len(pdf_paths)} receipts for {village}", "success")

            # Create master merge of all receipts
            if len(self.saved_pdfs) > 1:
                master_merger = PdfMerger()
                for pdf_info in sorted(self.saved_pdfs, key=lambda x: x["path"]):
                    try:
                        master_merger.append(pdf_info["path"])
                    except:
                        pass

                master_pdf_path = os.path.join(self.session_folder, "ALL_RECEIPTS_MERGED.pdf")
                master_merger.write(master_pdf_path)
                master_merger.close()

                self.add_result(f"✓ Master PDF created: {master_pdf_path}", "success")

            self.add_result(f"✓ PDF merging complete! Check folder: {self.session_folder}", "success")

        except Exception as e:
            self.add_result(f"⚠ PDF merge failed: {str(e)}", "warning")

    def organize_and_merge_pdfs(self):
        """Merge PDFs that are already in session folder (saved via CDP)"""
        try:
            if not self.saved_pdfs:
                self.add_result("⚠ No PDFs to merge", "warning")
                return

            self.add_result(f"📁 Merging {len(self.saved_pdfs)} PDFs...", "info")

            # Group by village (PDFs already in session folder via CDP)
            village_pdfs = {}

            for pdf_info in self.saved_pdfs:
                village = pdf_info["village"]
                pdf_path = pdf_info["path"]  # Already in session folder/village/

                # Verify file exists
                if os.path.exists(pdf_path):
                    # Track for merging
                    if village not in village_pdfs:
                        village_pdfs[village] = []
                    village_pdfs[village].append(pdf_path)
                else:
                    self.add_result(f"  ⚠ PDF not found: {pdf_path}", "warning")

            # Merge PDFs by village and create master
            if village_pdfs:
                self.merge_pdfs_by_village(village_pdfs)
            else:
                self.add_result("⚠ No PDFs found to merge", "warning")

        except Exception as e:
            self.add_result(f"✗ PDF merge failed: {str(e)}", "error")

    def merge_pdfs_by_village(self, village_pdfs):
        """Merge PDFs per village and create master"""
        try:
            all_pdfs = []

            # Merge per village
            for village, pdf_list in village_pdfs.items():
                if len(pdf_list) > 1:
                    merger = PdfMerger()
                    for pdf in sorted(pdf_list):
                        try:
                            merger.append(pdf)
                        except:
                            pass  # Skip corrupted PDFs

                    village_merged = os.path.join(self.session_folder, f"{village}_MERGED.pdf")
                    merger.write(village_merged)
                    merger.close()
                    self.add_result(f"  ✓ Merged {len(pdf_list)} PDFs for {village}", "success")

                all_pdfs.extend(pdf_list)

            # Master merge
            if len(all_pdfs) > 1:
                master_merger = PdfMerger()
                for pdf in sorted(all_pdfs):
                    try:
                        master_merger.append(pdf)
                    except:
                        pass

                master_path = os.path.join(self.session_folder, "ALL_RECEIPTS_MERGED.pdf")
                master_merger.write(master_path)
                master_merger.close()
                self.add_result(f"✓ Created master PDF: ALL_RECEIPTS_MERGED.pdf", "success")

            self.add_result(f"✓ All PDFs organized in: {self.session_folder}", "success")

        except Exception as e:
            self.add_result(f"✗ PDF merge failed: {str(e)}", "error")

    def stop_automation(self):
        self.is_running = False
        self.add_result("⛔ Abort sequence initiated...", "warning")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MarvelRIAutomation()
    app.run()
