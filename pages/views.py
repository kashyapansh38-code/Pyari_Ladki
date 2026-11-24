from django.shortcuts import render


def home(request):
    return render(request, 'pages/index.html')


def fun(request):
    return render(request, 'pages/fun.html')


def motivation(request):
    return render(request, 'pages/motivation.html')


def message(request):
    return render(request, 'pages/message.html')