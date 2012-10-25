from django.contrib import admin
from deckocards.models import *

class CardAdmin(admin.ModelAdmin):
	list_display = ('rank', 'suit')

admin.site.register(Card, CardAdmin)