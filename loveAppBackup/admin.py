from django.contrib import admin
from .models import Reply_of_Massage

# Register your models here.


@admin.register(Reply_of_Massage)
class Reply_of_MassageAdmin(admin.ModelAdmin):
    list_display = ['id',"replay"]