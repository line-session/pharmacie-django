from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from SharedDB.models import *
from pharmacien import views

# Create your views here.
@csrf_exempt
def index(request):
    return render(request, "internaute.html")

@csrf_exempt
def rechercherMedicament(request):
    if request.method == "POST":
        data = request.POST.get('medicament')
        result = medicament.objects.filter(nom__icontains=data).first()
        if result:
            return render(request, "result.html", {'result': result})
        else:
            return render(request, "NOTresult.html")

    return redirect("/")

@csrf_exempt
def checkpoint(request):
    if(request.method == "POST"):
        nom_medicament = request.POST.get('nom_medicament')
        prix_medicament = request.POST.get('prix_medicament')
        
        if(int(prix_medicament)<0):
            return redirect("/fail")
        else:
            if(nom_medicament and prix_medicament):
                return render(request, "status.html", {'nom_medicament': nom_medicament , 'prix_medicament': prix_medicament})
            else:
                return redirect("/internaute")
        
    return redirect("/internaute")

@csrf_exempt
def generate_receipt(request):
    if request.method == "POST":
        data = request.POST.get('nom_medicament')
        prix = request.POST.get('prix_medicament')
        prenom_acheteur = request.POST.get('prenom_acheteur')
        nom_acheteur = request.POST.get('nom_acheteur')
        quantite = request.POST.get('quantite')
        age = request.POST.get('age')
        if(int(age) <18):
            return redirect("/fail")
        if(int(quantite) < 0):
            return redirect("/fail")
        else:
            result = medicament.objects.filter(nom=data).first()
            total = int(quantite) * int(prix)
            stock = result.stockDisponible
            verifier = stock - int(quantite)
            if(verifier < 0):
                return render(request, "stockfail.html")
            
            views.sell(request, str(data), int(quantite))
            if result:
                return render(request, 'receipt.html', {'medicament': data, 'prenom_acheteur': prenom_acheteur, 'nom_acheteur': nom_acheteur, 'quantite': quantite, 'total': total})
            else:
                if request.path.endswith('/'):
                    return redirect("/internaute/checkpoint")
                else:
                    return redirect(request.path + "/")
    
    return redirect("/")
            

            
