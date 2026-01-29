from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'bio', 'birth_date')
    search_fields = ('bio',)
    list_filter = ('birth_date',)
