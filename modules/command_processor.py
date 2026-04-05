import datetime
import subprocess
import os
import random
from modules.integrations import get_weather, get_current_time

def process_command(command):
    """Process voice commands and return responses"""
    
    # Greeting commands
    if any(word in command for word in ['hello', 'hi', 'hey']):
        greetings = [
            "Hello sir. How can I assist you?",
            "Greetings. What do you need?",
            "Hello. At your service."
        ]
        return random.choice(greetings)
    
    # Identity commands
    if any(word in command for word in ['name', 'who are you', 'your name']):
        return "I am Jarvis, your personal voice assistant. A digital consciousness created to serve you."
    
    # Time commands
    if any(word in command for word in ['time', 'what time']):
        current_time = get_current_time()
        return f"The current time is {current_time}"
    
    # Date commands
    if any(word in command for word in ['date', 'today']):
        today = datetime.date.today().strftime("%B %d, %Y")
        return f"Today is {today}"
    
    # Weather commands
    if any(word in command for word in ['weather', 'temperature']):
        weather_info = get_weather()
        return weather_info
    
    # Joke commands
    if any(word in command for word in ['joke', 'make me laugh']):
        jokes = [
            "Why did the Python break up with Java? Because it needed a Pascal!",
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
            "Why did the developer go broke? He used up all his cache!",
            "What's a programmer's favorite hangout place? Foo Bar!"
        ]
        return random.choice(jokes)
    
    # Open applications (Windows/Linux/Mac)
    if 'open' in command:
        app = command.replace('open', '').strip()
        try:
            if 'notepad' in app or 'text' in app:
                if os.name == 'nt':  # Windows
                    subprocess.Popen('notepad.exe')
                else:  # Linux/Mac
                    subprocess.Popen(['gedit'])
                return f"Opening {app}"
            
            elif 'calculator' in app or 'calc' in app:
                if os.name == 'nt':
                    subprocess.Popen('calc.exe')
                else:
                    subprocess.Popen(['gnome-calculator'])
                return "Opening calculator"
            
            else:
                return f"I'm not sure how to open {app}"
        except Exception as e:
            return f"Failed to open {app}: {str(e)}"
    
    # System information
    if 'system' in command or 'info' in command:
        return "System information retrieved. Please check your terminal."
    
    # Default response
    return "I didn't understand that command. Could you please repeat or try something different?"