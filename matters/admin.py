from multiprocessing.connection import Client
from django.contrib import admin

# Register your models here.

from .models import User, Associate, Team, State, Court, Dispute, Client, Advice, Deal

admin.site.register(User)
admin.site.register(Associate)
admin.site.register(Team)
admin.site.register(State)
admin.site.register(Court)
admin.site.register(Dispute)
admin.site.register(Client)
admin.site.register(Advice)
admin.site.register(Deal)