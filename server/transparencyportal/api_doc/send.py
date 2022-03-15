import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC6c401b26a6594367ea84e1c328a21767"
auth_token = "329ac07d5d800eb7a5c79e30ee0600fa"



def broadcastMsgToWhatsapp():
   client = Client(account_sid, auth_token)
   message = client.messages.create(
      from_='whatsapp:+15049107543',
      body='Hello, from cafdo!',
      to='whatsapp:+23565574029'
   )
   print(message.sid)   
   print("Envoi avec succés")
   
broadcastMsgToWhatsapp()

