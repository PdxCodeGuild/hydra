from datetime import date

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect

from todo_app.models import ToDoItem

def home(request):
    Items = ToDoItem.objects.all() #This is the part that queries the database
    return render(request, 'pages/home.html', {'Items': Items}) # sends Json file the html template   -Joebird

def add(request):
    if request.method == 'GET':
        return render(request, 'pages/add.html')
    elif request.method == 'POST':
        description = request.POST['description']
        created_date = date.today()
        completed_date = None
        completed_boolean = False
        item = ToDoItem.objects.create(description=description, created_date=created_date, completed_date=completed_date, completed_boolean=completed_boolean)
        item.save()
        
        return redirect('home')


def complete(request):
    id = request.POST['id']
    item = ToDoItem.objects.get(id = id)
    item.completed_boolean = True
    item.completed_date = date.today()
    item.save()
    return redirect('home')

def delete(request):
    id = request.POST['id']
    item = ToDoItem.objects.get(id = id)
    item.delete()
    return redirect('home')







