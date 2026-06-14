# WhatsApp Auto-Responder Bot

A learning project built while exploring Python automation, OpenAI API integration,
clipboard handling, and desktop automation concepts.

The bot monitors a WhatsApp Web chat open in Chrome, detects when a specific contact
sends a message, generates a reply using OpenAI's GPT-3.5 Turbo, and sends it back
automatically through the browser.

---

## Features

- Detects new messages from a configured sender in WhatsApp Web
- Reads chat history by drag-selecting the chat area and copying to clipboard
- Sends the full chat context to OpenAI's Chat Completions API for reply generation
- Pastes and sends the reply through WhatsApp Web
- Skips duplicate replies — will not respond to the same message twice
- All credentials and screen coordinates stored in `.env` — nothing hardcoded
- Logs all actions and errors to both the terminal and `bot.log`
- Configurable bot persona via environment variable

---

## Technologies Used

- Python 3.10+
- [PyAutoGUI](https://pyautogui.readthedocs.io/) — mouse movement and keyboard automation
- [Pyperclip](https://pyperclip.readthedocs.io/) — clipboard read and write
- [OpenAI Python SDK](https://github.com/openai/openai-python) — GPT-3.5 Turbo API
- [python-dotenv](https://pypi.org/project/python-dotenv/) — `.env` file support

---

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/yourusername/whatsapp-auto-responder.git
cd whatsapp-auto-responder
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Create your `.env` file**

```bash
copy .env.example .env    # Windows
cp .env.example .env      # macOS / Linux
```

Open `.env` and fill in your values. At minimum, set `OPENAI_API_KEY`.

---

## Environment Variables

| Variable | Required | Default | Description |
|---|---|---|---|
| `OPENAI_API_KEY` | Yes | — | Your OpenAI API key |
| `SENDER_NAME` | No | `jagruthi` | Name of the contact to monitor |
| `POLL_INTERVAL` | No | `5` | Seconds between each check |
| `BOT_PERSONA` | No | Naruto persona | System prompt sent to the AI |
| `CHROME_ICON_X/Y` | No | `1639, 1412` | Chrome taskbar icon position |
| `CHAT_START_X/Y` | No | `1003, 237` | Top-left corner of the chat area |
| `CHAT_END_X/Y` | No | `1499, 1268` | Bottom-right corner of the chat area |
| `SEND_BTN_X/Y` | No | `1808, 1328` | WhatsApp send button position |

All coordinate defaults come from the original development setup. They will not
work on a different screen. Use `mouse_tracker.py` to find the correct values.

---

## Finding Screen Coordinates

Before running the bot, run the included tracker utility:

```bash
python mouse_tracker.py
```

Move your cursor to each of the following positions and note the X, Y values:

1. Chrome icon in the taskbar
2. Top-left corner of the WhatsApp chat message area
3. Bottom-right corner of the WhatsApp chat message area
4. The WhatsApp send button or message input field

Add the values to your `.env` file using the variable names in the table above.

---

## Usage

1. Open Chrome and go to [https://web.whatsapp.com](https://web.whatsapp.com).
2. Open the chat you want to monitor. Make sure Chrome is fully visible — do not minimize it.
3. Run the bot:

```bash
python bot.py
```

The bot clicks on Chrome to bring it into focus, then polls the chat every few seconds.
When it detects a new message from the configured sender, it generates and sends a reply.

Press `Ctrl+C` to stop. All activity is logged to `bot.log`.

---

## Project Structure

```
whatsapp-auto-responder/
├── bot.py               # Main bot loop and all automation logic
├── config.py            # Loads settings from .env
├── mouse_tracker.py     # Utility to find screen coordinates
├── .env.example         # Template — copy to .env and fill in values
├── requirements.txt     # Python dependencies
├── .gitignore
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
└── PROJECT_STRUCTURE.md
```

---

## Limitations

- **Screen-specific coordinates.** The bot relies on fixed pixel positions. Any change
  to window placement, monitor resolution, scaling, or taskbar layout will break it.
- **No dynamic window detection.** It cannot locate WhatsApp Web automatically — the
  window must be open and positioned consistently.
- **One-on-one chats only.** Group chats are not supported.
- **Timestamp parsing.** Sender detection splits on `/2026]` — the year in WhatsApp's
  copied timestamp format. This will need updating for other years.
- **No persistent memory.** Chat context is not saved across bot restarts.
- **Windows-focused.** Developed and tested on Windows. Some pyautogui features may
  require additional packages on Linux (e.g. `python-xlib`, `scrot`).

---

## Future Improvements

- Use image recognition (e.g. OpenCV template matching) to locate the chat window
  dynamically instead of fixed coordinates
- Add support for monitoring multiple contacts
- Store conversation history in a local file or SQLite database for better context
- Build a small setup GUI for coordinate configuration
- Add unit tests for the sender detection and config loading logic
- Make the timestamp split pattern configurable to handle different years

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
