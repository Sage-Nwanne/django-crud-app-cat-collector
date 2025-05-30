from django.shortcuts import render
# Add the following import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat



def home(request):
     return render(request, 'home.html')


def about(request):
     return render(request, 'about.html')

def cat_index(request):
     cats = Cat.objects.all()  # Query the database for all Cat objects
     return render(request, 'cats/index.html', {'cats': cats})

def cat_detail(request, cat_id):
     cat = Cat.objects.get(id=cat_id)
     return render(request, 'cats/detail.html', {'cat': cat})



class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
  


class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']
    



class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'