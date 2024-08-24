from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base/home.html' )

def profissional(request):
    return render(request, 'base/profissional.html')

def pessoal(request):
    return render(request, 'base/pessoal.html')