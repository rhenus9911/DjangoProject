from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question

def main(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list':question_list}
    return render(request, 'main/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'main/detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('main:detail', question_id=question.id)