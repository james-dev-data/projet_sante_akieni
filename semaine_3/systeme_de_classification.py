# ==========================================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Exercice 1 : Classification Stocks Medicaments
# Utilise les notions de S2 (variables, types, operateurs, f-strings)
# S3 (if/elif/else, conditions composees)
# ==========================================================================

# Medicament 1 artemether-lumefantrine
med1_nom = "artemether-lumefantrine"
med1_quantite_disponible = 1500
med1_seuil_rupture = 300
med1_cout_unitaire = 150.0

med2_nom = "Amoxicilline"
med2_quantite_disponible = 3200
med2_seuil_rupture = 500
med2_cout_unitaire = 150.0

med3_nom = "Paracetamol"
med3_quantite_disponible = 5000
med3_seuil_rupture = 800
med3_cout_unitaire = 50.0

med4_nom = "SRO"
med4_quantite_disponible = 800
med4_seuil_rupture = 200
med4_cout_unitaire = 300.0

med5_nom = "vaccin antipaludeen"
med5_quantite_disponible = 400
med5_seuil_rupture = 100
med5_cout_unitaire = 15000.0

# CLASSIFICATION 1
if med1_quantite_disponible <= med1_seuil_rupture:
    med1_statut  = 'RUPTURE CRITIQUE'
    med1_couleur = '[ROUGE]'
    med1_action  = 'Alerte immediate PNA — commande express sous 24h'
elif med1_quantite_disponible <= med1_seuil_rupture * 1.5:
    med1_statut  = 'ALERTE STOCK'
    med1_couleur = '[ORANGE]'
    med1_action  = 'Commande urgente a declencher'
elif med1_quantite_disponible <= med1_seuil_rupture * 2.0:
    med1_statut  = 'STOCK ALERTE'
    med1_couleur = '[JAUNE]'
    med1_action  = 'Surveillance renforcee'
else:
    med1_statut  = 'STOCK NORMAL'
    med1_couleur = '[VERT]'
    med1_action  = 'Surveillance renforcee - planifier commande'

# CLASSIFICATION 2
if med2_quantite_disponible <= med2_seuil_rupture:
    med2_statut  = 'RUPTURE CRITIQUE'
    med2_couleur = '[ROUGE]'
    med2_action  = 'Alerte immediate PNA — commande express sous 24h'
elif med2_quantite_disponible <= med2_seuil_rupture * 1.5:
    med2_statut  = 'ALERTE STOCK'
    med2_couleur = '[ORANGE]'
    med2_action  = 'Commande urgente a declencher'
elif med2_quantite_disponible <= med2_seuil_rupture * 2.0:
    med2_statut  = 'STOCK ALERTE'
    med2_couleur = '[JAUNE]'
    med2_action  = 'Surveillance renforcee'
else:
    med2_statut  = 'STOCK NORMAL'
    med2_couleur = '[VERT]'
    med2_action  = 'Surveillance renforcee - planifier commande'

# CLASSIFICATION 3
if med3_quantite_disponible <= med3_seuil_rupture:
    med3_statut  = 'RUPTURE CRITIQUE'
    med3_couleur = '[ROUGE]'
    med3_action  = 'Alerte immediate PNA — commande express sous 24h'
elif med3_quantite_disponible <= med3_seuil_rupture * 1.5:
    med3_statut  = 'ALERTE STOCK'
    med3_couleur = '[ORANGE]'
    med3_action  = 'Commande urgente a declencher'
elif med3_quantite_disponible <= med3_seuil_rupture * 2.0:
    med3_statut  = 'STOCK ALERTE'
    med3_couleur = '[JAUNE]'
    med3_action  = 'Surveillance renforcee'
else:
    med3_statut  = 'STOCK NORMAL'
    med3_couleur = '[VERT]'
    med3_action  = 'Surveillance renforcee - planifier commande'

# CLASSIFICATION 4
if med4_quantite_disponible <= med4_seuil_rupture:
    med4_statut  = 'RUPTURE CRITIQUE'
    med4_couleur = '[ROUGE]'
    med4_action  = 'Alerte immediate PNA — commande express sous 24h'
elif med4_quantite_disponible <= med4_seuil_rupture * 1.5:
    med4_statut  = 'ALERTE STOCK'
    med4_couleur = '[ORANGE]'
    med4_action  = 'Commande urgente a declencher'
elif med4_quantite_disponible <= med4_seuil_rupture * 2.0:
    med4_statut  = 'STOCK ALERTE'
    med4_couleur = '[JAUNE]'
    med4_action  = 'Surveillance renforcee'
else:
    med4_statut  = 'STOCK NORMAL'
    med4_couleur = '[VERT]'
    med4_action  = 'Surveillance renforcee - planifier commande'

# CLASSIFICATION 5
if med5_quantite_disponible <= med5_seuil_rupture:
    med5_statut  = 'RUPTURE CRITIQUE'
    med5_couleur = '[ROUGE]'
    med5_action  = 'Alerte immediate PNA — commande express sous 24h'
elif med5_quantite_disponible <= med5_seuil_rupture * 1.5:
    med5_statut  = 'ALERTE STOCK'
    med5_couleur = '[ORANGE]'
    med5_action  = 'Commande urgente a declencher'
elif med5_quantite_disponible <= med5_seuil_rupture * 2.0:
    med5_statut  = 'STOCK ALERTE'
    med5_couleur = '[JAUNE]'
    med5_action  = 'Surveillance renforcee'
else:
    med5_statut  = 'STOCK NORMAL'
    med5_couleur = '[VERT]'
    med5_action  = 'Situation normale - suivi standard'

# COMPTAGE
nb_ruptures_critiques = 0
nb_alertes_stock = 0
nb_stocks_normaux = 0

if med1_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques += 1
elif med1_statut == 'ALERTE STOCK':
    nb_alertes_stock += 1
else:
     nb_stocks_normaux += 1

# AFFICHAGE

print('=================================================================================')
print(' RAPPORT DE STOCK — PHARMACIE NATIONALE D APPROVISIONNEMENT')
print(' Date : 15 janvier 2026')

print('==================================================================================')

print(f' {med1_couleur} {med1_nom}')
print(f' Stock : {med1_quantite_disponible} unites | Seuil rupture : {med1_seuil_rupture}')
print(f' Statut : {med1_statut}')
print(f' Action : {med1_action}')

print('--------------------------------------------------------------------------------------------------------')

print(f' {med2_couleur} {med2_nom}')
print(f' Stock : {med2_quantite_disponible} unites | Seuil rupture : {med2_seuil_rupture}')
print(f' Statut : {med2_statut}')
print(f' Action : {med2_action}')
print('--------------------------------------------------------------------------------------------------------')

print(f' {med3_couleur} {med3_nom}')
print(f' Stock : {med3_quantite_disponible} unites | Seuil rupture : {med3_seuil_rupture}')
print(f' Statut : {med3_statut}')
print(f' Action : {med3_action}')

print('========================================================================================================')

print(f' {med4_couleur} {med4_nom}')
print(f' Stock : {med4_quantite_disponible} unites | Seuil rupture : {med4_seuil_rupture}')
print(f' Statut : {med4_statut}')
print(f' Action : {med4_action}')

print('========================================================================================================')

print(f' {med5_couleur} {med5_nom}')
print(f' Stock : {med5_quantite_disponible} unites | Seuil rupture : {med5_seuil_rupture}')
print(f' Statut : {med5_statut}')
print(f' Action : {med5_action}')
print('=' * 65)

print(' BILAN STOCK — PNA CONGO')
print(f' Ruptures critiques : {nb_ruptures_critiques}')
print(f' Alertes stock      : {nb_alertes_stock}')
print(f' Stocks normaux     : {nb_stocks_normaux}')

print('========================================================================================================')

if nb_ruptures_critiques > 0:
    print(f' !! ALERTE PRIORITAIRE : {nb_ruptures_critiques} medicaments en RUPTURE CRITIQUE !!')
    print(' Transmettre immediatement au Dr. MOUKALA (PNA)')

print('========================================================================================================')