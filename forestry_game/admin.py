from django.contrib import admin
from .models import Level, Report

# Register your models here.

class LevelAdmin(admin.ModelAdmin):
 	pass

class ReportAdmin(admin.ModelAdmin):
 	pass

admin.site.register(Level, LevelAdmin)
admin.site.register(Report, ReportAdmin)