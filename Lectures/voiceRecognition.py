import speech_recognition as sr
import webbrowser

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    
    print("You said : {}".format(text))
    if 'Google' or 'google' in text:
        url = "http://www.google.com"
        webbrowser.open(url) #This opens without any condition!!!! error!!
    else:
        print("Sorry could not recognize what you said")