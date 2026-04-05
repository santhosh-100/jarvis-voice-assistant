# Jarvis Configuration Settings

SETTINGS = {
    # Speech Recognition Settings
    'LANGUAGE': 'en-US',
    'TIMEOUT': 10,  # Seconds to wait for speech input
    'PHRASE_TIME_LIMIT': 10,  # Maximum duration of phrase
    
    # Text-to-Speech Settings
    'SPEECH_RATE': 150,  # Words per minute
    'SPEECH_VOLUME': 0.9,  # Volume level (0.0 to 1.0)
    
    # API Keys (Add your own)
    'OPENWEATHER_API_KEY': '',  # Get from https://openweathermap.org/api
    'NEWS_API_KEY': '',  # Get from https://newsapi.org/
    'LOCATION': 'Auto',  # Default location for weather
    
    # Command Settings
    'DEBUG_MODE': True,  # Enable debug output
    'RESPONSE_TIMEOUT': 5,  # Timeout for external APIs
}

# Custom Commands (Add your own)
CUSTOM_COMMANDS = {
    # Example: 'command': 'response'
    # 'hello': 'Hello sir, how can I assist?',
}