from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'debtors/index.html')


def chart(request):
    return render(request, 'debtors/chart.html')

def page404(request):
    return render(request, 'debtors/404.html')
