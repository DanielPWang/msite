from django.contrib import admin
from . import models

site_title = '我的管理学习'
site_header = '我的管理学习'

# StackedInline
class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # in edit view. order. #fields = ["pub_date", "question_text"]
    fields = ["question_text"]
    # in list view. even method.
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # add filter
    list_filter = ['pub_date']
    # add search
    search_fields = ('question_text',)
    # show choice in question's view.
    inlines = [ ChoiceInline ]

class ChoiceAdmin(admin.ModelAdmin):
    # change order in edit view.
    # fields = ['question', 'votes', 'choice_text']
    # in edit view. group, classes=collapse
    fieldsets = [ (None, {'fields':['question']}),
        ('Answer', {'fields':['votes', 'choice_text'], 'classes':['collapse']}),
        ]
    list_display = ('question', 'votes', 'choice_text', 'pub_date')
    list_filter = ('question', 'votes')
    # TODO: try multi fields. search_fields = ('question', 'choice_text')
    search_fields = ('choice_text', )

admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choice, ChoiceAdmin)
