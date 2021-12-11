from django.contrib import admin
from .models import Release, ReleaseAward, ReleaseContract, ReleaseParty, ReleasePartyRole, Record


class AwardInline(admin.StackedInline):
    model = ReleaseAward

class ReleaseInline(admin.StackedInline):
    model = Release
    readonly_fields = ['ocid', 'date']

class ContractInline(admin.StackedInline):
    model = ReleaseContract

class PartyRoleInline(admin.StackedInline):
    model = ReleasePartyRole

class PartyInline(admin.StackedInline):
    model = ReleaseParty

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    inlines = [
        ReleaseInline
    ]

@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    inlines = [
        AwardInline, ContractInline, PartyInline
    ]
