from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Choice, Question

def home(request):

    context = {
        'nome': 'antedeguemon',
        'idade': 34,
        'frutas': ['maçã', 'banana', 'uva']
    }

    return render(request, 'home.html', context)

def dashboard(request):
    question = Question.objects.first()

    return render(
        request,
        'dashboard.html',
        {
            'question': question
        }
    )

def landingpage(request):
    return render(request, 'landingpage.html')

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(
            pk=request.POST["choice"]
        )

    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "meninoDjango/dashboard.html",
            {
                "question": question,
                "error_message": "Você não selecionou uma opção.",
            },
        )

    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(
            reverse("meninoDjango:results", args=(question.id,))
        )

def results(request, question_id):
    question = get_object_or_404(
        Question,
        pk=question_id
    )

    return render(
        request,
        "results.html",
        {
            "question": question
        }
    )