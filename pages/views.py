from django.http import HttpResponse
from django.shortcuts import render

from pages.forms.formLogin import LoginForm

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'


# Create your views here.

def homePageView(request):
    return HttpResponse("Hello, World!")


def get_user(request):
    if request.method == 'POST':
        print('POST')
    else:
        print(request.method )
    form = LoginForm()
    return render(request, 'usuario.html', {'form': form})
