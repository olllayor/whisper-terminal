import speech_recognition as sr
import os
import whisper
import warnings
from colorama import Fore, Style

model = whisper.load_model("base")

warnings.filterwarnings('ignore')

filename = "audio.wav"
if os.path.exists(filename):
    os.remove(filename)

while True:
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 5
    with sr.Microphone() as source:
        print("Listening...120sec")       
        try:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=120)
            print("Running...")
        except sr.WaitTimeoutError:
            print("No speech detected for 120 seconds. Recording stopped.")
            continue  # Restart the loop if timeout occurs

    with open(filename, "wb") as audio_file:
        audio_file.write(audio.get_wav_data())
    print("Audio saved as 'audio.wav'")

    print("OpenAI Whisper request started.")

    result = model.transcribe(f"{filename}")
    text = result["text"]
    if text is None:
        print("\n\t[ERROR] OpenAI API returned empty response.\n")
    else:
        print("OpenAI Whisper request finished.")
    print("\n\n\n--------------------------\n\n\n")
    print(Fore.GREEN + Style.BRIGHT + text, end='')
    print(Style.RESET_ALL)
    print("\n\n\n--------------------------\n\n\n")
