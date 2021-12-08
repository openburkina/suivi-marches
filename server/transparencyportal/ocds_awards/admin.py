from django.contrib import admin
from ocds_awards.models import Award, Supplier, AwardAmendment, AwardDocument, AwardItem

admin.site.register(Award)
admin.site.register(Supplier)
admin.site.register(AwardAmendment)
admin.site.register(AwardDocument)
admin.site.register(AwardItem)
