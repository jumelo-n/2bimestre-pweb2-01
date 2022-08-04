from ast import Pass
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
            return HttpResponseRedirect('resultados/')
        else:
            pass

        context = {"form": form}
        return render(request, 'index.html', context=context)


def resultados(request, dados):
    conn = http.client.HTTPSConnection("sameer-kumar-aztro-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "3e67b48ba7msh2a79c2915744759p16c619jsn41ad5f3571a5",
        'X-RapidAPI-Host': "sameer-kumar-aztro-v1.p.rapidapi.com"
    }

    conn.request("POST", "/?sign=Leo&day=today", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return render(request, 'resultados.html', context={"dados": data})
