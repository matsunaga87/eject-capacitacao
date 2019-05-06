from django.contrib import admin

# Register your models here.

from .models import Curses

class CursesAdmin(admin.ModelAdmin):

	list_display = ['name', 'slug', 'start_date', 'created_at']
	search_fields = ['name', 'slug'] 
	prepopulated_fields = {'slug':('name',)}


admin.site.register(Curses, CursesAdmin)