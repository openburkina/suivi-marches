import os
from django.dispatch import receiver
from django.db.models.signals import post_save
#from twilio.rest import Client
import requests
from rest_framework.response import Response
from ocds_master_tables.constants import page_id_1, facebook_access_token_1
from ocds_release.models import Release

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC6c401b26a6594367ea84e1c328a21767"
auth_token = "329ac07d5d800eb7a5c79e30ee0600fa"


def broadcastMsgToWhatsapp():
   # client = Client(account_sid, auth_token)
   # message = client.messages.create(
   #    from_='whatsapp:+15049107543',
   #    body='Hello, from cafdo!',
   #    to='whatsapp:+23565574029'
   # )
   # print(message.sid)   
   print("Envoi avec succés")


@receiver(post_save, sender=Release, dispatch_uid="facebook_publish") 
def FacebookPublishView(sender, instance, *args, **kwargs):
  # ocid = kwargs.items
   ocid = instance.ref_record.ocid
   msg = ("Des modifications viennent d'être apporté au marché numero (numero du marché) portant sur (l'objectif du marché),allez sur la page du marché pour plus d'informations ", [ocid])
   payload = {
       'message': msg,
       'access_token': facebook_access_token_1
       }
   post_url ='https://graph.facebook.com/{}/feed'.format(page_id_1)
   r = requests.post(post_url, payload)
   return Response(status=None)
   



