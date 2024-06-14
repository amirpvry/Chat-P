from django.shortcuts import render
from django.http import HttpResponse
from APPSAMPLE.models import contact
from django.http import HttpResponseRedirect
from .Forms import NameForm , ContactForm 
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.views.generic.edit import CreateView
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import HttpResponse
import json

class AjaxExampleForm(CreateView):
    template_name = ''
    form_class = NameForm

    def form_invalid(self, form):
        if self.request.is_ajax():
            to_json_response = dict()
            to_json_response['status'] = 0
            to_json_response['form_errors'] = form.errors

            to_json_response['new_cptch_key'] = CaptchaStore.generate_key()
            to_json_response['new_cptch_image'] = captcha_image_url(to_json_response['new_cptch_key'])

            return HttpResponse(json.dumps(to_json_response), content_type='application/json')

    def form_valid(self, form):
        form.save()
        if self.request.is_ajax():
            to_json_response = dict()
            to_json_response['status'] = 1

            to_json_response['new_cptch_key'] = CaptchaStore.generate_key()
            to_json_response['new_cptch_image'] = captcha_image_url(to_json_response['new_cptch_key'])

            return HttpResponse(json.dumps(to_json_response), content_type='application/json')



def sample(request):
    return HttpResponse('Hello')

def index(request):
    return render(request,"appsample/index.html")

def about(request):
    return render(request,"appsample/about.html")

def contact_view(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "done")
            else:
                messages.add_message(request, messages.SUCCESS, "kir")

        
        form = ContactForm()

        return render(request,"appsample/contact.html" , {"form": form})

def test(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponse("/thanks/")
        else:
            return HttpResponse("/kir/")
        
    form = ContactForm()

    return render(request,"appsample/test.html" , {"form": form})

from django.shortcuts import render

def magic(request):
    if request.method == 'POST':
        number = request.POST['number']
        try:
            result = int(number) * 10
        except ValueError:
            result = None
        return render(request, 'index.html', {'result': result})
    else:
        return render(request, 'index.html')

# Create your views here.
