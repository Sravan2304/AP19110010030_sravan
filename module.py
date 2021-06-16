import camelcase
import emoji
import pyttsx3
def conn_camelcase():
    a=input("Enter your data: ")
    x=camelcase.CamelCase()
    if a==x.hump(a):
        print(emoji.emojize(":thumbs_up:"))
    else:
        print("The converted data is: ")
        x=camelcase.CamelCase()
        print(x.hump(a))
        spk=pyttsx3.init()
        spk.say("Successfully converted")
        spk.runAndWait()