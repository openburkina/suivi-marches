from django.contrib import admin
from ocds_awards.models import Award, Supplier, AwardAmendment, AwardDocument, AwardItem

class ItemInline(admin.StackedInline):
    model = AwardItem

class DocumentInline(admin.StackedInline):
    model = AwardDocument

class MilestoneInline(admin.StackedInline):
    model = AwardAmendment

class SupplierInline(admin.StackedInline):
    model = Supplier

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline, DocumentInline, MilestoneInline, SupplierInline
    ]
