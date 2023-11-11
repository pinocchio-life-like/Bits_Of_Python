import speech_recognition as sr

# create a recognizer object
r = sr.Recognizer()

# use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak something...")
    # listen for audio and store it in audio_data variable
    audio_data = r.record(source, duration=5)
    print("Recognizing...")

    # recognize speech using Google Speech Recognition
    text = r.recognize_google(audio_data)
    print(f"You said: {text}")
