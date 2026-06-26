# ==========================================================================================
# MODULE FONDATEUR - Projet Sante Publique / Akieni Academy
# Ce fichier centralise toutes les constantes et variables metiert
# Il sera enrichi chaque semaine jusqu'a S24
# ==========================================================================================

# =============== SECTION A: CONSTANTES NATIONES ET NORMES OMS =============================
TAUX_EUR_FCFA = 655.957
TAUX_USD_FCFA = 600.0
SEUIL_OMS_DENSITE_MEDICALE = 2.3    # medecins pour 1000 habitants
SEUIL_OMS_COUVERTURE_VACCIN = 95.0  # pourcentage minimum OMS
SEUIL_MORTALITE_ALERTE = 2.0        # % deces / hospitalisations
SEUIL_RUPTURE_STOCK_JOURS = 30      # jours minimum de stock
DEPARTEMENT_CONGO = [               # 12 departements officiels
    'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette', 
    'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala', 
    'Niari', 'Plateaux', 'Pool', 'Sangha'
]


# =============== SECTION B: VARIABLES DES 5 HOPITAUX ======================================

# Hopital 1 - CHU de Brazzaville

h1_nom              = 'CHU de Brazzaville'
h1_ville            = 'Brazzaville'
h1_departement      = 'Brazzaville'
h1_type             = 'CHU'
h1_nb_lits          = 320
h1_nb_lits_occupes  = 284
h1_nb_medecins      = 47
h1_nb_infirmiers    = 123
h1_population_zone  = 1_800_000

# Hopital 2 - Hopital General de Pointe-Noire

h2_nom              = 'HG de Pointe-Noire'
h2_ville            = 'Pointe-noire'
h2_departement      = 'Pointe-Noire'
h2_type             = 'hopital General'
h2_nb_lits          = 116
h2_nb_lits_occupes  = 93
h2_nb_medecins      = 21
h2_nb_infirmiers    = 67
h2_population_zone  = 69_990



# Hopital 3 - Hopital de DOLISIE

h3_nom              = 'Hopital de Dolisie'
h3_ville            = 'DOLISIE'
h3_departement      = 'Niari'
h3_type             = 'Hopital'
h3_nb_lits          = 123
h3_nb_lits_occupes  = 67
h3_nb_medecins      = 47
h3_nb_infirmiers    = 77
h3_population_zone  = 55_737

# Hopital 4 - Hopital du discrict d_Owando 

h4_nom              = 'Hopital d_Owando'
h4_ville            = 'Owando'
h4_departement      = 'Cuvette'
h4_type             = 'HOPITAL GENERAL'
h4_nb_lits          = 147
h4_nb_lits_occupes  = 47
h4_nb_medecins      = 13
h4_nb_infirmiers    = 66
h4_population_zone  = 12_437

# Hopital 5 - Centre de sante de Impfondo

h5_nom              = 'hopital d_impfondo'
h5_ville            = 'impfondo'
h5_departement      = 'LIKOUALA'
h5_type             = 'HOPITAL GENERALE'
h5_nb_lits          = 143
h5_nb_lits_occupes  = 47
h5_nb_medecins      = 13
h5_nb_infirmiers    = 88
h5_population_zone  = 23_783

# =============== SECTION C : VARIABLES DES 5 MEDICAMENTS ======================================

# Declaration des variables des 5 MEDICAMENTS ESSENTIELS
# Medicament 1 artemether-lumefantrine
med1 = "artemether-lumefantrine"
med1_quantite_disponible = 1500
med1_seuil_rupture = 300
med1_cout_unitaire = 150.0

# medicament 2 - amoxicilline
med2 = "Amoxicilline"
med2_quantite_disponible = 3200
med2_seuil_rupture = 500
med2_cout_unitaire = 150.0

# medicament 3 - paracetamol
med3 = "Paracetamol"
med3_quantite_disponible = 5000
med3_seuil_rupture = 800
med3_cout_unitaire = 50.0

# medicament 4 - SRO
med4 = "SRO"
med4_quantite_disponible = 800
med4_seuil_rupture = 200
med4_cout_unitaire = 300.0

med5 = "vaccin antipaludeen"
med5_quantite_disponible = 400
med5_seuil_rupture = 100
med5_cout_unitaire = 15000.0


# ================= SELECTION D : CALCULD D'INITIALISATION ========================================

# Densite medicale nationale (moyenne des 5 hopitaux)
total_medecins = h1_nb_medecins + h2_nb_medecins + h3_nb_medecins + h4_nb_medecins + h5_nb_medecins
total_population = h1_population_zone + h2_population_zone + h3_population_zone + h4_population_zone + h5_population_zone
densite_medicale_nationale = round(total_medecins / total_population * 1000, 2)

# Taux d'occupation moyen
taux_occ_h1 = h1_nb_lits_occupes / h1_nb_lits * 100
taux_occ_h2 = h2_nb_lits_occupes / h2_nb_lits * 100
taux_occ_h3 = h3_nb_lits_occupes / h3_nb_lits * 100
taux_occ_h4 = h4_nb_lits_occupes / h4_nb_lits * 100
taux_occ_h5 = h5_nb_lits_occupes / h5_nb_lits * 100
taux_occupation_moyen = round((taux_occ_h1 + taux_occ_h2 + taux_occ_h3 + taux_occ_h4 + taux_occ_h5) / 5, 2)

# Valeur totale du stock de medicaments
valeur_stock = (
    med1_quantite_disponible * med1_cout_unitaire +
    med2_quantite_disponible * med2_cout_unitaire +
    med3_quantite_disponible * med3_cout_unitaire +
    med4_quantite_disponible * med4_cout_unitaire +
    med5_quantite_disponible * med5_cout_unitaire
)

# ============================ section E : Rapport d'inventaire =================================


print('=' * 65)
print('   RAPPORT D\'INVENTAIRE — SYSTEME DE SANTE CONGO-BRAZZAVILLE')
print('=' * 65)

print('\n  KPIs GLOBAUX')
print(f'  Densite medicale nationale : {densite_medicale_nationale} medecins / 1000 hab')
print(f'  Norme OMS                  : {SEUIL_OMS_DENSITE_MEDICALE} medecins / 1000 hab')
print(f'  Taux occupation moyen      : {taux_occupation_moyen}%')

print('\n' + '-' * 65)
print('  HOPITAUX')
print('-' * 65)
print(f'  1. {h1_nom} — {h1_nb_lits} lits — {h1_nb_medecins} medecins')
print(f'  2. {h2_nom} — {h2_nb_lits} lits — {h2_nb_medecins} medecins')
print(f'  3. {h3_nom} — {h3_nb_lits} lits — {h3_nb_medecins} medecins')
print(f'  4. {h4_nom} — {h4_nb_lits} lits — {h4_nb_medecins} medecins')
print(f'  5. {h5_nom} — {h5_nb_lits} lits — {h5_nb_medecins} medecins')

print('\n' + '-' * 65)
print('  STOCK MEDICAMENTS')
print('-' * 65)
print(f'  1. {h1_nom} — {med1_quantite_disponible} unites — {med1_cout_unitaire} FCFA/unite')
print(f'  2. {h2_nom} — {med2_quantite_disponible} unites — {med2_cout_unitaire} FCFA/unite')
print(f'  3. {h3_nom} — {med3_quantite_disponible} unites — {med3_cout_unitaire} FCFA/unite')
print(f'  4. {h4_nom} — {med4_quantite_disponible} unites — {med4_cout_unitaire} FCFA/unite')
print(f'  5. {h5_nom} — {med5_quantite_disponible} unites — {med5_cout_unitaire} FCFA/unite')
print(f'\n  Valeur totale du stock : {valeur_stock:,.0f} FCFA')

print('\n' + '=' * 65)
print('  STATUT : Rapport genere avec succes')
print('=====================================================================================')