from django.contrib import admin

from .models import Incoming, AssignedTo

admin.site.register(Incoming)
admin.site.register(AssignedTo)
