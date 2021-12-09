from django.contrib import admin
from ocds_contracts.models import Contract, ContractDocument, ContractItem

class ItemInline(admin.StackedInline):
    model = ContractItem

class DocumentInline(admin.StackedInline):
    model = ContractDocument

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline, DocumentInline
    ]
