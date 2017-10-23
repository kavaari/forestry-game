from django.contrib import admin
from .models import CustomUser, Level, Report

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
	pass

class LevelAdmin(admin.ModelAdmin):
 	pass

class ReportAdmin(admin.ModelAdmin):
 	pass

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Report, ReportAdmin)