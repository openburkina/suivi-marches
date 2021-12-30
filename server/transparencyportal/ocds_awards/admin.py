from django.contrib import admin
from ocds_awards.models import Award, AwardAmendment, AwardDocument, AwardItem


class ItemInline(admin.StackedInline):
    model = AwardItem

class DocumentInline(admin.StackedInline):
    model = AwardDocument

class MilestoneInline(admin.StackedInline):
    model = AwardAmendment

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline, DocumentInline, MilestoneInline
    ]
