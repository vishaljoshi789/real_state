from django.contrib import admin
from .models import properties_detail, properties_image, intrested_user

# Register your models here.

class PropertyImageInline(admin.TabularInline):
    model = properties_image
    extra = 3

class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline, ]

admin.site.register(properties_detail, PropertyAdmin)
admin.site.register(intrested_user)
# admin.site.register(properties_image)
