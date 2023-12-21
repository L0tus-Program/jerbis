import pyaudio
import speech_recognition as sr
import os


def ouvir_microfone():
    microfone = sr.Recognizer()

    # Usando microfone
    with sr.Microphone() as source:
        # Chama o algoritmo de redução de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa:\n")

        audio = microfone.listen(source)

    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        if "navegador" in frase:
            os.system("start brave.exe")
        # print("Voce disse: ", frase)
    except sr.UnknownValueError:
        print("Nao entendi")
        return ("Erro")
    return (frase)


print(ouvir_microfone())
