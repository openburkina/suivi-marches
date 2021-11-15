from django.contrib import admin
from .models import Address, Buyer, ContactPoint

admin.site.register(Address)
admin.site.register(Buyer)
admin.site.register(ContactPoint)
