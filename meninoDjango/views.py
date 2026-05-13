from django.shortcuts import render

def home(request):

    context = {
        'nome': 'antedeguemon',
        'idade': 34,
        'frutas': ['maçã', 'banana', 'uva']
    }

    return render(request, 'home.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')


def landingpage(request):
    return render(request, 'landingpage.html')
