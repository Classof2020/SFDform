from django.shortcuts import render

# Create your views here.
from .models import Programming_Competition, NOSKode
from .forms import Programming_Competition_Form, NOSKode_Form

def home(request):
    template_name = 'index.html'
    return render(request,template_name)

def Programming_Competition(request):
    if request.method =='POST':
        form = Programming_Competition_Form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('home')
    else:
        form = Programming_Competition_Form()
    template_name = 'Programming_Competition.html'
    context = {'form':form}
    return render(request,template_name,context)

def NOSKode(request):
    if request.method =='POST':
        form = NOSKode_Form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('home')
    else:
        form = NOSKode_Form()
    template_name = 'NOSKode.html'
    context = {'form':form}
    return render(request,template_name,context)
