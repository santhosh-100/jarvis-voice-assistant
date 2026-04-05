import speech_recognition as sr
from modules.text_to_speech import speak
from modules.command_processor import process_command
from config.settings import SETTINGS
import time
import sys

class Jarvis:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.is_running = True
        
    def listen(self):
        """Listen to microphone input and return recognized text"""
        try:
            with self.microphone as source:
                print("🎤 Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=SETTINGS['TIMEOUT'])
            
            print("🔄 Processing...")
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        
        except sr.UnknownValueError:
            response = "Sorry, I didn't catch that. Could you repeat?"
            speak(response)
            return None
        except sr.RequestError as e:
            response = f"Error with speech recognition service: {e}"
            speak(response)
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def run(self):
        """Main loop for Jarvis"""
        print("=" * 50)
        print("🤖 JARVIS VOICE ASSISTANT ACTIVATED")
        print("=" * 50)
        speak("Jarvis activated. How can I assist you?")
        
        while self.is_running:
            try:
                command = self.listen()
                
                if command is None:
                    continue
                
                # Check for exit commands
                if any(word in command for word in ['exit', 'quit', 'stop', 'goodbye']):
                    speak("Goodbye sir. Jarvis shutting down.")
                    self.is_running = False
                    break
                
                # Process the command
                response = process_command(command)
                speak(response)
                
            except KeyboardInterrupt:
                print("\n\n⚠️  Interrupted by user")
                speak("Jarvis shutting down.")
                self.is_running = False
                break
            except Exception as e:
                print(f"Error in main loop: {e}")
                speak("An error occurred. Please try again.")

def main():
    try:
        jarvis = Jarvis()
        jarvis.run()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()