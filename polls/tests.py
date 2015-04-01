from django.test.utils import setup_test_environment
setup_test_environment()

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
import datetime

from django.utils import timezone
from . import models

class QuestionMethodTests(TestCase):
    def setUp(self):
        models.Question.objects.create(question_text='test quest 1')
        models.Question.objects.create(question_text='test quest 2')
    def test_was_published_recently(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = models.Question(pub_date = time, question_text = 'test quest')
        future_question.save()
        self.assertEqual(future_question.was_published_recently(), False)
    def test_get_all_question(self):
        client = Client()
        response = client.get(reverse('polls:index'))
        self.assertTrue(False, msg=response.context)
