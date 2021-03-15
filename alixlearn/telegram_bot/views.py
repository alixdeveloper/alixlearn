from django.shortcuts import render
import telebot
from django.conf import settings
from django.views import View
from telebot import TeleBot, types, logger
from django.http import HttpResponse
import json
from django.utils import timezone
import datetime


bot = telebot.TeleBot(settings.NOTIFICATION_TOKEN)


class UpdateBot(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Бот запущен и работает.")

    def post(self, request, *args, **kwargs):
        json_str = request.body.decode('UTF-8')
        update = types.Update.de_json(json_str)
        bot.process_new_updates([update])

        return HttpResponse({'code': 200})


def sender(text):
    bot.send_message(999205203, text=text)

