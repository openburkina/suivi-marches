from django.contrib import admin
from .models import Release, ReleaseAward, ReleaseContract, ReleaseParty, ReleasePartyRole, Record

admin.site.register(Release)
admin.site.register(ReleaseAward)
admin.site.register(ReleaseContract)
admin.site.register(ReleaseParty)
admin.site.register(ReleasePartyRole)
admin.site.register(Record)
