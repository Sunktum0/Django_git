from django.shortcuts import render

# Пример представления для главной страницы
def home(request):
    return render(request, 'fourth_task/home.html', {'pagename': 'Главная страница'})

# Пример представления для страницы магазина
def shop(request):
    return render(request, 'fourth_task/shop.html', {'pagename': 'Магазин'})

# Пример представления для страницы корзины
def cart(request):
    return render(request, 'fourth_task/cart.html', {'pagename': 'Корзина'})

# Пример представления с контекстом
def example_view(request):
    # Изменяем формат данных: передаем единый список
    context = {
        'games': ['Atomic Heart', 'Cyberpunk 2077']
    }
    return render(request, 'fourth_task/example_template.html', context)