from datetime import datetime
from random import random

from django.shortcuts import render
from django.views import View  # Базовый класс.
from django.http import HttpRequest, HttpResponse


class DateTimeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        now = datetime.now()
        return HttpResponse(now)


class RandomNumberView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        rand_num = random()
        return HttpResponse(rand_num)
