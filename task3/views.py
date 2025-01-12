from django.shortcuts import render

def home(request):
    return render(request, 'third_task/index.html')

def store(request):
    store_items = {
        'Игра 1': 100,
        'Игра 2': 150,
        'Игра 3': 200,
    }
    return render(request, 'third_task/store.html', {'store_items': store_items})

def cart(request):
    return render(request, 'third_task/cart.html')