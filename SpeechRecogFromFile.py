# Import library
import speech_recognition as sr

# Create Recognizer
r = sr.Recognizer()
# Import audio file
audio_file = sr.AudioFile('Welcome.wav')
# Recognize speech
with audio_file as source:
    r.adjust_for_ambient_noise(source)  # Delete noise
    audio = r.record(source)
result = r.recognize_google(audio)
# Export result into a text document
with open('test.txt', mode='w') as file:
    file.write("Recognized text:")
    file.write("\n")
    file.write(result)
    print("ready!")
