import sounddevice as sd
import soundfile as sf
import speech_recognition as sr

SAMPLE_RATE = 16000       #frames per sec
DURATION = 3

def listen():
    print("Listening...")

    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1
    )

    sd.wait()

    sf.write("input.wav", audio, SAMPLE_RATE)

    recognizer = sr.Recognizer()

    with sr.AudioFile("input.wav") as source:       #open audio file
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)

        print(f"You said: {text}")

        return text.lower()

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""

    except sr.RequestError:
        print("Speech service unavailable.")
        return ""