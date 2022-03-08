from email.mime import audio
import speech_recognition as sr
import os
import pyautogui
import time


pyautogui.PAUSE = 1
def ouvir():

    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        microfone.adjust_for_ambient_noise(source)

        print("Diga algo: ")

        audio = microfone.listen(source)

    try:

        frase = microfone.recognize_google(audio, language='pt-BR')
        os.system("start Chrome.exe")
        time.sleep(2)
        pyautogui.write("https://pt.wikipedia.org/wiki/" + frase)
        pyautogui.press("enter")
        print(frase)

    except sr.UnknownValueError:
        print("Não Entendi!!") 

    return frase

ouvir()              


