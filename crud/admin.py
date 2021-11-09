from django.contrib import admin

# Register your models here.
from .models import Land_Details

class Land_Details_Admin(admin.ModelAdmin):
    list_display = ("title", "description")
admin.site.register(Land_Details,Land_Details_Admin)
