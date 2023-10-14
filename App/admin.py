from django.contrib import admin
from .models import AppModel
class AppAdmin(admin.ModelAdmin):
    class Meta:
        model = AppModel
        fields = ['isim','konu','mesaj']




admin.site.register(AppModel,AppAdmin)
