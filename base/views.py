from django.shortcuts import render
import pywhatkit


def index(request):
    return render(request, 'index.html', {})


# Create your views here.

def sendmessage(request):
    print('1231243',request)
    pywhatkit.sendwhatmsg('+79673767234', 'Привет мир!')
    return 'done'
