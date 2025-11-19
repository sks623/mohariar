# ⚡ MOHARIAR - RI Automation System V2.0

**Automated Bulk Processing for Odisha Land Revenue RI Online Collection Entry**

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Windows](https://img.shields.io/badge/platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)

🦸 **Designed by SUSHANT** 🦸

---

## 📌 Overview

**MOHARIAR** is a powerful desktop application designed for Revenue Inspectors (RIs) in the Odisha Land Revenue Department. It automates the tedious process of entering land revenue collection data into the government portal, allowing processing of hundreds of khatas (land records) across multiple villages without manual intervention.

### 🌟 What's New in V2.0

- ✅ **PDF Automation**: Auto-save and merge receipt PDFs
- ✅ **Excel Integration**: Upload khata lists per village with delete option
- ✅ **Per-Khata Mobile Numbers**: Different mobile for each khata
- ✅ **Search & Filter**: Quickly find khatas in large lists
- ✅ **Village-Wise Selection**: Select all AND clear all buttons
- ✅ **Skip Button**: Skip current khata during processing
- ✅ **Session History**: View past automation sessions
- ✅ **Sound Notifications**: Audio feedback for system events
- ✅ **Windows Toast**: Desktop notifications on completion
- ✅ **Enhanced Progress Tracking**: ETA, color-coded live stats
- ✅ **Error Retry**: Auto-retry failed entries (no retry for already-paid!)
- ✅ **Export Results**: Save processing results to Excel
- ✅ **Mobile Validation**: Ensures correct 10-digit format
- ✅ **Colored Mission Log**: Status-based text colors
- ✅ **Help Guide**: Built-in PDF user manual

---

## 🚀 Features

### Core Automation
- **Bulk Processing**: Process 100s of khatas in one session
- **Multi-Village Support**: Handle multiple villages simultaneously
- **Auto-Navigation**: Automatically fills forms and submits data
- **Already Paid Detection**: Gracefully skips already-processed khatas (NO RETRY!)
- **Skip Button**: Skip current khata during processing (⏭ SKIP)
- **Session Management**: Organized PDF folders with timestamps
- **Session History**: View all past automation sessions with stats

### Excel Integration
- **Template Download**: Get pre-formatted Excel template
- **Village-Based Upload**: Upload separate Excel files for each village
- **Delete Uploaded Excel**: Remove uploaded Excel data and re-upload
- **Optional Mobile Column**: Specify mobile per khata or use default
- **Data Validation**: Checks format before processing

### PDF Management
- **Auto-Save Receipts**: Saves receipt PDFs automatically
- **Organized Folders**: `rrYYYYMMDD_HHMM/VillageName/` structure
- **Auto-Merge**: Creates merged PDFs per village + master PDF
- **Filename Format**: `Receipt_{Khata}_{Timestamp}.pdf`

### User Experience
- **Marvel-Themed UI**: Professional Iron Man / Avengers design (MOHARIAR branding)
- **Real-Time Progress**: Live progress bar with ETA
- **Color-Coded Mission Log**: Green/Yellow/Red/Blue text based on status
- **Live Statistics Panel**:
  - 🟢 Success (green)
  - 🟡 Already Paid (yellow)
  - 🔴 Errors (red)
  - 🟠 Skipped (orange)
  - 📄 PDFs (blue)
- **Search Function**: Filter khatas as you type
- **Sound Notifications**: Welcome sound on start, completion sound on finish
- **Windows Toast Notifications**: Desktop alerts when processing completes
- **Built-in Help Guide**: PDF manual accessible from UI

### Reliability
- **Auto-Retry**: 3 attempts with exponential backoff (5s, 15s, 30s)
- **Error Logging**: Detailed error log file (`error_log.txt`)
- **Session Recovery**: Organized tracking of processed khatas
- **Abort Functionality**: Stop processing anytime

---

## 📋 Requirements

### System Requirements
- **OS**: Windows 7/10/11
- **Python**: 3.7 or higher
- **RAM**: 4GB minimum (8GB recommended for large batches)
- **Disk Space**: 500MB for application + PDFs

### Software Requirements
- Google Chrome browser (latest version)
- ~~ChromeDriver~~ **AUTO-DOWNLOADED** (webdriver-manager handles this!)
- Microsoft Print to PDF printer (built-in on Windows 10/11)

### Internet Connection
- Stable internet connection for portal access
- Minimum 2 Mbps recommended

---

## 🛠️ Installation

### Step 1: Install Python
1. Download Python 3.7+ from [python.org](https://www.python.org/downloads/)
2. During installation, **check "Add Python to PATH"**
3. Verify: Open Command Prompt and run `python --version`

### Step 2: Download the Project
```bash
# Option A: Clone from GitHub (if available)
git clone https://github.com/yourusername/ri-automation.git
cd ri-automation

# Option B: Download ZIP
# Download and extract the ZIP file, then navigate to the folder
```

### Step 3: Install Dependencies
```bash
# Open Command Prompt in project folder
pip install -r requirements.txt
```

**Note:** ChromeDriver is now **automatically downloaded** on first run! No manual setup needed.

### Step 4: Verify Installation
```bash
python MOHARIAR.py
```

---

## 📖 Usage Guide

### Quick Start

1. **Launch Application**
   ```bash
   python MOHARIAR.py
   ```
   Or double-click `run.bat` (if available)

2. **Enter Default Mobile Number**
   - Enter 10-digit mobile number (required)
   - This will be used for khatas without specific mobile numbers

3. **Initialize System**
   - Click "🔐 INITIALIZE SYSTEM"
   - Browser opens to login page
   - **Manually log in** (captcha requires human intervention)
   - Wait for system to extract villages

4. **Select Villages**
   - Check desired villages OR click "☑ SELECT ALL VILLAGES"
   - Click "📥 EXTRACT KHATAS" to load all khatas

5. **Select Khatas**
   - Check specific khatas OR
   - Use village-wise "☑ Select All" buttons OR
   - Click "☑ SELECT ALL KHATAS" for everything

6. **Engage Protocol**
   - Click "⚡ ENGAGE PROTOCOL"
   - Monitor progress in real-time
   - View results in Mission Log

7. **Export Results** (Optional)
   - After completion, click "📊 EXPORT RESULTS"
   - Excel file with all results will be created

---

### Excel Upload Workflow

#### Step 1: Download Template
1. Click "📥 Download Excel Template"
2. Template file `Khata_Template.xlsx` will be created
3. Open in Excel

#### Step 2: Fill Template
```
| Khata Number | Mobile Number (Optional) |
|--------------|--------------------------|
| 101          | 9876543210               |
| 102          | 8765432109               |
| 103          |                          |  ← Will use default mobile
```

#### Step 3: Upload for Village
1. Check the village checkbox (e.g., "Kerpai")
2. Click "📤 Upload Excel" next to that village
3. Select your filled Excel file
4. System validates and loads khatas

#### Step 4: Process
1. Click "📥 EXTRACT KHATAS" to display loaded khatas
2. Verify khatas and mobile numbers
3. Click "⚡ ENGAGE PROTOCOL" to process

**Benefits:**
- Upload different Excel files for different villages
- Specify unique mobile number for each khata
- Faster than manual selection for large lists

---

### PDF Output

After processing, PDFs are organized in a session folder:

```
rr20251114_1430/               ← Session folder
├── Kerpai/
│   ├── Receipt_101_143055.pdf
│   ├── Receipt_102_143127.pdf
│   └── ...
├── Dharamgarh/
│   ├── Receipt_201_143200.pdf
│   └── ...
├── Kerpai_MERGED.pdf          ← Village merged PDF
├── Dharamgarh_MERGED.pdf      ← Village merged PDF
└── ALL_RECEIPTS_MERGED.pdf    ← Master merged PDF
```

---

## 🔧 Configuration

### Customizing Settings

Edit `MOHARIAR.py` to customize:

**Mobile Number Validation:**
```python
def validate_mobile_number(self, mobile):
    # Change validation rules here
    return len(mobile) == 10 and mobile.isdigit()
```

**PDF Automation Delays:**
```python
def save_receipt_as_pdf(self, village_name, khata_text):
    time.sleep(2)  # Adjust delays if PDF automation fails
```

**Retry Settings:**
```python
max_retries = 3
retry_delays = [5, 15, 30]  # Customize retry delays
```

---

## ⚠️ Troubleshooting

### Common Issues

**Issue: "ChromeDriver download failed"**
- **Solution**: Check internet connection and retry
- ChromeDriver auto-downloads on first run
- Cached after first download (no re-download needed)

**Issue: PDF automation not working**
- **Solution**:
  - Ensure "Microsoft Print to PDF" is installed
  - Check Windows 10/11 Settings → Printers
  - PDFs may fail silently; check `error_log.txt`

**Issue: "Module not found" errors**
- **Solution**: Reinstall dependencies
  ```bash
  pip install --upgrade -r requirements.txt
  ```

**Issue: Login timeout**
- **Solution**: Log in faster (within 5 minutes)
- Check internet connection stability

**Issue: Khatas not appearing**
- **Solution**:
  - Wait for full page load (3 seconds)
  - Refresh browser manually if needed
  - Check if village has khatas

**Issue: Already Paid not detected**
- **Solution**: Portal popup text may have changed
- Check `error_log.txt` for details
- Manually verify those khatas

---

## 🎨 UI Guide

### Color Coding

- **🟢 Green**: Success messages
- **🟡 Yellow**: Warnings (already paid, retries)
- **🔴 Red**: Errors
- **🔵 Blue**: Information

### Button States

- **Disabled (Gray)**: Not available yet
- **Active (Colored)**: Ready to use
- **Processing (Yellow)**: Operation in progress

---

## 📊 Performance

### Typical Processing Speed
- **15-20 seconds per khata** (average)
- **~200-240 khatas per hour**
- **500 khatas ≈ 2-3 hours**

### Factors Affecting Speed
- Server response time (2-5s)
- Internet speed
- PDF save time (3-5s per receipt)
- Already paid khatas (faster - skip immediately)

### Recommendations
- Process during off-peak hours (early morning)
- Stable internet connection
- Don't minimize browser during processing

---

## 🔐 Security & Privacy

### Data Handling
- ✅ **No credentials stored locally**
- ✅ **No data sent to external servers**
- ✅ **Session data cleared on exit**
- ✅ **Works on air-gapped networks** (after login)

### Compliance
- ✅ Uses official government portal only
- ✅ No bypassing of security measures
- ✅ Manual authentication (captcha)
- ✅ Audit trail via mission log

---

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Reporting Issues
- Open an issue on GitHub
- Include error log (`error_log.txt`)
- Describe steps to reproduce

### Feature Requests
- Describe the feature clearly
- Explain the use case
- Provide examples if possible

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🏆 Credits

**Developed by:** SUSHANT (Revenue Inspector)
**Version:** 2.0.0
**Release Date:** November 2025
**Platform:** Odisha Land Revenue Department

**Special Thanks:**
- Claude AI (Anthropic) for development assistance
- Odisha Land Revenue Department for the online portal
- All RIs providing feedback and testing

---

## 📞 Support

### For Technical Issues
- Check [Troubleshooting](#-troubleshooting) section
- Review `error_log.txt` for details
- Open GitHub issue with error details

### For Portal Issues
- Contact Odisha Land Revenue IT Support
- Check portal status at [odishalandrevenue.nic.in](https://odishalandrevenue.nic.in)

---

## 🔄 Version History

### V2.0.0 (November 2025)
- ✨ PDF automation with auto-save and merge
- ✨ Excel integration for bulk upload
- ✨ Per-khata mobile number support
- ✨ Village-wise "Select All" buttons
- ✨ Search and filter functionality
- ✨ Sound notifications
- ✨ Enhanced progress tracking with ETA
- ✨ Error retry mechanism (3 attempts)
- ✨ Export results to Excel
- ✨ Mobile number validation
- ✨ Improved error logging

### V1.0.0 (October 2025)
- 🎉 Initial release
- Basic automation of RI collection entry
- Multi-village and multi-khata support
- Marvel-themed UI
- Already Paid detection

---

## 🚧 Known Limitations

1. **PDF Automation**: May fail on some Windows versions (saves silently fail)
2. **Session Timeout**: Portal times out after ~2 hours
3. **Concurrent Users**: Only one user can process at a time per login
4. **Captcha**: Manual login required (cannot be automated)
5. **Network Dependency**: Requires stable internet throughout

---

## 🔮 Future Enhancements (V3.0)

- Resume capability for interrupted sessions
- Statistics dashboard (weekly/monthly reports)
- Multi-district support
- Scheduled batch processing
- Direct API integration (if available)
- Mobile app version
- Team collaboration features

---

## 📚 Additional Resources

- [QUICKSTART.md](QUICKSTART.md) - Simple getting started guide
- [CLAUDE.md](CLAUDE.md) - Technical documentation for developers
- [CHANGELOG.md](CHANGELOG.md) - Detailed version history

---

**Made with ⚡ by Avengers Tech**

*"With great automation comes great productivity!"*
#   m o h a r i a r  
 