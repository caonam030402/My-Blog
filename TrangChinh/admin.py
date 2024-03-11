from django.contrib import admin

# Register your models here.

from . models import Image,Post,NhatKy


admin.site.register([Image,Post,NhatKy])