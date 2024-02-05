from django.contrib import admin
from .models import Demande, Contact, Role, Utilisateur, Register, login, Booking


# Register your models here.

admin.site.register(Demande)
admin.site.register(Contact)
admin.site.register(Role)
admin.site.register(Utilisateur)
admin.site.register(Register)
admin.site.register(login)
admin.site.register(Booking)


