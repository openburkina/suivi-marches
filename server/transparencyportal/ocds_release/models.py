import datetime

from django.db import models

from ocds_release.custom_fields import ChoiceArrayField
from ocds_master_tables.models import Entity, Address, Value
from ocds_planning.models import Planning
from django.dispatch import receiver
from django.db.models.signals import post_save
import requests
from rest_framework.response import Response
from ocds_master_tables.constants import page_id_1, facebook_access_token_1

from .utils import to_json_publication
from .constants import INITIATION_TYPE, PARTY_ROLE, RELEASE_TAG_CHOICES

# TODO: When you have your own Client ID and secret, put down their values here:

class Target(models.Model):
    name = models.CharField(max_length=255)

class Record(models.Model):
    ocid = models.CharField(max_length=500, unique=True,null=True,blank=True)
    target = models.ForeignKey(Target, on_delete=models.PROTECT, null=True)
    implementation_address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True)
    implementation_value = models.ForeignKey(Value, on_delete=models.PROTECT, null=True)

    def save(self,*args, **kwargs):
        # update_or_create compîled_release
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.ocid)

class PublishedRelease(models.Model):
    ref_record = models.ForeignKey(Record, related_name='releases', on_delete=models.DO_NOTHING)
    release = models.JSONField()

class Role(models.Model):
    release = models.ForeignKey('Release', on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    role = ChoiceArrayField(models.CharField(max_length=255, choices=PARTY_ROLE), null=True)

class Release(models.Model):
    ref_record = models.OneToOneField(Record, related_name='compiled_release', on_delete=models.DO_NOTHING, null=True, blank=True)
    ocid = models.CharField(max_length=500, editable=False, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    tag = ChoiceArrayField(models.CharField(max_length=255, choices=RELEASE_TAG_CHOICES))
    initiation_type = models.CharField(max_length=255, default='tender', choices=INITIATION_TYPE)
    buyer = models.ForeignKey(Entity, related_name='releases', on_delete=models.DO_NOTHING, null=True, blank=True)
    planning = models.OneToOneField(Planning, on_delete=models.DO_NOTHING, null=True, blank=True)
    tender = models.OneToOneField('ocds_tender.Tender', on_delete=models.DO_NOTHING, null=True, blank=True)
    parties = models.ManyToManyField(Entity, through='Role')


    @property
    def step(self):
        for (step, verbose) in reversed(RELEASE_TAG_CHOICES):
            if step in self.tag:
                return step

    @property
    def suppliers(self):
        return self.parties.filter(role__role__contains=['supplier']).values_list('name', flat=True)

    def add_role(self, party, role_name):
        role_instance, created = Role.objects.get_or_create(release=self, entity=party)
        if role_instance.role:
            role_instance.role.append(role_name)
        else:
            role_instance.role = [role_name]
        role_instance.save()

    def remove_role(self, party, role_name):
        role_instance, created = Role.objects.get_or_create(release=self, entity=party)
        if role_instance.role:
            role_instance.role.remove(role_name)
        else:
            role_instance.role = [role_name]
        role_instance.save()

    def update_buyer_role(self):
        last_instance = Release.objects.get(pk=self.pk)
        if getattr(last_instance, 'buyer'):
            self.remove_role(getattr(last_instance, 'buyer'), 'buyer')
        if getattr(self, 'buyer'):
            self.add_role(getattr(self, 'buyer'), 'buyer')

    def set_ocid(self, *args, **kwargs):
        inc = self.ref_record.releases.count() + 1
        self.ocid = self.ref_record.ocid + '-' + str(inc) + '-' + str(self.date)

    def update_date(self, *args, **kwargs):
        self.date = datetime.datetime.now()

    def publish(self, *args, **kwargs):
        self_instance = Release.objects.get(pk=self.pk)
        publication = PublishedRelease.objects.create(ref_record=self.ref_record, release=to_json_publication(self_instance))
        publication.save()
        self.set_ocid()

    def save(self, *args, **kwargs):
        self.set_ocid(self, *args, **kwargs)
        if self.pk:
            self.update_date(self, *args, **kwargs)
        super().save(*args, **kwargs)

    def __str__(self):
        return '%s' % (self.ocid)

@receiver(post_save, sender=Release, dispatch_uid="facebook_publish") 
def FacebookPublishView(sender, instance,**kwargs):
  # ocid = kwargs.items
   ocid = instance.ref_record.ocid
   ide = instance.id
   target = instance.ref_record.target.name
   adresse = instance.ref_record.implementation_address
   valeur = instance.ref_record.implementation_value
   dates = instance.date
   bailleur = instance.buyer
   instanceId = "40"
   clientId = "tinto.jean@openburkina.bf"
   clientSecret = "9d787b21a3164a99bdbc04a3a1461daa"
# TODO: Customize the following 3 lines
   groupName = 'Cafdotest'  # FIXME
   groupAdmin = "22666020547"  # FIXME
   message = "Bonjour/Bonsoir cher(e) tous.Honneur vous informer qu'une modification vient\
   d'être apporté au marché numero %s.Marché portant sur le domaine de %s lancée le %s.Informations complémentaire\
   le bailleur de ce marché est %s et le marche couvre la ville de %s pour une valeur de %s.\
   Rendez vous sur le https://localhost:3000/projects/%d , pour plus d'informations" %(ocid,target,dates,bailleur,adresse,valeur,ide)  # FIXME
   headers = {
    'X-WM-CLIENT-ID': clientId, 
    'X-WM-CLIENT-SECRET': clientSecret
   }
   jsonBody = {
    'group_name': groupName,
    'group_admin': groupAdmin,
    'message': message
   }

   msg = ("Bonjour/Bonsoir cher(e) tous.Honneur vous informer qu'une modification vient\
   d'être apporté au marché numero %s.Marché portant sur le domaine de %s lancée le %s.Informations complémentaire\
   le bailleur de ce marché est %s et le marche couvre la ville de %s pour une valeur de %s.\
   Rendez vous sur le https://localhost:3000/projects/%d , pour plus d'informations" %(ocid,target,dates,bailleur,adresse,valeur,ide))
   payload = {
       'message': msg,
       'access_token': facebook_access_token_1
       }
   post_url ='https://graph.facebook.com/{}/feed'.format(page_id_1)
   #r = requests.post(post_url, payload)
   r = requests.post('http://api.whatsmate.net/v3/whatsapp/group/text/message/%s' %instanceId, headers=headers, json=jsonBody)
   return Response(status=None)






