from django.shortcuts import render, HttpResponseRedirect
from telegram_bot.views import sender


def index(request):
    return render(request, 'website/index.html')


def contact(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    sender(f'Заявка с сайта alixlearn\n{name}\n{phone}')
    return HttpResponseRedirect('/')
