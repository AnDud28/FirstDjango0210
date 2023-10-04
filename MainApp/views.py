from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "index.html")

def about(request):
    text = """<p> Имя: <b>Анастасия</b><br>
               Отчество: <b>Александровна</b><br>
               Фамилия: <b>Дудченко</b><br>
               телефон: <b>8-923-600-03-03</b><br>
               email: <b>andud@mail.ru</b></p>
    """

    return HttpResponse(text)