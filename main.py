from listener import listen
from speaker import speak

command = listen()

if command:
    speak(f"You said {command}")