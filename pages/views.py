from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from pages.forms.formLogin import LoginForm

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'

class RegisterPageView(TemplateView):
    template_name = 'register.html'
    
class BlockPageView(TemplateView):
    template_name = 'bloque.html'

class BlockchainPageView(TemplateView):
    template_name = 'blockchain.html'


# Create your views here.

def handler404(request, *args, **kwargs):
    return HttpResponseRedirect('/')

def homePageView(request):
    return HttpResponse("Hello, World!")


def get_user(request):
    if request.method == 'POST':
        print('POST')
    else:
        print(request.method )
    form = LoginForm()
    return render(request, 'usuario.html', {'form': form})
