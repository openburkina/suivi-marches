from django.contrib import admin
from .models import Buyer, Tender, TenderItem, TenderDocument, TenderMilestone, Tenderer

admin.site.register(Buyer)

class ItemInline(admin.StackedInline):
    model = TenderItem

class DocumentInline(admin.StackedInline):
    model = TenderDocument

class MilestoneInline(admin.StackedInline):
    model = TenderMilestone

class TendererInline(admin.StackedInline):
    model = Tenderer

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline, DocumentInline, MilestoneInline, TendererInline
    ]
