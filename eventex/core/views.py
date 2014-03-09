# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Speaker, Talk
from django.views.generic import TemplateView, DetailView

# Create your views here.
#def home(request):
    #return render(request, 'index.html')

class HomeView(TemplateView):
    template_name = "index.html"

#def speaker_detail(request, slug):
#    speaker = get_object_or_404(Speaker, slug=slug)
#    context = {'speaker': speaker }
#    return render(request, 'core/speaker_detail.html', context)

class SpeakerDetail(DetailView):
    model = Speaker


def talk_list(request):
    context = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(),
    }
    return render(request, 'core/talk_list.html', context)

#def talk_detail(request, pk):
    #talk = get_object_or_404(Talk, pk=pk)
    #context = {
        #'talk': talk,
    #}
#
    #return render(request, 'core/talk_detail.html', context)

class TalkDetail(DetailView):
    model = Talk
