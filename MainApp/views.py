from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    text = """<h1>Изучаем django"</h1>
              <strong>Автор</strong>: <i>Дудченко А.А.</i>
    """

    return HttpResponse(text)

def about(request):
    text = """<p> Имя: <b>Анастасия</b><br>
               Отчество: <b>Александровна</b><br>
               Фамилия: <b>Дудченко</b><br>
               телефон: <b>8-923-600-03-03</b><br>
               email: <b>andud@mail.ru</b></p>
    """

    return HttpResponse(text)