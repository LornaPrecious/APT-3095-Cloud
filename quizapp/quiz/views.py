from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    question = Question.objects.all()
    total_questions= Question.objects.count()
    context = {
        'question':question,
        'total_questions':total_questions,
    }
    return render(request, 'quiz/index.html', context)

def landing(request):
    context ={}
    return render(request,'quiz/landing.html',context)
