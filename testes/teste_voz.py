import speech_recognition as sr
import os
import pyttsx3

def ouvir_microfone():
    microfone = sr.Recognizer()

    # Usando microfone
    with sr.Microphone() as source:
        # Chama o algoritmo de redução de ruídos no som
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa:\n")

        audio = microfone.listen(source)

    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        if "navegador" in frase:
            os.system("start chrome.exe")

        # Síntese de voz para reproduzir o que foi reconhecido
        engine = pyttsx3.init()
        engine.say(frase)
        engine.runAndWait()

        return frase
    except sr.UnknownValueError:
        print("Não entendi")
        return "Erro"

print(ouvir_microfone())
