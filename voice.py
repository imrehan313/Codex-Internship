import threading as t,time,datetime as d,requests as re,speech_recognition as sr,pyttsx3 as p,re as regex,os
# Use https://www.weatherapi.com/ for Weather API Key generation
# Use https://newsapi.org/ for News API Key generation


r=sr.Recognizer()

def setReminder(message,delay=2*60):
    time.sleep(delay)
    p.speak(message)
    print(message)

def checkWeather(cityName):
    api_key=os.getenv("WEATHER_API_KEY")
    p.speak(f"Checking the weather of {cityName}")
    response =re.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={cityName}&aqi=no").json()
    try:
      city=response["location"]["name"]
      time=response["location"]["localtime"]
      temp=response["current"]["temp_c"]
      lat=response["location"]["lat"]
      lon=response["location"]["lon"]
      
      print(f"City: {city}\nDate and Time: {time}\nTemperature: {temp}°C\nLatitude: {lat},Longitude: {lon}\n ")
      p.speak(f"The weather of {cityName} is {temp}°C at {time}")
     
    except Exception as e:
     print("There is no such city\n",e)  
    p.speak("There is no such city\n",e)
     
def checkNews(topic,from_date=d.date.today()-d.timedelta(days=7),to_date=d.date.today()):
    api_key=os.getenv("NEWS_API_KEY")
    p.speak(f"Extracting the article about topic {topic}")
    response=re.get(f"https://newsapi.org/v2/everything?q={topic}&from={from_date}&to={to_date}&sortBy=popularity&apiKey={api_key}").json()

    try:
     newsName=response["articles"][1]["source"]["name"]
     publishedDate=response["articles"][1]["publishedAt"]
     author=response["articles"][1]["author"]
     newsTitle=response["articles"][1]["title"]
     description=response["articles"][1]["description"]
     url=response["articles"][1]["url"]

     print(f"{newsName}\nPublished Date: {publishedDate}\nAuthor: {author}\nTitle: {newsTitle}\nDescription: {description}\nURL: {url}\n")   
     p.speak(f"the news about {topic} is {description}")
    
    except Exception as e:
     print("There is no News for the specified duration or topic\n",e)
     p.speak("There is no News for the specified duration or topic\n",e)
     
def runReminder():   
    try:  
      p.speak("Give the message for reminder")
      print("Give the message for reminder")

      with sr.Microphone() as src:
           message=r.listen(src)
           message=r.recognize_google(message).lower()
        
           p.speak("Give the delay for reminder")
           print("Give the delay for reminder")
           delay=r.listen(src,timeout=10)
           delay=r.recognize_google(delay)

      numbers = list(map(int, regex.findall(r'\d+', delay)))

      if len(numbers) == 1:
        totalSeconds = numbers[0]

      elif len(numbers) == 2:
          if "hour" in delay:
             hours, minutes = numbers
             totalSeconds = hours * 3600 + minutes * 60
          else:
             minutes, seconds = numbers
             totalSeconds = minutes * 60 + seconds

      else:
       hours, minutes, seconds = numbers
       totalSeconds = hours * 3600 + minutes * 60 + seconds

      p.speak(f"{totalSeconds} seconds")
      print(f"{totalSeconds} seconds")
      p.speak(f"Reminder is set for your message for the delay of {delay}")
      print("Reminder is set for your message for the delay of ",delay)
    
      t.Timer(totalSeconds,setReminder,args=([message,totalSeconds])).start()
      print("you can use other function, the message will automatically reminds you after specified time".title())
    except Exception as e:
      print(e if e else "")

def main():
 try:
     with sr.Microphone() as src:
      text=r.listen(src,timeout=5)
      text=r.recognize_google(text).lower()
      print(text)
     
     if "weather" in text:
      checkWeather(text.split(" ")[-1])

     elif "news" in text or "tell me about" in text:
      checkNews(text.split(" ")[-1])
    
     elif "reminder" in text or "notify" in text:
      t1= t.Thread(target=runReminder).start()

     else:
      p.speak("sorry")
      print("Sorry for the Inconvenience but i can only help you with Weather, News and Reminders Right Now")
 except Exception as e:
    print(e if e else "")
    
if __name__=="__main__":
 
 execute="max"
 print("I am here to help you")  
 while True: 
    try:
     with sr.Microphone() as src:
      userMessage=r.listen(src)
      userMessage=r.recognize_google(userMessage).lower()
      print(userMessage)
    
      if "exit" in userMessage :
        p.speak("Bye Bye")
        print("Bye Bye")
        break
      
      elif execute in userMessage:
       p.speak("how can i help you")
       print("how can i help you")
       main()
      else:
       pass
    except Exception as e:
          pass
       
