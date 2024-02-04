import speech_recognition as sr

def speech_to_text():
    # Create a speech recognition object
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Speak something...")

        try:
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds

            # Use the Google Web Speech API to recognize the audio
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text  # Return the recognized text

        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Error with the speech recognition service; {e}")
            return None

if __name__ == "__main__":
    recognized_text = speech_to_text()

    if recognized_text:
        print("Stored text:", recognized_text)
        # Now you can use 'recognized_text' for further processing or store it in a variable
