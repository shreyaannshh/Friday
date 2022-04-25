import pyttsx3
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[1].id)
engine.setProperty("rate",180)

def Speak(Text):
    print(f"{Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("  ")

Speak("Friday here")
