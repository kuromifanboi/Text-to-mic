from multiprocessing.connection import wait
import pyttsx3
import time
from pygame import mixer


while True:
    #get the text needed and convert it to mp3
    text = input('Enter your text: ')
    print('saying: ' + text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.save_to_file(text, 'text.mp3')
    engine.runAndWait()
    print('\n')


    #play the mp3 over the microphone
    mixer.init()
    mixer.music.load('text.mp3')
    mixer.music.play()
    time.sleep(5)
    mixer.music.stop()
    mixer.quit()
    time.sleep(1)
    print('\n')