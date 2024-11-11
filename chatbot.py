
import pyttsx3
import time
engine = pyttsx3.init()
engine.say("hi dear i am cypher how can i help you ? please enter your name  ")
engine.runAndWait()



curr = time.ctime()

name = input("Enter your name : ")
print("Hi", name, "How can i assist you ?")


# Celsius to Fahrenheit conversion function
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


for i in range (10000):  
  chat=str(input("ask some question:"))
  if chat == "what is your name":
     print("My name is cypher")
  elif chat == "who made you":
     print("Madhurjya(sssniperspider) made me") 
  elif chat == "what are you doing":
     print("Nothing, i am just waiting for your question to serve you better answer.....thank you")
  elif chat == "quit":
     break
  elif chat == "hi":
     print("hello")
  elif chat == "how are you":
     print("i am fine") 
  elif chat == "what is the time now":   
     print("Current time:", curr)
  elif chat == "can you convert celsius to fahrenheit":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F") 
     
  else :
     print("i cann't understand what are you say!!!.....sorry")