# 🚀 MOHARIAR - Installation Guide (Executable Version)

## 📋 For Complete Beginners - Step by Step

This guide will help you install and run **MOHARIAR.exe** on any Windows computer with **ZERO programming knowledge required**.

---

## ✅ What You Need

### Required (Must Have):
1. ✅ **Windows Computer** (Windows 7, 10, or 11)
2. ✅ **Google Chrome Browser** (Download from: https://www.google.com/chrome/)
3. ✅ **Internet Connection** (for first-time setup only)
4. ✅ **MOHARIAR.exe** file (the application)

### NOT Required (Don't Need):
- ❌ Python installation
- ❌ Manual ChromeDriver download
- ❌ Any coding knowledge
- ❌ Command prompt/terminal experience

---

## 📥 STEP 1: Download Required Files

### A. Download Google Chrome (if not already installed)

1. Open any web browser (Edge, Firefox, etc.)
2. Go to: **https://www.google.com/chrome/**
3. Click **"Download Chrome"**
4. Run the downloaded file and follow installation steps
5. ✅ Verify: Open Chrome and check it works

### B. Get MOHARIAR.exe

**Option 1: From GitHub Release**
1. Go to the GitHub releases page
2. Download **MOHARIAR.exe** (latest version)
3. Save to a folder you'll remember (e.g., `Desktop` or `Documents\MOHARIAR`)

**Option 2: From Direct Share**
1. Copy **MOHARIAR.exe** to your computer
2. Place in a dedicated folder (e.g., `C:\MOHARIAR\`)

---

## 🛡️ STEP 2: Handle Windows Security Warning

When you run MOHARIAR.exe for the first time, Windows might show a warning:

### "Windows protected your PC"

**This is NORMAL!** Here's how to proceed:

1. Click **"More info"**
2. Click **"Run anyway"**

**Why this happens:**
- Windows shows this for any .exe not digitally signed by Microsoft
- MOHARIAR is safe - it's just automation software for government portal
- Antivirus might also flag it - add it to exclusions if needed

---

## ▶️ STEP 3: First Run (Automatic Setup)

### Launch MOHARIAR

1. **Double-click** `MOHARIAR.exe`
2. Wait 10-20 seconds for the application to load
3. You'll see the MOHARIAR interface with Iron Man theme

### First-Time Automatic Setup (Happens Once)

On **FIRST RUN ONLY**, you'll see:

```
🔧 Setting up ChromeDriver (auto-download)...
```

**What's happening:**
- MOHARIAR is automatically downloading ChromeDriver (~10MB)
- This matches your Chrome browser version
- Takes 5-10 seconds with good internet
- **Only happens ONCE** - future runs will be instant!

**If you see errors:**
- ✅ Check your internet connection
- ✅ Make sure Chrome is installed
- ✅ Allow MOHARIAR through firewall if asked

---

## 🎮 STEP 4: Using MOHARIAR

### A. Enter Mobile Number

1. In the **"DEFAULT Mobile Number"** field, enter your 10-digit mobile number
   - Example: `9876543210`
   - This will be used for all khatas unless specified otherwise

2. Click **"🔐 INITIALIZE SYSTEM"**

### B. Login to Portal

1. Chrome browser will open automatically
2. **Portal URL:** `https://odishalandrevenue.nic.in`
3. **You must login MANUALLY** (captcha cannot be automated)
   - Select District
   - Enter User ID
   - Enter Password
   - Type Captcha
   - Click Login

4. Wait for villages to load in MOHARIAR

### C. Process Khatas

**Method 1: Select Villages Manually**
1. Check villages you want to process
2. Click **"Extract Khatas"**
3. Check khatas you want to process
4. Click **"⚡ ENGAGE PROTOCOL"**

**Method 2: Upload Excel File**
1. Click **"Download Excel Template"**
2. Fill in: Khata Number | Mobile Number (optional)
3. Check village name
4. Click **"📁 Upload Excel"** next to that village
5. Select your filled Excel file
6. Click **"Extract Khatas"**
7. Click **"⚡ ENGAGE PROTOCOL"**

### D. Monitor Progress

- ✅ Watch **Mission Log** for real-time status
- ✅ Check **Live Stats** for success/error counts
- ✅ See **Progress Bar** with ETA
- ✅ PDFs auto-saved to `rrYYYYMMDD_HHMM/` folder

### E. When Complete

- 🔊 Completion sound plays
- 🔔 Desktop notification shows
- 📊 Click **"Export Results"** to save Excel report
- 📜 Click **"HISTORY"** to view past sessions

---

## 📂 STEP 5: Understanding Output Files

After running MOHARIAR, you'll find these files/folders:

### PDF Output (Receipts)
```
rr20251117_1430/           ← Session folder
├── Kerpai/                ← Village folder
│   ├── Receipt_101_143055.pdf
│   ├── Receipt_102_143110.pdf
│   └── ...
├── Kerpai_MERGED.pdf      ← All Kerpai receipts in one file
└── ALL_RECEIPTS_MERGED.pdf ← All receipts from all villages
```

### Excel Reports
```
RI_Results_20251117_1430.xlsx  ← Detailed results with status
```

### History & Logs
```
session_history.json       ← Last 50 sessions data
error_log.txt             ← Detailed error messages (if any)
```

---

## 🆘 TROUBLESHOOTING

### Problem: "ChromeDriver auto-download failed"

**Solution:**
1. Check internet connection
2. Make sure Chrome is installed and updated
3. Restart MOHARIAR.exe
4. If still failing, check firewall settings

---

### Problem: "Chrome browser not opening"

**Solution:**
1. Install Google Chrome from https://www.google.com/chrome/
2. Open Chrome once manually to complete setup
3. Close Chrome
4. Restart MOHARIAR.exe

---

### Problem: "Already paid" khatas taking too long

**Good News:** This is FIXED in latest version!
- Already-paid khatas are detected instantly
- No more retries for already-paid entries
- Check mission log for orange "⚠ ALREADY PAID" messages

---

### Problem: Application won't start / Crashes immediately

**Solutions:**
1. **Windows Defender blocking:**
   - Right-click MOHARIAR.exe → Properties
   - Check "Unblock" at bottom → Apply

2. **Antivirus blocking:**
   - Add MOHARIAR.exe to exclusions
   - Or temporarily disable antivirus

3. **Missing Visual C++ Runtime:**
   - Download: https://aka.ms/vs/17/release/vc_redist.x64.exe
   - Install and restart computer

---

### Problem: Portal login fails / Page not loading

**Solutions:**
1. Check internet connection
2. Verify portal is accessible: https://odishalandrevenue.nic.in
3. Try logging in manually first
4. Clear Chrome cache and try again

---

### Problem: PDFs not saving

**Solutions:**
1. Check folder permissions (run as Administrator if needed)
2. Make sure enough disk space available (100MB+)
3. Close any PDFs that are already open
4. Check `error_log.txt` for specific error

---

### Problem: Excel upload not working

**Solutions:**
1. Make sure Excel file has "Khata Number" column
2. Use template: Click "Download Excel Template"
3. Save as .xlsx format (not .xls or .csv)
4. Check no empty rows in Excel

---

## 🎓 Tips for Smooth Operation

### ✅ DO:
- Keep Chrome browser updated
- Maintain stable internet connection during processing
- Use "Export Results" after each session
- Check Session History to avoid re-processing

### ❌ DON'T:
- Don't close Chrome browser manually during processing
- Don't click inside portal page while automation is running
- Don't process same khatas twice (check History first)
- Don't run multiple MOHARIAR instances simultaneously

---

## 🔒 Security & Privacy

### What MOHARIAR Does:
- ✅ Automates form filling on government portal
- ✅ Saves receipts as PDFs locally
- ✅ Stores session history in local JSON file

### What MOHARIAR Does NOT Do:
- ❌ Send any data to external servers
- ❌ Store your password anywhere
- ❌ Access any files outside its folder
- ❌ Connect to internet except for portal and ChromeDriver download

### Your Data:
- All data stays on YOUR computer
- No cloud storage or uploads
- PDFs and Excel files saved locally only
- Session history stored in `session_history.json` (local file)

---

## 📞 Need Help?

### Check Documentation:
1. **README.md** - Full feature list
2. **CLAUDE.md** - Technical documentation
3. **GITHUB_SETUP.md** - How to update/contribute

### Help Button:
- Click **"📖 HELP"** in MOHARIAR
- Opens user manual PDF with screenshots

### Session History:
- Click **"📜 HISTORY"** to see past runs
- Helps avoid re-processing same data

---

## 🎯 Quick Start Checklist

Before first run, verify:

- [ ] Google Chrome installed and working
- [ ] MOHARIAR.exe downloaded
- [ ] Windows security warning handled
- [ ] Internet connection active
- [ ] 10-digit mobile number ready
- [ ] Portal login credentials ready

---

## 🔄 Updating MOHARIAR

When a new version is released:

1. Download new **MOHARIAR.exe**
2. Replace old file with new file
3. Your data is safe (PDFs, session history, etc.)
4. First run might re-download ChromeDriver (normal)

**Note:** Session history and PDFs from old version remain intact!

---

## 📊 Performance Expectations

### Processing Speed:
- **Average:** 15-20 seconds per khata
- **Faster if:** Portal responds quickly, fewer retries
- **Slower if:** Network issues, many already-paid khatas

### Batch Sizes:
- ✅ **Tested up to:** 500 khatas per session
- ✅ **Recommended:** 50-100 khatas per batch
- ✅ **Session timeout:** ~2 hours (portal limitation)

### Success Rate:
- **Typical:** 95%+ success rate
- **Already Paid:** 3-5% (normal, not an error)
- **Errors:** <2% (network issues, retry automatically)

---

## 🎉 You're Ready!

**Congratulations!** You now know how to:
- ✅ Install and run MOHARIAR.exe
- ✅ Handle Windows security warnings
- ✅ Process khatas automatically
- ✅ Troubleshoot common issues
- ✅ Export results and view history

**No ChromeDriver download needed - it's automatic! 🎊**

---

**MOHARIAR - Designed by SUSHANT**
*Automating land revenue collection with Iron Man efficiency*

---

## 📝 Changelog

**Latest Version Features:**
- ✅ Automatic ChromeDriver download (no manual setup!)
- ✅ Fixed already-paid retry bug
- ✅ Skip button during processing
- ✅ Session history tracking
- ✅ Colored mission log
- ✅ Windows desktop notifications
- ✅ Delete uploaded Excel feature
- ✅ Help guide integration

**For full changelog, see:** `CHANGELOG.md`
