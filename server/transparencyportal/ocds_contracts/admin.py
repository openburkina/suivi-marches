from django.contrib import admin
from ocds_contracts.models import Contract, ContractDocument, ContractItem

admin.site.register(Contract)
admin.site.register(ContractDocument)
admin.site.register(ContractItem)
