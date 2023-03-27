from django.contrib import admin

# Register your models here.
from .models import Visitor

class VisitorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Visitor, VisitorAdmin)