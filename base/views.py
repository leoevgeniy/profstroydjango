from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
# import pywhatkit
from profstroydgango import settings


def index(request):
    return render(request, 'index.html', {})


# Create your views here.

def sendmessage(request):
    name = request.GET.get('name')
    phone = request.GET.get('phone')
    subject = 'Информация о новом запросе на обратный звонок'
    message = f'{name} Просит ему перезвонить по номеру {phone}.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['profstroy73@yandex.ru']
    send_mail(subject, message, email_from, recipient_list)
    print(name, phone, 'done')
    return HttpResponse('sent email')
