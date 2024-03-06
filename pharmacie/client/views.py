from django.shortcuts import redirect, render
from SharedDB.models import medicament
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "client.html")

def DemanderConseils(request):
    return render(request, "DemanderConseils.html")


def tmpsell(request):
    return render(request, "tmpsell.html")


def buying(request):
    if request.method == "POST":
        nom_medicament = request.POST.get('medicament')
        quantite = request.POST.get('quantite')

        if(int(quantite) < 0):
            return render(request, "sellfail.html")
        else:
            result = medicament.objects.filter(nom__icontains = nom_medicament).first()
            if result:
                stock = result.stockDisponible
                verif = stock - int(quantite)
                if (verif < 0):
                    return render(request, "stockissue.html")
                else:
                    result.stockDisponible = verif
                    return render(request, "buysuccess.html", {'medicament': result, 'quantite':quantite})
            else:
                return render(request, "medicamentIssue.html")
    return redirect("/client")
