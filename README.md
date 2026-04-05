# Jarvis Voice Assistant 🎙️

A Python-based voice assistant inspired by Iron Man's Jarvis. Control your system, execute commands, and interact with your computer using voice commands.

## Features

- 🎤 **Speech Recognition** - Listen to voice commands
- 🔊 **Text-to-Speech** - Respond with synthesized voice
- 💻 **System Control** - Execute system commands
- 🌐 **Web Integration** - Fetch data from APIs
- ⚙️ **Customizable** - Easy to extend with new commands
- 🎯 **Command Processing** - Intelligent command matching

## Requirements

- Python 3.8+
- Microphone (for voice input)
- Speakers (for voice output)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/santhosh-100/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the voice assistant:
```bash
python jarvis.py
```

Once running, speak your commands clearly. Jarvis will listen, process, and respond.

## Available Commands

- "hello jarvis" - Greeting
- "what is your name" - Identity
- "what time is it" - Current time
- "tell me a joke" - Random joke
- "open notepad" - Open applications
- "weather" - Current weather
- "exit" / "quit" - Stop the assistant

## Project Structure

```
jarvis-voice-assistant/
├── jarvis.py              # Main voice assistant script
├── modules/
│   ├── speech_recognition.py   # Speech input module
│   ├── text_to_speech.py        # Voice output module
│   ├── command_processor.py     # Command processing logic
│   └── integrations.py          # API integrations
├── config/
│   └── settings.py        # Configuration settings
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## Configuration

Edit `config/settings.py` to customize:
- Speech recognition language
- Voice speed and volume
- Command timeout
- Custom commands

## Extending Jarvis

Add new commands in `modules/command_processor.py`:

```python
def handle_custom_command(command):
    if "your command" in command:
        return "Your response"
```

## Troubleshooting

**Microphone not detected:**
- Check system audio settings
- Ensure microphone is connected and enabled

**Speech recognition not working:**
- Check internet connection (required for some engines)
- Speak clearly and slowly
- Adjust microphone sensitivity

## License

MIT License - Feel free to use and modify!

## Contributing

Pull requests are welcome! Please create a feature branch for any contributions.

## Future Enhancements

- [ ] GUI Interface
- [ ] Advanced NLP
- [ ] Smart home integration
- [ ] Machine learning for custom responses
- [ ] Multi-language support
- [ ] Browser automation

---

Made with ❤️ by Santhosh
