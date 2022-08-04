from ast import Pass
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
import http.client

from inicio.forms import SignoForm


# Create your views here.
def index(request):
    if request.method == "GET":
        form = SignoForm()
        context = {"form": form}
        return render(request, 'index.html', context=context)
    else:
        form = SignoForm(request.POST)

        if form.is_valid():
            form = SignoForm()
            dia, hora = request.POST['day'], request.POST['time']
            signo = achaSigno(dia, hora)
            return HttpRequest('/resultados/')
        else:
            pass

        context = {"form": form}
        return render(request, 'index.html', context=context)


def achaSigno(dia, hora):
    return "Virgo"


def resultados(request):
    conn = http.client.HTTPSConnection("sameer-kumar-aztro-v1.p.rapidapi.com")
    corpo = request.body
    print(corpo)

    headers = {
        'X-RapidAPI-Key': "3e67b48ba7msh2a79c2915744759p16c619jsn41ad5f3571a5",
        'X-RapidAPI-Host': "sameer-kumar-aztro-v1.p.rapidapi.com"
    }

    conn.request("POST", "/?sign=Leo&day=today", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return render(request, 'resultados.html', context={"dados": data})
