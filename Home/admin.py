from django.contrib import admin
# from Services.models import Services
from Home.models import FormSubmit


# Register your models here.
# class ServicesAdmin(admin.ModelAdmin):
#     list_display = ('name','email', 'phone', 'description')

class SaveEnquery(admin.ModelAdmin):
    list_display = ('name','email', 'phone', 'description')

admin.site.register(FormSubmit,SaveEnquery)



