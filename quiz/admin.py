from django.contrib import admin
from quiz.models import Course
from quiz.models import Question
from quiz.models import Result







# # Register your models here.
# class CustomerAdmin(admin.ModelAdmin):
#     list_display=('name','user','locality','city','zipcode','state')

admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Result)



# Register your models here.

