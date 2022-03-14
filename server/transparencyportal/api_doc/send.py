import pywhatkit
import datetime as t
def broadcastMsgToWhatsapp():
   # using Exception Handling to avoid
   # unprecedented errors
   try:
   # sending message to receiver
   # using pywhatkit
      pywhatkit.sendwhatmsg("+22666020547",
                              "Hello from cafdo test",
                              13,
                              35
                            )
      print("Successfully Sent!")
   
   except:
      # handling exception
      # and printing error message
      print("An Unexpected Error!")