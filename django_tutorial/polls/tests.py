from django.test import TestCase
from datetime import timedelta
from django.urls import reverse
from django.utils import timezone
from .models import Question

class QuestionModelTests(TestCase):
    def test_future_question(self):
        time = timezone.now() + timedelta(days=30)
        question = Question(pub_date=time)
        self.assertIs(question.was_published_recently(), False)


