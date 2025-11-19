# ⚡ RI AUTOMATION - QUICK START GUIDE ⚡

## 🚀 FIRST TIME SETUP

### Prerequisites
- Windows 7/10/11
- Python 3.7 or higher ([Download](https://www.python.org/downloads/))
- Google Chrome browser
- Internet connection

### Installation

1. **Extract all files** to a folder
2. **Open Command Prompt** in that folder (Shift + Right Click → "Open PowerShell window here")
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶ HOW TO RUN

```bash
python marvel_ri_automation.py
```

---

## 📋 STEP-BY-STEP USAGE

### STEP 1: INITIALIZE SYSTEM
1. Enter your **mobile number** (or keep default: 8984750096)
2. Click **"🔐 INITIALIZE SYSTEM"**
3. Browser window opens automatically
4. **LOGIN MANUALLY** with your credentials
5. Wait for system to extract villages

### STEP 2: SELECT VILLAGES
- **Option A:** Check individual villages you want to process
- **Option B:** Click **"☑ SELECT ALL VILLAGES"** to select all

### STEP 3: EXTRACT KHATAS
1. Click **"📥 EXTRACT KHATAS"** button
2. System scans and displays all khatas from selected villages
3. Wait for "KHATAS LOADED" message

### STEP 4: SELECT KHATAS
- **Option A:** Manually check khatas you want to process
- **Option B:** Click **"☑ SELECT ALL KHATAS"** to select all
- **Option C:** Mix - select some, skip others

### STEP 5: START AUTOMATION
1. Click **"⚡ ENGAGE PROTOCOL"**
2. Monitor progress in real-time
3. Check results in Mission Log

### STEP 6: REVIEW RESULTS
- **✓ Success** - Entry created successfully
- **⚠ Already Paid** - Skipped (already processed)
- **✗ Error** - Failed (check manually)

---

## 🎯 COMMON SCENARIOS

### Process ALL khatas in ONE village
1. Select that village only
2. Extract khatas
3. Click "Select All Khatas"
4. Engage protocol

### Process ALL khatas in MULTIPLE villages
1. Click "Select All Villages"
2. Extract khatas
3. Click "Select All Khatas"
4. Engage protocol

### Process SPECIFIC khatas only
1. Select desired villages
2. Extract khatas
3. Manually check only the khatas you want
4. Engage protocol

---

## ⚠ TROUBLESHOOTING

### "Module not found" error
```bash
pip install -r requirements.txt
```

### Chrome doesn't open
- Make sure Chrome is installed
- Update Chrome to latest version

### Login issues
- Check internet connection
- Verify credentials are correct
- Dismiss any error popups and retry

### "Already Paid" for all khatas
- Those khatas were processed earlier
- This is normal - system skips them

### Automation stops
- Check internet connection
- Check if browser window is still open
- Click "Engage Protocol" again to retry

---

## 📞 QUICK REFERENCE

| Button | Action |
|--------|--------|
| 🔐 INITIALIZE SYSTEM | Login and extract villages |
| ☑ SELECT ALL VILLAGES | Select all villages at once |
| 📥 EXTRACT KHATAS | Scan and display all khatas |
| ☑ SELECT ALL KHATAS | Select all khatas at once |
| ⚡ ENGAGE PROTOCOL | Start automation |
| ⛔ ABORT MISSION | Stop automation |

---

## 💾 PORTABLE SETUP

### To use on another computer:
1. Copy these 2 files:
   - `marvel_ri_automation.py`
   - `requirements.txt`
2. Install Python on new computer
3. Run: `pip install -r requirements.txt`
4. Run: `python marvel_ri_automation.py`

---

## 📊 EXPECTED PERFORMANCE

- **Processing Speed:** ~15-20 seconds per khata
- **100 khatas:** ~30-40 minutes
- **500 khatas:** ~2.5-3 hours

**Note:** Speed depends on internet connection and server response time.

---

## 🔒 SECURITY

- ✅ No credentials are stored
- ✅ No data is sent to external servers
- ✅ Everything runs locally on your computer
- ✅ Safe to use on government networks

---

## 📝 TIPS FOR BEST RESULTS

1. **Stable Internet:** Use wired connection if possible
2. **Don't Minimize:** Keep browser visible during automation
3. **Regular Breaks:** Process in batches of 100-200 khatas
4. **Verify First:** Test with 2-3 khatas first
5. **Check Results:** Review mission log for errors

---

## 🆘 NEED HELP?

Check the detailed documentation in `CLAUDE.md` for advanced features and troubleshooting.

---

**Version:** 1.0 (Marvel Edition)
**Created by:** SUSHANT
**Last Updated:** October 2025
