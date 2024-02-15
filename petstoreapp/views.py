from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm

# Create your views here.
def home(request):
    return render(request, 'petstoreapp/home.html')

def pets_list(request):
    pets = Pet.objects.all()
    return render(request, 'petstoreapp/pets_list.html', {'pets': pets})

def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)   
        if form.is_valid():
            form.save()
            return redirect('pets_list')
    else:
        form = PetForm()
    return render(request, 'petstoreapp/pet_create.html', {'form': form})