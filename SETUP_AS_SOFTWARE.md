# 📌 Using MOHARIAR Like Regular Software

## ✅ YES! You Can Pin to Taskbar & Use Like Any Software

MOHARIAR.exe is a **standalone executable** that works exactly like installed software (Chrome, Word, etc.)

---

## 🎯 Setting Up MOHARIAR as Regular Software

### **Step 1: Choose a Permanent Location**

**IMPORTANT:** Place MOHARIAR.exe in a folder where it will stay permanently.

**Good Locations:**
```
✅ C:\Program Files\MOHARIAR\MOHARIAR.exe
✅ C:\Users\YourName\Documents\MOHARIAR\MOHARIAR.exe
✅ D:\Software\MOHARIAR\MOHARIAR.exe
```

**Bad Locations:**
```
❌ Desktop (gets messy)
❌ Downloads folder (might get deleted)
❌ Temporary folders
```

**Recommended Setup:**
1. Create folder: `C:\MOHARIAR\`
2. Copy `MOHARIAR.exe` to this folder
3. All output folders (PDFs, Excel) will be created here automatically

---

### **Step 2: Pin to Taskbar**

#### **Method 1: While Running (Easiest)**
1. Double-click `MOHARIAR.exe` to run it
2. Look at your taskbar - you'll see the MOHARIAR icon
3. **Right-click** the taskbar icon
4. Select **"Pin to taskbar"**
5. ✅ Done! Icon stays on taskbar permanently

#### **Method 2: From File Explorer**
1. Open File Explorer
2. Navigate to your MOHARIAR folder (e.g., `C:\MOHARIAR\`)
3. **Right-click** `MOHARIAR.exe`
4. Select **"Pin to taskbar"**
5. ✅ Done!

**Result:** You'll see the MOHARIAR icon on your taskbar always. Click it anytime to launch!

---

### **Step 3: Create Desktop Shortcut (Optional)**

1. **Right-click** `MOHARIAR.exe` in File Explorer
2. Select **"Send to"** → **"Desktop (create shortcut)"**
3. ✅ Shortcut appears on Desktop
4. (Optional) Rename shortcut to just "MOHARIAR"

**OR:**

1. **Right-click** `MOHARIAR.exe`
2. Select **"Create shortcut"**
3. **Drag** the shortcut to Desktop

---

### **Step 4: Add to Start Menu (Optional)**

#### **For Quick Access:**
1. **Right-click** `MOHARIAR.exe`
2. Select **"Pin to Start"**
3. ✅ Appears in Start Menu tiles

**OR Create Start Menu Entry:**
1. Press `Windows + R`
2. Type: `shell:programs`
3. Press Enter (opens Start Menu folder)
4. Create shortcut to MOHARIAR.exe here
5. ✅ Appears in Start Menu alphabetically

---

## 🚀 Daily Usage (After Setup)

Once pinned to taskbar:

1. **Click** MOHARIAR icon on taskbar
2. Application opens instantly
3. Enter mobile number and use normally
4. All PDFs/Excel files save to same folder as .exe

**No different from Chrome, Word, or any installed software!**

---

## 📂 Understanding File Structure

### **When You Run MOHARIAR:**

Your MOHARIAR folder will look like this:

```
C:\MOHARIAR\
├── MOHARIAR.exe                    ← The application
│
├── [Generated on first run]
├── session_history.json            ← Your session history
├── error_log.txt                   ← Error logs (if any)
│
├── [Generated when you use it]
├── rr20251117_1430\                ← PDF receipts (timestamped folders)
│   ├── Kerpai\
│   │   ├── Receipt_101.pdf
│   │   └── Receipt_102.pdf
│   └── ALL_RECEIPTS_MERGED.pdf
│
├── RI_Results_20251117_1430.xlsx   ← Excel exports
├── Khata_Template.xlsx             ← Template (if downloaded)
│
└── [ChromeDriver cache - hidden]
    └── (auto-managed by webdriver-manager)
```

**Important:**
- ✅ Don't move MOHARIAR.exe after pinning to taskbar
- ✅ All output files stay in same folder
- ✅ Easy to backup: just copy the entire MOHARIAR folder

---

## 🔄 Moving MOHARIAR to Another Location

**If you need to move MOHARIAR.exe after pinning:**

1. **Unpin** from taskbar (right-click icon → "Unpin from taskbar")
2. **Move** MOHARIAR.exe to new location
3. **Delete** old shortcuts (if any)
4. **Re-pin** from new location
5. **Create new shortcuts** pointing to new location

**Tip:** Choose permanent location from the start to avoid this!

---

## 🎨 Customizing the Icon (Advanced - Optional)

MOHARIAR.exe already has a default icon, but if you want a custom one:

### **Method 1: Shortcut Icon Change**
1. Create a shortcut to MOHARIAR.exe
2. Right-click shortcut → **Properties**
3. Click **"Change Icon..."**
4. Choose a custom icon (.ico file)
5. Click **OK**

**Note:** This only changes the shortcut icon, not the .exe itself.

### **Method 2: Rebuild .exe with Custom Icon**
If you have the source code:
1. Create/download a `.ico` file
2. Edit `MOHARIAR.spec` line:
   ```python
   exe = EXE(
       ...
       icon='path/to/custom_icon.ico',  # Add this line
       ...
   )
   ```
3. Rebuild: `pyinstaller MOHARIAR.spec`

---

## ⚡ Quick Launch Options

### **Option 1: Keyboard Shortcut**
1. Create Desktop shortcut
2. Right-click shortcut → **Properties**
3. Click in **"Shortcut key"** field
4. Press your desired key combo (e.g., `Ctrl + Alt + M`)
5. Click **OK**
6. ✅ Now press `Ctrl + Alt + M` to launch MOHARIAR from anywhere!

### **Option 2: Run Command**
1. Press `Windows + R`
2. Type: `C:\MOHARIAR\MOHARIAR.exe`
3. Press **Enter**

**To make it shorter:**
1. Add `C:\MOHARIAR\` to system PATH (advanced)
2. Then just type: `MOHARIAR` in Run dialog

---

## 🔒 Administrative Rights (If Needed)

Some operations (like PDF saving) might need admin rights:

### **Run as Administrator (One Time):**
1. Right-click MOHARIAR icon (taskbar or desktop)
2. Select **"Run as administrator"**
3. Click **Yes** on UAC prompt

### **Always Run as Administrator:**
1. Right-click `MOHARIAR.exe` in File Explorer
2. Select **Properties**
3. Go to **"Compatibility"** tab
4. Check **"Run this program as an administrator"**
5. Click **OK**
6. ✅ Now always runs with admin rights (even from taskbar)

**Note:** Usually not needed unless you're saving to restricted folders.

---

## 🗑️ Uninstalling MOHARIAR

MOHARIAR doesn't have a traditional installer, so uninstalling is simple:

### **To Remove:**
1. **Unpin** from taskbar (right-click icon → "Unpin")
2. **Delete** desktop shortcuts (if any)
3. **Delete** Start Menu entries (if any)
4. **Delete** the MOHARIAR folder (e.g., `C:\MOHARIAR\`)
5. ✅ Done! Completely removed

**No registry entries!**
**No hidden files!**
**Clean removal!**

---

## 📊 Comparison: .exe vs Installed Software

| Feature | Traditional Software | MOHARIAR.exe |
|---------|---------------------|--------------|
| **Installation** | Runs installer, registry changes | Copy file, done! |
| **Pin to Taskbar** | ✅ Yes | ✅ Yes |
| **Desktop Shortcut** | ✅ Yes | ✅ Yes |
| **Start Menu** | ✅ Yes | ✅ Yes (manual) |
| **Uninstall** | Control Panel | Delete folder |
| **Updates** | Auto-update | Replace .exe file |
| **Portable** | ❌ No | ✅ Yes (copy to USB) |
| **Registry Entries** | ✅ Yes | ❌ No |
| **Size** | Varies | 165MB |

---

## 💾 Portable Usage (Bonus!)

MOHARIAR.exe is **portable** - you can use it from USB drive:

### **Steps:**
1. Copy entire `MOHARIAR` folder to USB drive
2. On any Windows computer:
   - Plug in USB
   - Navigate to `USB:\MOHARIAR\`
   - Double-click `MOHARIAR.exe`
3. ✅ Works without installation!

**Requirements on target PC:**
- ✅ Windows OS
- ✅ Google Chrome installed
- ✅ Internet (first run only, for ChromeDriver)

**Portable Use Cases:**
- Use on multiple computers
- Work computer + home computer
- Share with colleague (they copy to their PC)
- Backup on external drive

---

## 🎯 Best Practices

### **DO:**
✅ Place in permanent location before pinning
✅ Create shortcuts for easy access
✅ Backup the folder regularly (includes session history)
✅ Keep in a folder named "MOHARIAR" (not "New Folder")

### **DON'T:**
❌ Move .exe after pinning (breaks shortcuts)
❌ Keep in Downloads folder (might get auto-deleted)
❌ Run from temporary folders
❌ Delete while application is running

---

## 🆘 Troubleshooting Taskbar Pin

**Issue: "Pin to taskbar" option grayed out**
- **Solution**: Run the .exe first, then pin while running

**Issue: Taskbar icon launches but app doesn't open**
- **Solution**: .exe was moved; unpin and re-pin from new location

**Issue: Multiple MOHARIAR icons on taskbar**
- **Solution**: One is the pinned icon, one is running instance; normal behavior

**Issue: Icon shows generic .exe icon**
- **Solution**: This is normal for custom .exe files; works fine

---

## ✅ Summary

**YES!** MOHARIAR.exe works exactly like regular software:

✅ **Pin to Taskbar** - One click to launch
✅ **Desktop Shortcut** - Double-click to run
✅ **Start Menu** - Find alphabetically
✅ **Keyboard Shortcut** - Custom hotkey
✅ **Portable** - Works from USB drive
✅ **No Installation** - Just copy and use
✅ **Clean Uninstall** - Delete folder, done

**It's just like Chrome, Word, or any other software - only simpler!** 🎉

---

**MOHARIAR - Designed by SUSHANT**
*Making automation as easy as clicking an icon*
