from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def name1(request):
    return HttpResponse('Hello name1!!!!')


def name2(request):
    return HttpResponse('<h1>Hello name2 whatsapp!!!!!</h1>')


def name3(request):
    return HttpResponse('''<div><h1>Hello name3</h1></div>
                        <div><h1>Name3 Age is 22</h1></div>
                        <div><h1>MY favourite is name3</h1></div>''')