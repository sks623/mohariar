# Contributing to RI Automation System

First off, thank you for considering contributing to the RI Automation System! It's people like you that make this tool better for Revenue Inspectors across Odisha.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)

---

## 🤝 Code of Conduct

This project and everyone participating in it is governed by respect and professionalism. By participating, you are expected to:

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

---

## 💡 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When you create a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the behavior
- **Expected vs actual behavior**
- **Screenshots** if applicable
- **Environment details**:
  - OS version (Windows 7/10/11)
  - Python version
  - Chrome version
  - Error log (`error_log.txt` contents)

**Bug Report Template:**

```markdown
**Environment:**
- OS: Windows 10
- Python: 3.9.5
- Chrome: 120.0.6099.109

**Description:**
PDF automation fails on Windows 11

**Steps to Reproduce:**
1. Process khata with "Engage Protocol"
2. Receipt window opens
3. PDF save fails silently

**Expected Behavior:**
PDF should be saved to rr folder

**Actual Behavior:**
No PDF created, error_log shows: [error details]

**Screenshots:**
[Attach screenshots]
```

### Suggesting Features

Feature requests are welcome! Please provide:

- **Clear use case**: Why is this feature needed?
- **Proposed solution**: How would it work?
- **Alternatives considered**: What other approaches exist?
- **Impact**: Who benefits from this feature?

**Feature Request Template:**

```markdown
**Feature:** Resume capability for interrupted sessions

**Use Case:**
When internet disconnects mid-processing, I lose all progress and must restart from scratch. This is frustrating with 500+ khatas.

**Proposed Solution:**
- Save checkpoint after every 10 khatas
- On restart, ask "Resume previous session?"
- Skip already-processed khatas

**Alternatives:**
- Manual session tracking (tedious)
- Process smaller batches (inefficient)

**Impact:**
All RIs processing large batches would benefit.
```

### Code Contributions

We welcome code contributions! You can contribute:

1. **Bug Fixes**: Fix reported bugs
2. **New Features**: Implement from roadmap or feature requests
3. **Performance Improvements**: Optimize slow operations
4. **Documentation**: Improve README, add examples
5. **Tests**: Add test cases (future improvement)

---

## 🛠️ Development Setup

### Prerequisites

```bash
# Install Python 3.7+
python --version  # Verify

# Install Git
git --version  # Verify
```

### Clone and Setup

```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/YOUR_USERNAME/ri-automation.git
cd ri-automation

# Add upstream remote
git remote add upstream https://github.com/ORIGINAL_OWNER/ri-automation.git

# Install dependencies
pip install -r requirements.txt

# Test the application
python MOHARIAR.py
```

### Branch Strategy

```bash
# Create a feature branch from main
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b fix/bug-description

# Keep your branch updated
git fetch upstream
git rebase upstream/main
```

---

## 📝 Coding Standards

### Python Style

Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines:

```python
# Good
def process_khata(village_value, khata_number, mobile):
    """Process a single khata entry.

    Args:
        village_value (str): Village dropdown value
        khata_number (str): Khata number to process
        mobile (str): 10-digit mobile number

    Returns:
        str: Status - 'success', 'already_paid', or 'error'
    """
    # Implementation
    pass

# Bad
def prcKhata(v,k,m):  # Unclear names, no docstring
    pass
```

### Code Organization

- **One class per file** (if adding new modules)
- **Max 100 lines per function** (split longer functions)
- **Descriptive variable names** (`khata_number` not `kn`)
- **Constants in UPPER_CASE** (`MAX_RETRIES = 3`)
- **Type hints where applicable** (`def foo(x: int) -> str`)

### Error Handling

```python
# Good - Specific exceptions
try:
    element = driver.find_element(By.XPATH, xpath)
except NoSuchElementException as e:
    log_error(f"Element not found: {xpath}")
    return "error"
except TimeoutException as e:
    log_error(f"Timeout waiting for element: {xpath}")
    return "error"

# Bad - Generic exception
try:
    element = driver.find_element(By.XPATH, xpath)
except Exception as e:  # Too broad
    return "error"
```

### Comments

- **Docstrings** for all functions/classes
- **Inline comments** for complex logic
- **TODO comments** for known issues
- **Avoid obvious comments**

```python
# Good
# Retry mechanism: 3 attempts with exponential backoff (5s, 15s, 30s)
for attempt in range(MAX_RETRIES):
    # Implementation

# Bad
x = x + 1  # Increment x by 1 (too obvious)
```

---

## 🚀 Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Code formatting (no logic change)
- `refactor`: Code restructuring (no feature/fix)
- `perf`: Performance improvement
- `test`: Adding tests
- `chore`: Build process, dependencies

### Examples

```bash
# Good
feat(pdf): add automatic PDF merging per village

- Merges all receipts for each village
- Creates master merged PDF with all receipts
- Uses PyPDF2 for reliable merging

Closes #42

# Good
fix(excel): handle missing mobile number column

Previously crashed when Mobile Number column was absent.
Now defaults to empty string if column missing.

Fixes #38

# Good
docs(readme): add troubleshooting section for PDF issues

# Bad
update stuff  # Too vague
Fixed bug  # Which bug? No details
```

---

## 🔄 Pull Request Process

### Before Submitting

1. **Update from upstream**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Test your changes**
   - Run the application
   - Test affected features
   - Check for errors in `error_log.txt`

3. **Update documentation**
   - README if user-facing changes
   - CLAUDE.md if technical changes
   - Docstrings for new functions

4. **Check code quality**
   ```bash
   # Optional: Run formatter
   pip install black
   black MOHARIAR.py
   ```

### Submitting PR

1. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request on GitHub**
   - Clear title: `feat(pdf): add automatic PDF merging`
   - Detailed description:
     - What changed?
     - Why was it needed?
     - How was it tested?
     - Screenshots if UI changes
   - Link related issues: `Closes #42`

3. **PR Template**

```markdown
## Description
Adds automatic PDF merging feature per village and creates master merged PDF.

## Motivation
Users requested a single PDF per village instead of individual receipts.

## Changes
- Added `merge_pdfs()` method
- Village PDFs: `{village}_MERGED.pdf`
- Master PDF: `ALL_RECEIPTS_MERGED.pdf`
- Updated progress reporting

## Testing
- Tested with 50 khatas across 3 villages
- Verified merged PDFs open correctly
- Checked error handling for corrupted PDFs

## Screenshots
[Attach UI changes if any]

## Checklist
- [x] Code follows style guidelines
- [x] Self-reviewed the code
- [x] Updated documentation
- [x] Tested on Windows 10
- [ ] Tested on Windows 11 (need help)

Closes #42
```

### Review Process

- Maintainers will review within 3-5 days
- Address feedback with new commits
- Once approved, PR will be merged
- Celebrate! 🎉

---

## 🧪 Testing Guidelines

Currently, testing is manual. Future improvement: automated tests.

### Manual Testing Checklist

**Before Every PR:**

- [ ] Application launches without errors
- [ ] Can initialize system and login
- [ ] Villages extract correctly
- [ ] Khatas extract correctly
- [ ] Search/filter works
- [ ] Selection works (all, village-wise, individual)
- [ ] Excel upload works (valid/invalid files)
- [ ] Excel template downloads
- [ ] Processing completes successfully
- [ ] PDF automation works (or fails gracefully)
- [ ] Export to Excel works
- [ ] Error log generates correctly
- [ ] Sounds play (welcome, completion)
- [ ] UI responsive, no freezing

**For PDF Changes:**

- [ ] PDFs save to correct folders
- [ ] Filenames follow format
- [ ] Merging works correctly
- [ ] Handles missing/corrupted PDFs

**For Excel Changes:**

- [ ] Valid Excel uploads successfully
- [ ] Invalid Excel shows error
- [ ] Mobile numbers parsed correctly
- [ ] Missing mobile uses default

---

## 📚 Documentation

### When to Update Docs

- **README.md**: User-facing changes
- **CLAUDE.md**: Technical architecture changes
- **CHANGELOG.md**: All notable changes
- **Docstrings**: New functions/classes

### Documentation Style

- **Clear and concise**
- **Examples for complex features**
- **Screenshots for UI changes**
- **Step-by-step for workflows**

---

## ❓ Questions?

- **General**: Open a [GitHub Discussion](https://github.com/ORIGINAL_OWNER/ri-automation/discussions)
- **Bugs**: Open an [Issue](https://github.com/ORIGINAL_OWNER/ri-automation/issues)
- **Security**: Email [security contact - add if needed]

---

## 🎖️ Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md (future)
- Mentioned in release notes
- Credited in commit history

---

**Thank you for contributing to RI Automation System!**

*Together, we're making life easier for Revenue Inspectors across Odisha.* 🚀
