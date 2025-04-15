from django.contrib import admin
from web_app.models import StatusModel

# Register your models here.
from .models import StatusModel,Album,Song

admin.site.register(StatusModel)
admin.site.register(Album)
admin.site.register(Song)
#admin.site.register(GeeksModel)