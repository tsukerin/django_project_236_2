from django.contrib import admin
from .models import Answers, Sertif

@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('title', 'Users', 'Skills', 'Score', 'Date')
    list_filter = ('Users', 'Skills', 'Date')
    search_fields = ('title', 'Users__username', 'Skills__title')
    list_per_page = 20

@admin.register(Sertif)
class SertifAdmin(admin.ModelAdmin):
    list_display = ('title', 'Users', 'Blank', 'Date')
    list_filter = ('Users', 'Blank', 'Date')
    search_fields = ('title', 'Users__username', 'Blank__title')
    list_per_page = 20
