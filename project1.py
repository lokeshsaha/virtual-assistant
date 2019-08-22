import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir")

    elif hour>=12 and hour<18:
        speak("Good afternoon sir")

    else:
        speak("Good evening sir")

    speak("iam Lokesh assistant sir.please tell me how may i help you?")               
def takecommand():
    #it takes microphone input from the user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")  
    except Exception as e:
        #print(e)
        print("say that again please...")
        return "None"
    return query
def sendEmail(to,content):
 
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com', 'your_password')
    server.sendmail('your_email@gmail.com', to, content)
    server.close()
        

if __name__ == '__main__':
     wishMe()
#while True:
if 1:  
        query = takecommand().lower()
        if 'wikipedia' in query:
             speak ('searching wikipedia...')
             query= query.replace ("wikipedia","")
             results=wikipedia.summary(query,sentences=25)
             speak('According to wikipedia')
             print(results)
             speak(results)

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 
        elif 'open stackoverflow' in query:
             webbrowser.open("stackoverflow.com")
        elif 'open facebook' in query:
             webbrowser.open("facebook.com")
        elif 'open amazon' in query:
             webbrowser.open("amazon.com")
        elif 'play music' in query:
             music_dir = 'F:\\music\\My old'
             songs=os.listdir(music_dir)
             print(songs)
             os.startfile(os.path.join(music_dir,songs[5]))
        elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"sir, the time is {strTime}")           
        elif 'open code' in query:
             codepath = "C:\\Users\\LOKESH SAHA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(codepath)
        elif 'email to Lokesh' in query:
             try:
                 speak("what should i say")
                 content = takecommand()
                 to = "receiver_email@gmail.com"
                 sendEmail(to, content)
                 speak("email has been sent sucessfully")
             except Exception as e:
                 print(e)
                 speak("sorry!Lokesh bro iam not able to sent the email at the moment")


               
              
            
