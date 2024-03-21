from django.shortcuts import render, redirect
from SharedDB.models import medicament, pharmacien
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if((username == "root") and (password == "admin")):
            return redirect("/pharmacien")
        else:
            return redirect("/fail")
    return render(request, "pharmacien.html")

@csrf_exempt
def tmpauth(request):
    return render(request, "authentification.html")

def fail(request):
    return render(request, "fail.html")

@csrf_exempt
def afficherMedicament(request):
    if request.method == "POST":
        nom_medicament = request.POST.get('medicament')
        result = medicament.objects.filter(nom__icontains=nom_medicament).first()

        if(result):
            return render(request, "ResultAfficherMedicament.html", {'medicament': result})
        else:
            return render(request, "NotResultAfficherMedicament.html")

    return render(request, "AfficherMedicament.html")

@csrf_exempt
def afficherToutMedicament(request):
        all_medicaments = medicament.objects.all()

        if all_medicaments:
            return render(request, "allmedecines.html", {'all_medicaments': all_medicaments})
        else:
            return render(request, "NotResultAfficherMedicament.html")

@csrf_exempt
def AfficherToutPharmacien(request):
    all_pharmaciens = pharmacien.objects.all()
    if all_pharmaciens:
        return render(request, "allpharmaciens.html", {'all_pharmaciens': all_pharmaciens})
    else:
        return render(request, "NotResultAfficherPharmacien.html")

@csrf_exempt
def VisualiserPharmacien(request):
    if request.method == "POST":
        pharmacien_nom = request.POST.get('pharmacien')
        prenom_pharmacien = pharmacien.objects.filter(prenom__icontains=pharmacien_nom).first()

        if(prenom_pharmacien):
            return render(request, "ResultAfficherPharmacien.html", {'pharmacien': prenom_pharmacien})
        else:
            return render(request, "NotResultAfficherPharmacien.html")
        
    return render(request, "AfficherPharmacien.html")

@csrf_exempt
def tamponMed(request):
    return render(request, "tamponMed.html")

@csrf_exempt
def tamponPhar(request):
    return render(request, "tamponPhar.html")

@csrf_exempt
def SupprimerPharmacien(request):
    if(request.method == "POST"):

        nom_pharmacien = request.POST.get('pharmacien')
        result = pharmacien.object.filter(nom=nom_pharmacien).delete()

        if(result):
            return render(request, "ResultSuppressionPharmacien.html")
        else:
            return render(request, "NotResutlSuppressionPharmacien.html")
    return render(request, "SuppressionPharmacien.html")

@csrf_exempt
def supprimerMedicament(request):
    if request.method == "POST":

        nom_medicament = request.POST.get('medicament')
        result = medicament.objects.filter(nom=nom_medicament).delete()
        
        if(result):
            return render(request, "SuppresionMedicament.html")  
        else:
            return render(request, "NotSuppresionMedicament.html")
        
    return render(request, "SuppresionMedicament.html")

@csrf_exempt
def tmpsell(request):
    return render(request, "tmpSell.html")

@csrf_exempt
def displaysell(request):
    if request.method == "POST":
        amount = request.POST.get('quantite')
        nom_medicament = request.POST.get('medicament')
        result = sell(request, nom_medicament, amount)
        if result==True:
            return render(request, "ResultatVente.html", {'medicament': nom_medicament, 'quantite':amount})
        else:
            return render(request, "NotResultatVente.html")
    return redirect("/pharmacien")
    
@csrf_exempt
def sell(request, nom_medicament, amount):
    if(int (amount) < 0):
        return redirect("/fail")
    else:
        object = medicament.objects.filter(nom__icontains=nom_medicament).first()
        stockActuel = object.stockDisponible
        if stockActuel >= 0:
            new_stock = stockActuel - int(amount)
            object.stockDisponible = new_stock
            object.save()
            return True
        else:
            return render(request, "NOTresult.html")
    
@csrf_exempt
def changeStock(request, nom_medicament, amount):
    if request.method == "POST":
        if(int (amount) < 0):
            return redirect("/fail")
        else:
            object = medicament.objects.filter(nom__icontains=nom_medicament).first()

            if object:
                stockActuel = object.stockDisponible
                new_stock = stockActuel + int(amount)
                object.stockDisponible = new_stock
                object.save()
                return True
            else:
                return render(request, "stockfail.html")
    return redirect("/internaute")
    
@csrf_exempt
def tmpaddmed(request):
    return render(request, "tmpaddmed.html")

@csrf_exempt
def displayaddmed(request):
    if request.method == "POST":
        Vnom = request.POST.get('nom')
        Vcode = request.POST.get('code')
        Vprix = request.POST.get('prix')
        Vdescription = request.POST.get('description')
        VdateExpiration = request.POST.get('dateExpiration')
        VstockDisponible = request.POST.get('stockDisponible')
        if(int (VstockDisponible) <0 ):
            return redirect("/fail")
        else:
            new_med = medicament.objects.create(
                nom=Vnom,
                code = Vcode,
                prix = Vprix,
                description = Vdescription,
                dateExpiration = VdateExpiration,
                stockDisponible = VstockDisponible)

            if new_med:
                return render(request, "ResultAjouterMedicament.html", {'medicament': new_med})
    return redirect("/pharmacien")

@csrf_exempt
def tmpaddphar(request):
    return render(request, "tmpaddphar.html")

@csrf_exempt
def displayaddphar(request):
    if request.method == "POST":
        Vprenom = request.POST.get('prenom')
        Vnom = request.POST.get('nom')
        Vsexe = request.POST.get('sexe')
        Vaddress = request.POST.get('address')
        Vsalaire = request.POST.get('salaire')
        if (int(Vsalaire) <0):
            return redirect("/fail")
        else:
            new_phar = pharmacien.objects.create(
                nom=Vnom,
                prenom = Vprenom,
                address = Vaddress,
                sexe = Vsexe,
                salaire = Vsalaire)
                
            if new_phar:
                return render(request, "ResultAjouterPharmacien.html", {'pharmacien': new_phar})
    return redirect("/pharmacien")

@csrf_exempt
def tmpdelphar(request):
    return render(request, "tmpdelphar.html")

@csrf_exempt
def displaydelphar(request):
    if request.method == "POST":
        Vprenom = request.POST.get('prenom_pharmacien')
        Vnom = request.POST.get('nom_pharmacien')
        result = pharmacien.objects.filter(prenom__icontains=Vprenom, nom__icontains=Vnom).delete()
        
        if result:
            return render(request, "ResultSuppressionPharmacien.html")
    return redirect("/pharmacien")

@csrf_exempt
def tmpdelmed(request):
    return render(request, "tmpdelmed.html")

@csrf_exempt
def displaydelmed(request):
    if request.method == "POST":
        nom_medicament = request.POST.get('medicament')
        result = medicament.objects.filter(nom__icontains=nom_medicament).delete()
        
        if result:
            return render(request, "ResultSuppressionMedicament.html")
    return redirect("/pharmacien")

@csrf_exempt
def tmpstock(request):
    return render(request, "tmpstock.html")

@csrf_exempt
def displaystock(request):
    if request.method == "POST":
        amount = request.POST.get('quantite')
        if int(amount) <= 0:
            return render(request, "stockfail.html")

        nom_medicament = request.POST.get('medicament')
        result = changeStock(request, nom_medicament, amount)
        if result==True:
            return render(request, "stocksuccess.html", {'medicament': nom_medicament, 'quantite':amount})
        else:
            return render(request, "stockfail.html")
    return redirect("/pharmacien")



