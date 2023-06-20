import pyttsx3
import time
from pygame import mixer, _sdl2

while True:
    # Get the text needed and convert it to mp3
    text = input('Enter your text: ')
    print('Saying:', text)

    # Initialize the engine and save the text to an mp3 file
    with pyttsx3.init() as engine:
        engine.save_to_file(text, 'text.mp3')
        engine.runAndWait()

    print()

    # Play the mp3 over the microphone
    mixer.init()

    print("Inputs:", _sdl2.audio.get_audio_device_names(True))
    print("Outputs:", _sdl2.audio.get_audio_device_names(False))

    mixer.init(devicename='CABLE-A Input (VB-Audio Virtual Cable A)')  # Initialize it with the correct device
    mixer.music.load("text.mp3")  # Load the mp3
    mixer.music.play()  # Play it

    while mixer.music.get_busy():  # Wait for the music to finish playing
        time.sleep(1)
