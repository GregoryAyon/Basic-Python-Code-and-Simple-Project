#pip install pywin32
from win32com.client import Dispatch

def speak(str):
    speak = Dispatch(("SAPI.Spvoice"))
    speak.speak(str)

if __name__ == '__main__':
    with open("text.txt") as f:
        for item in f.readlines():
            speak(item)