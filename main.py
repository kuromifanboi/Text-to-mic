from multiprocessing.connection import wait
import pyttsx3
import time
from pygame import mixer, _sdl2
import sounddevice as sd

while True:
    #get the text needed and convert it to mp3
    text = input('Enter your text: ')
    print('saying: ' + text)
    engine = pyttsx3.init()
    engine.save_to_file(text, 'text.mp3')
    engine.runAndWait()
    print('\n')


    #play the mp3 over the microphone
    mixer.init()

    print("Inputs:", _sdl2.audio.get_audio_device_names(True))
    print("Outputs:", _sdl2.audio.get_audio_device_names(False))