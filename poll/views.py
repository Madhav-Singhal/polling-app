from django.shortcuts import render, redirect
from .models import PollModel
from .forms import PollForm
from django.http import HttpResponse

# Create your views here.

def list(request):
    

    object = PollModel.objects.all()
    return render(request, 'home.html', {'obj':object})

def create(request):
    form = PollForm
    if request.method == 'POST':
        form = PollForm(request.POST or None)
        if form.is_valid():
           
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def view(request, id):

    obj = PollModel.objects.get(pk = id)

    if request.method == "POST":
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            obj.count1 +=1
        elif selected_option == 'option2':
            obj.count2 +=1
        elif selected_option == 'option3':
            obj.count3 +=1
        else:
            return HttpResponse(400, 'invalid form')
        
        obj.save()
        
        return redirect('results', obj.id)

    return render(request, 'view.html', {'query': obj})


def results(request, id):

    obj = PollModel.objects.get(pk = id)
    return render(request, 'results.html', {'query': obj})

    


