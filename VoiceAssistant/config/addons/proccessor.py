import wikipedia
from datetime import datetime
import webbrowser
import os
from utils.setup import response


def processor():
    while True:
            speech = input(":")
            if "Search for" in speech:
                assistant = ('Searching Wikipedia.. Please Wait')
                print(assistant), response(assistant)
                speech = speech.replace('Wikipedia', '')
                result = wikipedia.summary(speech, sentences=2), response("According To Wikipedia..")
                print(result), response(result)
            
            elif "open youtube" in speech:
                webbrowser.open("http://www.youtube.com")
                response("opening youtube")

            elif "open facebook" in speech:
                webbrowser.open("http://www.facebook.com")
                response("opening facebook")

            elif "open whatsapp" in speech:
                webbrowser.open("http://www.web.whatsapp.com")
                response("opening whatsapp")

            elif "open my learning website" in speech:
                webbrowser.open("http://www.w3school.com")
                response("opening your website")

            elif "i want to check something in my course" in speech:
                webbrowser.open("http://www.coursera.org")
                response("opening coursera website")

            elif "open udemy" in speech:
                webbrowser.open("http://www.udemy.com")
                response("opening udemy")

            elif "open stackoverflow" in speech:
                webbrowser.open("http://www.stackoverflow.com")
                response("opening stackoverflow")

            elif "open teams" in speech:
                webbrowser.open("http://www.teams.microsoft.com")
                response("opening microsoft teams")

            elif "open instagram" in speech:
                webbrowser.open("http://www.instagram.com")
                response("opening instagram")

            elif "open google" in speech:
                codePath = "C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"
                os.startfile(codePath)
                response("opening google")

            elif "close google" in speech:
                os.system("taskkill /f  /im chrome.exe")

            elif "search on google" in speech:
                response("what should i search on google sir")
                search = speech().lower()
                webbrowser.get("windows-default").open(f"{search}")

            elif "what is the time" in speech or "what time is it" in speech:
                now = datetime.now()
                current_time = now.strftime("%I:%M %p")
                response(current_time)

            elif "open code" in speech:
                codePath = "C:\\Users\\Dev Ed\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
                response("opening vscode")

            elif "open notepad" in speech:
                codePath = "notepad.exe"
                os.startfile(codePath)
                response("opening notepad")

            elif "close notepad" in speech:
                os.system("taskkill /f  /im notepad.exe")

            elif "open yahoo" in speech:
                webbrowser.open("http://www.yahoo.com")
                response("opening yahoo")

            elif "open gmail" in speech:
                webbrowser.open("http://www.mail.google.com")
                response("opening google mail")

            elif "open snapdeal" in speech:
                webbrowser.open("http://www.snapdeal.com")
                response("opening snapdeal")

            elif "open amazon store" in speech or "shop online" in speech:
                webbrowser.open("https://www.amazon.com")
                response("opening amazon store")

            elif "open flipkart store" in speech:
                webbrowser.open("http://www.flipkart.com")
                response("opening flipkart store")

            elif "open ebay store" in speech:
                webbrowser.open("http://www.ebay.com")
                response("opening ebay store")

            elif "open cmd" in speech:
                os.system("start cmd")

            elif "close cmd" in speech:
                os.system("taskkill /f  /im cmd.exe")

            elif "open downloads" in speech:
                codePath = "C:\\Users\\Dev Ed\\Downloads"
                os.startfile(codePath)
                response("opening downloads")
            
            else:
                response("Sorry I Don\'t Know That")