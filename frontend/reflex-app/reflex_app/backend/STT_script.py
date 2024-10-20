import speech_recognition as sr
from playsound import playsound

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to capture speech and convert it to text
def speech_to_text():
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)

        playsound("./beep_sound_1.wav")

        print("Listening for your speech...")
        # Capture the audio from the microphone
        audio_data = recognizer.listen(source)
        print("Converting speech to text...")

        try:
            # Convert the speech to text using Google's Speech Recognition
            text = recognizer.recognize_google(audio_data)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

# Call the function
if __name__ == "__main__":
    speech_to_text()
