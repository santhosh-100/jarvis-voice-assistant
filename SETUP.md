# Jarvis Voice Assistant - Setup Guide

## Quick Start

### Step 1: Install Python
Make sure you have Python 3.8 or higher installed.

### Step 2: Clone Repository
```bash
git clone https://github.com/santhosh-100/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

### Step 3: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

**Note:** PyAudio installation can be tricky. If you encounter issues:

**Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

**Mac:**
```bash
brew install portaudio
pip install pyaudio
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install python3-pyaudio
```

### Step 5: Run Jarvis
```bash
python jarvis.py
```

## Configuration

Edit `config/settings.py` to customize:
- Speech language
- Voice speed and volume
- API keys
- Custom commands

## Available Commands

### General
- "hello" / "hi" - Greeting
- "who are you" / "what is your name" - Identity
- "exit" / "quit" - Stop assistant

### Information
- "what time is it" - Current time
- "what is today's date" - Today's date
- "weather" - Current weather

### Entertainment
- "tell me a joke" - Random joke

### System Control
- "open notepad" - Open applications
- "open calculator" - Open calculator

## Troubleshooting

### Microphone Not Detected
- Check system audio settings
- Ensure microphone is connected and enabled
- Test with: `python -m speech_recognition`

### "No module named 'pyaudio'"
- Install using pipwin (Windows) or system package manager (Linux/Mac)

### Speech Recognition Not Working
- Check internet connection
- Speak clearly and slowly
- Try adjusting microphone sensitivity in settings

### Permission Denied on Linux
```bash
sudo usermod -a -G audio $USER
# Log out and back in
```

## Advanced Features

### Enable Debug Mode
In `config/settings.py`, set:
```python
'DEBUG_MODE': True
```

### Add Custom Commands
Edit `modules/command_processor.py` to add new commands:
```python
if 'your command' in command:
    return "Your response here"
```

### API Integrations
Get free API keys for:
- Weather: https://openweathermap.org/api
- News: https://newsapi.org/
- ChatGPT: https://openai.com/api/

Add keys to `config/settings.py`

## Next Steps

1. Customize commands for your needs
2. Add weather API key for live weather
3. Integrate with smart home devices
4. Add machine learning for personalization

## Support

For issues, check:
- PyAudio installation guide
- SpeechRecognition documentation
- Google Speech-to-Text setup

---

Enjoy using Jarvis! 🤖
