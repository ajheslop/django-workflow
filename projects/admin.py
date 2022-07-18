from atexit import register
from django.contrib import admin
from .models import Project, Review, Tag #place model in here for it to be visible in the admin panel.
# Register your models here. you will be able to see the tables in the admin panel here.

admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)