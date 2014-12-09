from django.contrib import admin
from transcriptions.models import ENAnnotation, ARAnnotation

# Register your models here.
admin.site.register(ARAnnotation)
admin.site.register(ENAnnotation)
