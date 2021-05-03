from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.

def index (request):
    now = datetime.datetime.now()
    if now.month ==1 and now.day==1:
        answer = True
    else:
        answer = False
    return render(request, "newyear/index.html",
    {
        "answer": answer
    })
