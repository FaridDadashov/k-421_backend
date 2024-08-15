# admin.py
from django.contrib import admin
from .models import Contact  # Ensure the path to Contact is correct

admin.site.register(Contact)
