from django.contrib import admin

from ocds_awards.admin import AwardInline

from .models import Release, Record, Role, Target


class ReleaseInline(admin.StackedInline):
    model = Release
    readonly_fields = ['ocid', 'date']

class RoleInline(admin.StackedInline):
    model = Role
    extra = 1

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    inlines = [
        ReleaseInline
    ]

@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    inlines = [
        AwardInline, RoleInline
    ]

admin.site.register(Target)
