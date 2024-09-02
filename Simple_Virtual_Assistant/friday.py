import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

friday = pyttsx3.init()
# getProperty(): lay giong, setProperty(): chon giong
voice = friday.getProperty('voices')
# voice[0].id: nam, voice[1].id: nu
friday.setProperty('voices', voice[1].id)

def speak(audio):
    print('C.O.M.A.Y.: ' + audio)
    friday.say(audio)
    friday.runAndWait()

def time():
    Time = datetime.datetime.now().strftime('%I: %M: %p')
    speak(Time)
    
def welcom():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour < 12:
        speak('Good morning sir!')
    elif hour >=12 and hour < 18:
        speak('Good afternoon sir!')
    elif hour >=18 and hour < 24:
        speak('Good night sir!')
    speak('How can I help you!')
    
def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language = 'en')
        print('Sept: ' + query)
        return query
    except sr.UnknownValueError:
        print('Please repeat or typing the command!')
        query = str(input('Your order is: '))
        return query
    except sr.RequestError as e:
        print(f"Sorry, there was an issue with the request; {e}")
        return "" #tra ve chuoi rong neu k nhan dien dc
    
if __name__ == "__main__":
    welcom()
    while True:
        query = command()
        if query: #ktra neu query k la null or none
            if "google" in query.lower():
                speak('What should I search boss?')
                search = command()
                if search:
                    url = f"https://www.google.com/search?q={search}"
                    wb.get().open(url)
                    speak(f'Here is your {search} on google')
            if "youtube" in query.lower():
                speak('What should I search boss?')
                search = command()
                if search:
                    url = f"https://www.youtube.com/search?q={search}"
                    wb.get().open(url)
                    speak(f'Here is your {search} on youtube')
            elif "open music" in query.lower():
                meme = r"C:\Users\pc\Downloads\Cạn Tình Như Thế Remix.mp3"
                os.startfile(meme)
            elif "time" in query.lower():
                time()
            elif "quit" in query.lower():
                speak('CoMay is quitting sir. Goodbye boss!')
                quit()