from django.contrib import admin
from .models import Usuario, List, Wish

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Wish)
admin.site.register(List)
