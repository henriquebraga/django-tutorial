from django.contrib import admin

# Register your models here.
from mysite.polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    """Table to many choices"""
    model = Choice
    extra = 1

class QuestionModelAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    search_fields = ('question_text', 'pub_date')


admin.site.register(Question, QuestionModelAdmin)
admin.site.register(Choice)