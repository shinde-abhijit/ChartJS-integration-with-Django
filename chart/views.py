from django.shortcuts import render, redirect
from .models import CountryPopulation
from .forms import CountryPopulationForm


# Create your views here.
def home(request):
    data = CountryPopulation.objects.all()
    if request.method == 'POST':
        form = CountryPopulationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CountryPopulationForm()
    context ={
        'data': data,
        'form': form,
    }
    return render(request, 'base.html', context)