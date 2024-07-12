from django.contrib import admin
from app.models import Insight

# Register your models here.

@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    list_display=['intensity','sector','topic']
    search_fields = ['topic']
