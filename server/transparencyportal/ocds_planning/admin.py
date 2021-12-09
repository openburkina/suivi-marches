from django.contrib import admin
from ocds_planning.models import Planning, PlanningDocument

class DocumentInline(admin.StackedInline):
    model = PlanningDocument

@admin.register(Planning)
class PlanningAdmin(admin.ModelAdmin):
    inlines = [DocumentInline]
