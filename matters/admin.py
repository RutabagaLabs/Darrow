from multiprocessing.connection import Client
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from .models import User, Associate, Team, State, Court, Dispute, Client, Advice, Deal


class StateResource(resources.ModelResource):

    class Meta:
        model = State
        skip_unchanged = True

class StateAdmin(ImportExportModelAdmin):
    resource_class = StateResource


class CourtResource(resources.ModelResource):

    class Meta:
        model = Court
        skip_unchanged = True

class CourtAdmin(ImportExportModelAdmin):
    resource_class = CourtResource


admin.site.register(User)
admin.site.register(Associate)
admin.site.register(Team)
# admin.site.register(State)
# admin.site.register(Court)
admin.site.register(Dispute)
admin.site.register(Client)
admin.site.register(Advice)
admin.site.register(Deal)
admin.site.register(State, StateAdmin)
admin.site.register(Court, CourtAdmin)