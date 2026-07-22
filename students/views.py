from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def students(request):
    students = [
        {
            "id": 1,
            "name": "John",
            "age": 25
        }
    ]

    return HttpResponse(students)
