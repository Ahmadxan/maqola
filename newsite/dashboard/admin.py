from django.contrib import admin
from . import models


admin.site.register(models.Category)
admin.site.register(models.Customer)
admin.site.register(models.Material)
admin.site.register(models.GetInTouch)