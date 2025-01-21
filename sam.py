import pyttsx3

def main():
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Get user input
    text = input("Type something to be spoken: ")

    # Configure voice properties (optional)
    engine.setProperty('rate', 150)  # Speed (default is 200 words per minute)
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

    # Speak the input text
    print("Speaking...")
    engine.say(text)

    # Wait for the speech to complete
    engine.runAndWait()
    print("Done speaking!")

if __name__ == "__main__":
    main()
