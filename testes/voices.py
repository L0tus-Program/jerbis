import pyttsx3

engine = pyttsx3.init()

# Obtém informações sobre as vozes disponíveis
voices = engine.getProperty('voices')

for voice in voices:
    print("ID:", voice.id)
    print("Name:", voice.name)
    print("Lang:", voice.languages)
    print("Gender:", voice.gender)
    print("Age:", voice.age)
    print("\n")
