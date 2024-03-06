from django.core.management.base import BaseCommand
import django
from ...models import *

class Command(BaseCommand):
    help = "Pour ajouter plusieur object dans la base de donnees de DJANGO"

    def handle(self, *args, **options):

        medicament_Data = [
            medicament(nom='Paracetamol', code='PARA001', stockDisponible=100, description='Pain reliever and fever reducer', dateExpiration='2024-06-01', prix=500),
            medicament(nom='Amoxicillin', code='AMOX002', stockDisponible=500, description='Antibiotic used to treat various bacterial infections', dateExpiration='2024-08-15', prix=300),
            medicament(nom='Lisinopril', code='LISI003', stockDisponible=2000, description='Angiotensin-converting enzyme (ACE) inhibitor used to treat high blood pressure and heart failure', dateExpiration='2024-07-20', prix=200),
            medicament(nom='Simvastatin', code='SIMV004', stockDisponible=550,description='Lipid-lowering medication used to reduce the risk of heart disease and stroke', dateExpiration='2024-09-30', prix=400),
            medicament(nom='Omeprazole', code='OMEP005', stockDisponible=1540, description='Proton pump inhibitor used to reduce stomach acid and treat gastroesophageal reflux disease (GERD)', dateExpiration='2024-08-10', prix=600),
            medicament(nom='Atorvastatin', code='ATOR006', stockDisponible=1250, description='Lipid-lowering medication used to treat high cholesterol and reduce the risk of heart attack and stroke', dateExpiration='2024-10-05', prix=350),
            medicament(nom='Metformin', code='METF007', stockDisponible=1870,  description='Oral diabetes medicine used to control blood sugar levels in people with type 2 diabetes', dateExpiration='2024-07-15', prix=450),
            medicament(nom='Losartan', code='LOSA008', stockDisponible=1450, description='Angiotensin II receptor blocker (ARB) used to treat high blood pressure and heart failure', dateExpiration='2024-09-25', prix=250),
            medicament(nom='Albuterol', code='ALBU009', stockDisponible=1500, description='Bronchodilator used to treat bronchospasm and symptoms of asthma and chronic obstructive pulmonary disease (COPD)', dateExpiration='2024-08-30', prix=150),
            medicament(nom='Warfarin', code='WARF010', stockDisponible=1802, description='Anticoagulant used to treat and prevent blood clots in veins and arteries', dateExpiration='2024-09-15', prix=100),
            medicament(nom='Ibuprofen', code='IBUP011', stockDisponible=1100, description='Nonsteroidal anti-inflammatory drug (NSAID) used to treat pain, fever, and inflammation', dateExpiration='2024-07-05', prix=700),
            medicament(nom='Ciprofloxacin', code='CIPR012', stockDisponible=1152, description='Antibiotic used to treat various bacterial infections', dateExpiration='2024-08-20', prix=250),
            medicament(nom='Amlodipine', code='AMLO013', stockDisponible=1900, description='Calcium channel blocker used to treat high blood pressure and coronary artery disease', dateExpiration='2024-09-10', prix=300),
            medicament(nom='Metoprolol', code='METO014', stockDisponible=1402, description='Beta blocker used to treat high blood pressure, chest pain, and heart failure', dateExpiration='2024-10-15', prix=400),
            medicament(nom='Hydrochlorothiazide', code='HYDR015', stockDisponible=1540, description='Diuretic used to treat high blood pressure and fluid retention', dateExpiration='2024-06-30', prix=200),
            medicament(nom='Prednisone', code='PRED016', stockDisponible=1500, description='Corticosteroid used to treat allergic disorders, skin conditions, arthritis, and more', dateExpiration='2024-08-25', prix=600),
            medicament(nom='Levothyroxine', code='LEVO017', stockDisponible=500,description='Thyroid hormone replacement used to treat hypothyroidism', dateExpiration='2024-07-15', prix=350),
            medicament(nom='Metronidazole', code='METR018', stockDisponible=1500, description='Antibiotic and antiprotozoal medication used to treat bacterial and parasitic infections', dateExpiration='2024-09-05', prix=450),
            medicament(nom='Fluoxetine', code='FLUO019', stockDisponible=1550, description='Selective serotonin reuptake inhibitor (SSRI) used to treat depression, panic disorder, and other mental health conditions', dateExpiration='2024-10-20', prix=150),
            medicament(nom='Doxycycline', code='DOXY020', stockDisponible=5200, description='Antibiotic used to treat bacterial infections, including acne and malaria', dateExpiration='2024-07-10', prix=500),
            medicament(nom='Loratadine', code='LORA021', stockDisponible=5400, description='Antihistamine used to treat allergy symptoms such as sneezing, runny nose, and itching', dateExpiration='2024-08-01', prix=350),
            medicament(nom='Tramadol', code='TRAM022', stockDisponible=5050, description='Opioid analgesic used to treat moderate to severe pain', dateExpiration='2024-09-30', prix=250),
            medicament(nom='Gabapentin', code='GABA023', stockDisponible=5210, description='Anticonvulsant and neuropathic pain medication used to treat epilepsy and nerve pain', dateExpiration='2024-06-15', prix=400),
            medicament(nom='Cephalexin', code='CEPH024', stockDisponible=5770, description='Antibiotic used to treat bacterial infections, including respiratory tract infections and skin infections', dateExpiration='2024-07-25', prix=300),
            medicament(nom='Metformin', code='METF025', stockDisponible=1450, description='Oral diabetes medicine used to control blood sugar levels in people with type 2 diabetes', dateExpiration='2024-08-15', prix=450),
            medicament(nom='Trazodone', code='TRAZ026', stockDisponible=500,description='Serotonin antagonist and reuptake inhibitor (SARI) antidepressant used to treat depression and anxiety disorders', dateExpiration='2024-10-10', prix=200),
            medicament(nom='Furosemide', code='FURO027', stockDisponible=5020, description='Loop diuretic used to treat fluid retention (edema) and high blood pressure', dateExpiration='2024-06-20', prix=550),
            medicament(nom='Alprazolam', code='ALPR028', stockDisponible=5001, description='Benzodiazepine anxiolytic used to treat anxiety and panic disorders', dateExpiration='2024-09-01', prix=300),
            medicament(nom='Azithromycin', code='AZIT029', stockDisponible=4520, description='Antibiotic used to treat a wide variety of bacterial infections', dateExpiration='2024-07-30', prix=400),
            medicament(nom='Citalopram', code='CITA030', stockDisponible=1450, description='Selective serotonin reuptake inhibitor (SSRI) antidepressant used to treat depression and anxiety disorders', dateExpiration='2024-08-05', prix=350),
            medicament(nom='Acetaminophen', code='ACET031', stockDisponible=500,description='Pain reliever and fever reducer commonly used for headaches, muscle aches, and arthritis', dateExpiration='2024-07-15', prix=800),
            medicament(nom='Clarithromycin', code='CLAR032', stockDisponible=4500, description='Antibiotic used to treat bacterial infections such as pneumonia, bronchitis, and sinusitis', dateExpiration='2024-08-20', prix=350),
            medicament(nom='Bupropion', code='BUPR033', stockDisponible=6500, description='Atypical antidepressant used to treat depression and aid in smoking cessation', dateExpiration='2024-09-10', prix=400),
            medicament(nom='Rosuvastatin', code='ROSU034', stockDisponible=7500, description='Statins medication used to lower cholesterol and reduce the risk of heart disease and stroke', dateExpiration='2024-10-15', prix=200),
            medicament(nom='Prednisolone', code='PRED035', stockDisponible=5500, description='Corticosteroid medication used to treat a variety of conditions including inflammation, allergies, and autoimmune diseases', dateExpiration='2024-06-30', prix=600),
            medicament(nom='Sildenafil', code='SILD036', stockDisponible=8500, description='Phosphodiesterase type 5 (PDE5) inhibitor used to treat erectile dysfunction and pulmonary arterial hypertension', dateExpiration='2024-08-25', prix=450),
            medicament(nom='Escitalopram', code='ESCI037', stockDisponible=9500, description='Selective serotonin reuptake inhibitor (SSRI) antidepressant used to treat depression and anxiety disorders', dateExpiration='2024-07-15', prix=300),
            medicament(nom='Fexofenadine', code='FEXO038', stockDisponible=5500, description='Second-generation antihistamine used to relieve allergy symptoms such as sneezing, itching, and runny nose', dateExpiration='2024-09-05', prix=500),
            medicament(nom='Venlafaxine', code='VENL039', stockDisponible=5000, description='Serotonin-norepinephrine reuptake inhibitor (SNRI) antidepressant used to treat depression and anxiety disorders', dateExpiration='2024-10-20', prix=350),
            medicament(nom='Levofloxacin', code='LEVO040', stockDisponible=1452, description='Fluoroquinolone antibiotic used to treat bacterial infections of the skin, sinuses, kidneys, bladder, and prostate', dateExpiration='2024-07-10', prix=250),
            medicament(nom='Metronidazole', code='METR041', stockDisponible=1450, description='Antibiotic and antiprotozoal medication used to treat bacterial and parasitic infections', dateExpiration='2024-08-01', prix=400),
            medicament(nom='Naproxen', code='NAPR042', stockDisponible=1450, description='Nonsteroidal anti-inflammatory drug (NSAID) used to relieve pain, swelling, and stiffness caused by arthritis, gout, and other conditions', dateExpiration='2024-09-30', prix=450),
            medicament(nom='Montelukast', code='MONTE043', stockDisponible=4500, description='Leukotriene receptor antagonist used to prevent asthma and to treat seasonal allergies', dateExpiration='2024-06-15', prix=200),
            medicament(nom='Pantoprazole', code='PANT044', stockDisponible=7500, description='Proton pump inhibitor (PPI) used to treat erosive esophagitis and other conditions involving excess stomach acid production', dateExpiration='2024-07-25', prix=300),
            medicament(nom='Budesonide', code='BUDE045', stockDisponible=4500, description='Corticosteroid medication used to treat asthma, COPD, inflammatory bowel disease (IBD), and nasal polyps', dateExpiration='2024-08-15', prix=550),
            medicament(nom='Duloxetine', code='DULO046', stockDisponible=5300, description='Serotonin-norepinephrine reuptake inhibitor (SNRI) antidepressant used to treat depression, anxiety, and nerve pain', dateExpiration='2024-10-10', prix=300),
            medicament(nom='Esomeprazole', code='ESOM047', stockDisponible=7850, description='Proton pump inhibitor (PPI) used to treat gastroesophageal reflux disease (GERD) and other conditions involving excess stomach acid production', dateExpiration='2024-06-20', prix=400),
            medicament(nom='Fluconazole', code='FLUC048', stockDisponible=1450, description='Antifungal medication used to treat infections caused by fungus, including yeast infections of the mouth, throat, esophagus, and other organs', dateExpiration='2024-09-01', prix=350),
            medicament(nom='Lisinopril', code='LISI049', stockDisponible=1550, description='Angiotensin-converting enzyme (ACE) inhibitor used to treat high blood pressure, heart failure, and to improve survival after heart attack', dateExpiration='2024-07-30', prix=250),
            medicament(nom='Tadalafil', code='TADA050', stockDisponible=4150, description='Phosphodiesterase type 5 (PDE5) inhibitor used to treat erectile dysfunction (impotence) and symptoms of benign prostatic hyperplasia (enlarged prostate)', dateExpiration='2024-08-05', prix=400)
            ]
        medicament.objects.bulk_create(medicament_Data)

        pharmacien_Data = [
            pharmacien(nom="SOW", prenom="Ousmane", sexe="M", address="Parcelles Assainies U17", salaire=500000),
            pharmacien(nom="LO", prenom="Ibrahim", sexe="M", address="Parcelles Assainies U26", salaire=500000),
            pharmacien(nom="SEYE", prenom="Libasse", sexe="M", address="SOPRIM", salaire=500000),
            pharmacien(nom="SALL", prenom="Moumamed Madeniyou", sexe="M", address="Thies", salaire=500000),
        ]
        pharmacien.objects.bulk_create(pharmacien_Data)

        acheteurData  = [
            acheteur(nom="NDIAYE", prenom="Moussa", age=19, CIN="1852451356457"),
            acheteur(nom="DIOP", prenom="Fallou", age=19, CIN="1854265335245"),
        ]
        acheteur.objects.bulk_create(acheteurData)
