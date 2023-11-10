# import speech_recognition as sr

# create a recognizer object
r = sr.Recognizer()

# use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak now...")
    # listen for audio and convert it to text
    audio = r.listen(source)

try:
    # recognize speech using Google Speech Recognition
    text = r.recognize_google(audio, language='en-US')
    print("You said: ", text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
