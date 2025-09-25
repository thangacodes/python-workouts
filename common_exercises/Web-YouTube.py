########## Opening YouTube video links through Python Script #############

## Here, we are using a custom function called as "watch_python_tutorial()" to call. 
## The webbrowser module provides a high-level interface to allow displaying Web-based documents to users.

print ("HOW TO WATCH YOUTUBE VIDEOS USING PYTHON")
import time
import webbrowser # Importing webbrowser
import webbrowser as web ## Calling std library webbrowser as web
def watch_steve_smith_netsession(): # custom function
    web.open("https://www.youtube.com/watch?v=Yba4NNp9Kso")

## Calling steve smith net session video using
watch_steve_smith_netsession()
print("You are watching steve smith net practice session")
time.sleep (5)

def watch_python_tutorial():
    web.open("https://www.youtube.com/watch?v=cdkzcNu4k34")
## Calling custom function 
watch_python_tutorial()
print("You are watching whatsapp message automation tutorial")
a="thanks for watching python fun"
print(a.upper())
