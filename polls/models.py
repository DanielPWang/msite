from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=4096, verbose_name='问题', help_text='长度4096')
    pub_date = models.DateTimeField(verbose_name='Published date', auto_now_add=True, editable=False)
    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def pub_date(self):
        return self.question.pub_date
    def __str__(self):
        return "%s - %d" % (self.question.question_text + self.choice_text, self.votes)
    class Mate():
        ordering = ['votes', 'choice_text']

