from django.contrib import admin
from ocds_implementation.models import Implementation, ImplementationDocument, ImplementationMilestone, Transaction

admin.site.register(Implementation)
admin.site.register(ImplementationDocument)
admin.site.register(ImplementationMilestone)
admin.site.register(Transaction)
