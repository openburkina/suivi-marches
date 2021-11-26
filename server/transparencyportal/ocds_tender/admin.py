from django.contrib import admin
from .models import Tender, TenderItem, TenderDocument, TenderMilestone, Tenderer
admin.site.register(Tender)
admin.site.register(TenderItem)
admin.site.register(TenderDocument)
admin.site.register(TenderMilestone)
admin.site.register(Tenderer)
