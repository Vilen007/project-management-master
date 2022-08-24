from django.contrib import admin
from .models import *

admin.site.register(Project)
admin.site.register(Access)

admin.site.register(State)
admin.site.register(Task)
admin.site.register(Type)
admin.site.register(Info)
admin.site.register(Comment)
admin.site.register(Commenttask)
