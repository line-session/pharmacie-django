# Pharmacie Project Web

Ce projet est une application web basée sur Django pour la gestion d'une pharmacie, permettant aux utilisateurs de rechercher des médicaments, d'effectuer des achats, de demander des conseils et de fournir aux pharmaciens des outils pour gérer les stocks de médicaments, les ventes et les informations sur les pharmaciens.

## Usage
1. Clonez ce dépôt:
   ```bash
   git clone https://github.com/line-session/pharmacie-django.git
   ```
3. Installez les paquets requis
4. Lancez le serveur sur un terminal : `python manage.py runserver`
5. Accédez à l'application dans votre navigateur à l'adresse `http://localhost:8000/`

## Requirements
Installer django
```bash
pip install django
```
Installer django-admin
```bash
sudo apt update
sudo apt install python3-django
```
Installer django-browser-reload et python-dotenv
```bash
pip install django-browser-reload python-dotenv
```
## Principe de Fonctionnement du Projet

### L'Internaute Peut:

- [1] Rechercher un médicament. Ensuite, acheter si l'âge est supérieur ou égal à 18 et le stock suffisant

### Le Client Peut:

- [1] Acheter un médicament.
- [2] Demander des conseils.

### Le Pharmacien Peut :

- [1] Vendre un médicament.
- [2] Visualiser les détails d'un médicament.
- [3] Visualiser tous les médicaments.
- [4] Ajouter un médicament.
- [5] Modifier le stock d'un médicament.
- [6] Supprimer un médicament.
- [7] Afficher le pharmacien.
- [8] Visualiser tous les pharmaciens.
- [9] Ajouter un pharmacien.
- [10] Supprimer un pharmacien.



