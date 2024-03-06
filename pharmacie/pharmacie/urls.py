#
"""pharmacie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from internaute import views as internaute_views
from client import views as client_views
from pharmacien import views as pharmacien_views
from pharmacie import views as core_views

urlpatterns = [
    path("internaute/checkpoint/", internaute_views.checkpoint),
    path("internaute/result/", internaute_views.rechercherMedicament),
    path("internaute/receipt/", internaute_views.generate_receipt),
    path("", core_views.index, name="main"),
    path("authentification", pharmacien_views.tmpauth),
    path("fail", pharmacien_views.fail),
    path("internaute/", internaute_views.index),
    path("client/", client_views.index),
    path("pharmacien/", pharmacien_views.index),
    path("pharmacien/medecines", pharmacien_views.afficherToutMedicament),
    path("pharmacien/pharmaciens", pharmacien_views.AfficherToutPharmacien),
    path("pharmacien/medecine", pharmacien_views.afficherMedicament),
    path("pharmacien/pharmacien", pharmacien_views.VisualiserPharmacien),
    path("pharmacien/tmpMed", pharmacien_views.tamponMed),
    path("pharmacien/tmpPhar", pharmacien_views.tamponPhar),
    path("pharmacien/tmpsell", pharmacien_views.tmpsell),
    path("pharmacien/selling", pharmacien_views.displaysell),
    path('pharmacien/tmpaddmed', pharmacien_views.tmpaddmed),
    path("pharmacien/addmedsuccess", pharmacien_views.displayaddmed),
    path('pharmacien/tmpaddphar', pharmacien_views.tmpaddphar),
    path("pharmacien/addpharsuccess", pharmacien_views.displayaddphar),
    path('pharmacien/tmpdelmed', pharmacien_views.tmpdelmed),
    path("pharmacien/delmedsuccess", pharmacien_views.displaydelmed),
    path('pharmacien/tmpdelphar', pharmacien_views.tmpdelphar),
    path("pharmacien/delpharsuccess", pharmacien_views.displaydelphar),
    path('pharmacien/tmpstock', pharmacien_views.tmpstock),
    path("pharmacien/stocksuccess", pharmacien_views.displaystock),
    path("client/tmpsell", client_views.tmpsell),
    path("client/buying", client_views.buying),
    path("client/asking", client_views.DemanderConseils),
    path("admin/", admin.site.urls),
]
