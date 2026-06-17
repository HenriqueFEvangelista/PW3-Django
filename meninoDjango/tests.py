import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question, Choice


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)

        future_question = Question(pub_date=time)

        self.assertIs(
            future_question.was_published_recently(),
            False
        )

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)

        old_question = Question(pub_date=time)

        self.assertIs(
            old_question.was_published_recently(),
            False
        )

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59)

        recent_question = Question(pub_date=time)

        self.assertIs(
            recent_question.was_published_recently(),
            True
        )


def create_question(question_text, days):
    """
    Cria uma pergunta com base no número de dias
    deslocados em relação ao momento atual.
    """
    time = timezone.now() + datetime.timedelta(days=days)

    return Question.objects.create(
        question_text=question_text,
        pub_date=time
    ) 

class VoteViewTests(TestCase):

    def test_vote_increments_choice_votes(self):
        question = Question.objects.create(
            question_text="Qual sua cor favorita?",
            pub_date=timezone.now()
        )

        choice = Choice.objects.create(
            question=question,
            choice_text="Azul",
            votes=0
        )

        response = self.client.post(
            reverse(
                "meninoDjango:vote",
                args=(question.id,)
            ),
            {
                "choice": choice.id
            }
        )

        choice.refresh_from_db()

        self.assertEqual(choice.votes, 1)
        self.assertEqual(response.status_code, 302)

class VoteViewErrorTests(TestCase):

    def test_vote_without_choice(self):
        question = Question.objects.create(
            question_text="Pergunta teste",
            pub_date=timezone.now()
        )

        response = self.client.post(
            reverse(
                "meninoDjango:vote",
                args=(question.id,)
            ),
            {}
        )

        self.assertContains(
            response,
            "Você não selecionou uma opção."
        )

class ResultsViewTests(TestCase):

    def test_results_view(self):
        question = Question.objects.create(
            question_text="Pergunta teste",
            pub_date=timezone.now()
        )

        response = self.client.get(
            reverse(
                "meninoDjango:results",
                args=(question.id,)
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["question"],
            question
        )