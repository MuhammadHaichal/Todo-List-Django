from django.shortcuts import redirect, render
from .models import todoModels

def index(request):
    todo_data = todoModels.objects.all()
    context = {
            'datalist' : todo_data,
            }

    if request.method == "POST":
        #print(request.POST)
        data_taks = request.POST['add']
        data_taks_db = todoModels.objects.create(judulTodo = data_taks)
       
    return render(request, 'todo/index.html', {'context' : context})


def remove(request, removeItems):
    remove_todo = todoModels.objects.filter(id = items).delete()
    return redirect('/')


def clear(request):
    remove_todo = todoModels.objects.all().delete()
    return redirect('/')


