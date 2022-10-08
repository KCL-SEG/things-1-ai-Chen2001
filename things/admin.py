from django.contrib import admin

# Register your models here.
from .models import Thing
@admin.register(Thing)
class ThingAdmin(admin.ModelAdmin):
    list_display=['name','description','quantity',]
