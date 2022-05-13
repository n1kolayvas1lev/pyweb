from django.views import View  # Базовый класс.
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


class HelloView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'common/index.html')
