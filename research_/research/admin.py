from django.contrib import admin

from .models import (Notification, 
                    profile,
                    paper,
                    payment)

admin.site.register(profile)
admin.site.register(paper)
admin.site.register(payment)
admin.site.register(Notification)
# Register your models here.
