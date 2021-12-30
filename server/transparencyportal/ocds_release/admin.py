from django.contrib import admin

from ocds_master_tables.admin import Entity
from .models import Release, ReleaseAward, ReleaseContract, Record, Role, Target


class AwardInline(admin.StackedInline):
    model = ReleaseAward

class ReleaseInline(admin.StackedInline):
    model = Release
    readonly_fields = ['ocid', 'date']

class RoleInline(admin.StackedInline):
    model = Role
    extra = 1

class ContractInline(admin.StackedInline):
    model = ReleaseContract

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    inlines = [
        ReleaseInline
    ]

@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    inlines = [
        AwardInline, ContractInline, RoleInline
    ]

admin.site.register(Target)
