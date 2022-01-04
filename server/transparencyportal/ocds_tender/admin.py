from django.contrib import admin

from .models import Tender, TenderDocument, TenderItem, TenderMilestone


class ItemInline(admin.StackedInline):
    model = TenderItem

class DocumentInline(admin.StackedInline):
    model = TenderDocument

class MilestoneInline(admin.StackedInline):
    model = TenderMilestone

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline, DocumentInline, MilestoneInline
    ]
