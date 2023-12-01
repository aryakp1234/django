from django.contrib import admin
from. models import *
# Register your models here.


class Department_display(admin.ModelAdmin):
    list_display=['dept']

class Hod_display(admin.ModelAdmin):
    list_display=['hodname','dept']

class Tutor_display(admin.ModelAdmin):
    list_display=['tname','hodname']


admin.site.register(Department,Department_display)
admin.site.register(Hod,Hod_display)
admin.site.register(Tutor,Tutor_display)