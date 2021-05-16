from django.shortcuts import render
#
from .forms import TodoForm
from .models import Todo
from django.http import HttpResponseRedirect
from django.urls import reverse  #using reverse utility so that django should handle redirect with parameters
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required 
def get_showing_todos(request,todos):

    # request.GET give us every parameter in the url
    # we need to do .get('filter') since it is a dictionary
    if request.GET and request.GET.get('filter'):
        if request.GET.get('filter')=='complete':
            return todos.filter(is_completed=True)
        
        if request.GET.get('filter')=='incomplete':
            return todos.filter(is_completed=False)

    return todos


@login_required
def index(request):
    # getting all of the todo of the login user
    todos = Todo.objects.filter(owner=request.user)

    completed_count = todos.filter(is_completed=True).count()
    incompleted_count = todos.filter(is_completed=False).count()
    all_count = todos.count()


    context = {
        'todos': get_showing_todos(request,todos), 
        'all_count': all_count, 
        'completed_count': completed_count,
        'incompleted_count': incompleted_count
        }
    return render(request, 'todo/index.html', context)


@login_required
def create_todo(request):
    form = TodoForm()
    context = {'form': form}

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_completed = request.POST.get('is_completed', False) # false as default
        # is_completed value will be off or on

        todo = Todo()

        todo.title = title
        todo.description = description
        todo.is_completed = True if is_completed == "on" else False
        todo.owner = request.user

        
        todo.save()

        messages.add_message(request, messages.SUCCESS, 'Todo created successfully')

        # to redirect, here with don't know the url name but we know the page name and what it needs ie parameter in this case id
        # we use reverse for this
        return HttpResponseRedirect(reverse("todo", kwargs={'id': todo.pk}))

    
    return render(request, 'todo/create-todo.html', context)


@login_required
def todo_detail(request, id):
    # egtting todo with a specific id
    # get_object_or_404 this will make sure django serves us the corrent template if the todo is not found
    todo = get_object_or_404(Todo, pk=id)
    context = {'todo': todo}
    return render(request, 'todo/todo-detail.html', context)


@login_required
def todo_delete(request, id):
    todo = get_object_or_404(Todo, pk=id)
    context = {'todo': todo}

    # if there's a post request
    if request.method == 'POST':
        if todo.owner == request.user:
            #delete the todo
            todo.delete()
            messages.add_message(request, messages.SUCCESS, 'Todo deleted successfully')
            return HttpResponseRedirect(reverse('home')) # redirect to home page
        
        return render(request, 'todo/todo-delete.html', context)

    return render(request, 'todo/todo-delete.html', context)


@login_required
def todo_edit(request, id):
    #
    todo = get_object_or_404(Todo, pk=id)
    form = TodoForm(instance=todo)

    context = {'todo': todo, 'form':form}


    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_completed = request.POST.get('is_completed', False) # false as default
        # is_completed value will be off or on

        todo.title = title
        todo.description = description
        todo.is_completed = True if is_completed == "on" else False

        if todo.owner == request.user:
            todo.save()

            messages.add_message(request, messages.SUCCESS, 'Todo updated successfully')

   
        # to redirect, here with don't know the url name but we know the page name and what it needs ie parameter in this case id
        # we use reverse for this
        return HttpResponseRedirect(reverse("todo", kwargs={'id': todo.pk}))


    return render(request, 'todo/todo-edit.html', context)




