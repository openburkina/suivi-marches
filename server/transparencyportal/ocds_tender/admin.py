from django.contrib import admin
from .models import Buyer, Tender, TenderItem, TenderDocument, TenderMilestone, Tenderer

admin.site.register(Buyer)
admin.site.register(Tender)
admin.site.register(TenderItem)
admin.site.register(TenderDocument)
admin.site.register(TenderMilestone)
admin.site.register(Tenderer)
