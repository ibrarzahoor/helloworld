import time
import random

print("Hi I am BOOT i am here to help you ")
time.sleep(2)
name = input("Hello, what is your name? ")
time.sleep(2)
print("Wellcome " + name)
boss = input("Who’s your boss?")
print("WOW GRATE PERSONLITY :" + boss)
time.sleep(1)
print("My master is IBRAR ZAHOOR. He Know how to train me")

feeling = input("How are you today? ")

time.sleep(2)
if "good" in feeling:
  print("I'm feeling good too!")
if "not good" in feeling:
  print("I'm with you !")
else:
  print("I'm sorry to hear that!")

time.sleep(2)
age = input("How old are you?")
time.sleep(2)
if "30>20" in age:
  print("you are too young")
else:
  print("this is the age to boost your slef")
  time.sleep(2)
favcolour = input("What is your favourite colour? ")
colours = ["Red", "Green", "Blue"]

time.sleep(2)
print("My favourite colour is " + random.choice(colours))
