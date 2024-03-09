from django.shortcuts import render
from .models import Todo

def home(requests):
    todos=Todo.objects.all()
    task3_todos=Todo.objects.filter(title="Title 1")
    task4_todos=Todo.objects.exclude(title="Title 1")
    return render(requests,'home.html',{'todos':todos,'task3_todos':task3_todos,'task4_todos':task4_todos})

def detail_todo(requests,todo_id):
    todo=Todo.objects.get(id=todo_id)
    return render(requests,'detail.html',{'todo':todo})
# def task_three(requests):
#     todo=Todo.objects.filter(title="Title 1")
#     return render(requests,'task_3.html',{'todos':todo})
# def task_four(requests):
#     todos=Todo.objects.exclude(title="Title 1")
#     return render(requests,'task_4.html',{'todo':todos})