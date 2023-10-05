from django.contrib import admin
from .models import NewCategory, NewLineItem, budget
# Register your models here.

admin.site.register(budget)
admin.site.register(NewCategory)
admin.site.register(NewLineItem)