from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForms, TodoUpdateForms

def home(request):
    todos = Todo.objects.all()
    return render(request , 'home.html', context= {'todos':todos})

def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', context={"todo":todo})

def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success (request ,'todo deleted successfully', extra_tags='')
    messages.warning (request ,'You need to add more todos')
    return redirect('home')


def create(request):
    if request.method=='POST':
        form= TodoCreateForms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], body=cd['body'] , created=cd['created'])
            messages.success(request, 'Todo created successfully' , 'success')
            return redirect('home')
            
    else:
        form=TodoCreateForms()
    return render(request, 'create.html', {'form':form})

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    # render(request, 'detail.html', context={"todo":todo})
    if request.method== 'POST':
        form = TodoUpdateForms(request.POST, instance = todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ok','success')
            # return redirect('details', todo_id)
            return redirect('home')
    else:
        form = TodoUpdateForms()
    return render(request, 'update.html' , {'form':form})
