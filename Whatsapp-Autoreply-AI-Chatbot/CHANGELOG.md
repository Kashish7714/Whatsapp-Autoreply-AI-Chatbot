# Changelog

All notable changes to this project are documented here.

---

## [1.0.0] — 2026-05-16

### Added
- Core bot loop: monitors WhatsApp Web, generates AI replies, sends them automatically
- `config.py` — centralised configuration loaded from `.env` via `python-dotenv`
- `mouse_tracker.py` — utility script for finding screen coordinates
- Duplicate reply prevention using chat snapshot comparison
- Logging to both terminal and `bot.log` using Python's `logging` module
- Type hints and docstrings on all functions
- Full GitHub repository files: README, LICENSE, CONTRIBUTING, CHANGELOG, PROJECT_STRUCTURE

### Fixed
- **Critical:** Renamed `openai.py` → merged logic into `bot.py` to resolve Python
  module shadowing conflict (local `openai.py` was overriding the installed package)
- **Critical:** Removed WhatsApp chat messages accidentally pasted inside source code
- `time.slip(1)` → `time.sleep(1)` (AttributeError)
- `messages` → `message` in `is_last_message_from_sender` (NameError)
- `completion.choices[0].message.conetent` → `.content` (AttributeError, appeared twice)
- `pyautogui.hotkey('ctr', 'v')` → `'ctrl'` (paste was silently failing)
- Indentation error: reply block now correctly inside the `if sender` check
- Hardcoded empty API key (`" "`) replaced with environment variable
- Undefined `command` variable replaced with `chat_history` parameter
- Automation code moved out of module level and into `run_bot()` function
- `main.py` CPU hammering fixed with `time.sleep(0.1)` in the tracking loop
