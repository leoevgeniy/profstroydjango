from django.shortcuts import render
import pywhatkit


def index(request):
    return render(request, 'index.html', {})


# Create your views here.

def sendmessage(request):
    print(request)
    pywhatkit.sendwhatmsg('+7XXXXXXXXXX', 'Привет мир!', 18, 40)
