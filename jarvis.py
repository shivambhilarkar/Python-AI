import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import subprocess


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


print("----------------------------------------------------------------------------------------------")
#   it shows the symbol image file of robot
#print(''' ``````````````````````/syys/``````````````````````
#`````````````````````+hhhhhh+`````````````````````
#`````````````````````:hhhhhh:`````````````````````
#``````````````````````.yhhy.``````````````````````
#``````````````````````.yhhs.``````````````````````
#`````````````````-/oyhhhhhhhhyo/-`````````````````
#``````````````./yhhhhhhhhhhhhhhhhy/```````````````
#`````````````/yhhhhhhhhhhhhhhhhhhhhy/`````````````#
#````````````shhhhhhhhhhhhhhhhhhhhhhhho````````````
#```````````ohhhhhhhhhhhhhhhhhhhhhhhhhho```````````
#``````````:hhhhhhhhhhhhhhhhhhhhhhhhhhhh-``````````
#````-+++.`+hhhhhyssyhhhhhhhhhhhysshhhhh+`.+++-````
#```:hhhh.`ohhhs-````-shhhhhhh+.````:yhho`-hhhh:```
#```/hhhh.`ohhh```````.hhhhhho```````/hho`-hhhh/```
#```/hhhh.`ohhh-``````:hhhhhhy```````ohho`-hhhh/```
#```/hhhh.`ohhhh+:--:ohhhhhhhhy+:--/shhho`-hhhh/```
#````+yyy.`ohhhhhhhhhhhhhhhhhhhhhhhhhhhho`.yyy+````
#``````````ohhhhhhhhyyyyyyyyyyyyhhhhhhhho``````````
#``````````ohhhhhhh+````````````+hhhhhhho``````````
#``````````ohhhhhhh/````````````/hhhhhhho``````````
#``````````.-------.````````````.-------.``````````
#``````.ooooooooooooooooooooooooooooooooooo+.``````
#``````:hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh:``````
#``````:hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh:``````
#``````-yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy-``````''')


#      for showing imagge in python
# importing Image class from PIL package 
#from PIL import Image 
# creating a object 
#im = Image.open("E:\py\jarvis.jpg")
#im.show() 



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon")
        speak("Good Afternoon!")   

    else:
       print("Good Evening")
       speak("Good Evening!")  
  #  print("I am Jarvis Sir. Please tell me how may I help you") 
    print("Hello World I am Robot")#Speed 1 terahertz, memory 1 zeta byte.")
   # speak("I am Jarvis Sir. Please tell me how may I help you") 
    speak("Hello World I am Robot")# Speed 1 terahertz, memory 1 zeta byte.")

    print("how may i help you sir")
    speak("how may i help yu sir")  


    print("===================================================================================")    
def takeCommand():
                                                                        #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...") 
        speak("Say that again please..") 
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif  'google it' in query: 
			speak('searching on google.....')
			query = query.replace("google", "")
			results=googlesearch.summary(query, sentences=1)
			speak("result obtained on google is..")
			print(results)
			speak(results)
         
        elif 'who are you' in query:
            print("my name is jarvis")
            speak("my name is jarvis")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'open gmail' in query:
            webbrowser.open("www.gmail.com") 

        elif 'play music' in query:
            music_dir = 'E:\\study\\j7prime\\mymusic\\My Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        
        #elif 'play video' in query:
         #   video_dir='E:\\Videos\\languages'
          #  videos = os.listdir(video_dir)
           # print(videos)
           #os.startfile(os.path.join(video_dir, videos[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

       # elif 'open code' in query:
        #    codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #    os.startfile(codePath)

        elif 'email to shivam' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "shivambhilarkar1999@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")  

        elif 'facebook' in query:
          webbrowser.open('www.facebook.com')

        elif 'instagram' in query:
            webbrowser.open('instagram.com')
        

        elif 'weather in india' in query:
            webbrowser.open('https://www.accuweather.com/en/in/india-weather')

        elif 'flipkart' in query:
            webbrowser.open('www.flipkart.com')

        elif 'amazon' in query:
            webbrowser.open('www.amazon.in')

        elif 'firefox' in query:
            import subprocess
            subprocess.call(['C:\\Program Files\\Mozilla Firefox\\firefox.exe'])

        elif 'mobile' in query:
            webbrowser.open('https://www.google.com/search?client=firefox-b-d&q=best+mobiles+in+market')


        elif 'chrome'in query:
            import subprocess
            subprocess.call(['C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'])


        elif 'news' in query:
            webbrowser.open('https://www.indiatoday.in/news.html')

        elif 'search' in query:
            try: 
	            from googlesearch import search 
            except ImportError: 
	              print("No module named 'google' found") 
                     # to search 
            query = "youtube"
            for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
	                 print(j) 



        elif 'games' in query:
            webbrowser.open('https://www.google.com/search?client=firefox-b-d&q=best+games+for+pc')





        else:
            print("Sorry Sir ,I dont understand what you are trying to say")
            speak("i dont understand what you are trying to say")




        
 