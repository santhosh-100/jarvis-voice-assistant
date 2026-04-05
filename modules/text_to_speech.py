import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Speed of speech
        self.engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)
    
    def speak(self, text):
        """Synthesize and play text as speech"""
        print(f"🔊 Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

# Initialize TTS engine
_tts = TextToSpeech()

def speak(text):
    """Speak the given text"""
    _tts.speak(text)