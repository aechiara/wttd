# coding: utf-8
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.views.generic import CreateView, DetailView


class SubscriptionCreate(CreateView):
    model = Subscription
    form_class = SubscriptionForm

class SubscriptionDetail(DetailView):
    model = Subscription

# ajax
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

def validate_cpf(request):
    if request.is_ajax():
        cpf = request.GET.get('cpf')
        from .forms import cpf_checksum
        if cpf_checksum(cpf):
            return HttpResponse("Success")
        else:
            return HttpResponse("Fail")

    return HttpResponse("Fail")

