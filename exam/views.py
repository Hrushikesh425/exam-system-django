from django.db.models.base import Model
from django.shortcuts import render
from exam.models import Exam
# Create your views here.

def exam(request):
    exam = Exam.objects.all()
    return render(request, "exam.html", {"exam": exam, "count": 0})
