
# Create your views here.
from django.shortcuts import render
from django.views import View

# Классовое представление
class ClassBasedView(View):
    template_name = 'second_task/template_class_view.html'

    def get(self, request):
        return render(request, self.template_name)

# Функциональное представление
def FunctionalView(request):
    return render(request, 'second_task/template_functional_view.html')