from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

# Create your views here.

def index(request):
    template = loader.get_template('polls/index.html')
    return HttpResponse("Oi, gente!")
                        #(template.render(context, request))