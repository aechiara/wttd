# coding: utf-8
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

def subscribe(request):
    if request.method == "POST":
        return create(request)
    else:
        return new(request)

def new(request):
    return render(request, 'subscriptions/subscription_form.html',
            {'form': SubscriptionForm()})

def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html',
                {'form': form})
    
    obj = form.save()
    return HttpResponseRedirect('/inscricao/%d/' % obj.pk)

def detail(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscription})

def get_emails(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        emails = Subscription.objects.filter(email__startswith=q)[:10]
        results = []
        for e in emails:
            email_json = {}
            email_json['id'] = e.id
            email_json['label'] = e.email
            email_json['value'] = e.email
            results.append(email_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    
    print data
    return HttpResponse(data, 'application/json')
