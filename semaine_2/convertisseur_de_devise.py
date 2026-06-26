#==============================================================================================================
# AKIENI ACADEMY -  Projet Sante Publique
# Semaine 2 - Exercice 2 : KPIs Sanitaires OMS
# ===================================================================================================================

# --- DONNEES BRUTES ---

budget_fcfa = 87_450_000
nb_consultation_ext = 4_823
nb_hospitalisation = 1_247
nb_deces = 18 
nb_lits_totals = 180
nb_lit_occupes = 143
nb_medecin = 22
nb_infirmiere = 58
population_dept = 128_000
taux_eur_fcfa   = 655.957
taux_usd_fcfa   = 600.0

# --- A COMPLETER ---
# 1. conversion devises

budget_euro = round(budget_fcfa / taux_eur_fcfa, 2)
budget_usd =  round(budget_fcfa / taux_usd_fcfa, 2)

# 2. Indications OMS
densite_medicale = round((nb_medecin / population_dept )*1000, 1)
taux_mortalite = round((nb_deces / nb_hospitalisation)*100, 1)
taux_occupation = round((nb_lit_occupes / nb_lits_totals )*100, 1)

# 3. Division entiere et modulo
budget_medicaments = round(int(budget_fcfa * 0.35), 1)
cout_journalier_meds = 450_000
jours_stock = budget_medicaments // cout_journalier_meds
jours_restant =  budget_medicaments // cout_journalier_meds
#   mis en pause faute de données

# 4. Puissance pour projection
budget_n_plus_2 = round(budget_fcfa*(1.08**2), 1)


# --- AFFICHAGE RAPPORT ---
print("              ")
print("              ")
print("              ")
print("=== RAPPORT TRIMESTRIEL Q4 2025 - Hopital General Pointe-Noire ===")
print("BUDGET")
print(f'  Depenses Q4        :{budget_fcfa}' )
print(f' En euro             : {budget_euro} EUR')
print(f' En dollars          : {budget_usd} USD')
print("INDICATEURS OMS")
print(f' Densite medicale    : {densite_medicale}  medecins / 1000 hab  [Norme OMS : >=    2.3]')
print(f'  Taux de mortalite  : {taux_mortalite} %                          [Seuil alerte  : > 2%] ')
print(f'  Taux d occupation  : {taux_occupation}%                          [Optimal : 70-85%] ' )
print("ANALYSE PHARMACIE")
print(f'  Budget medicaments :  {budget_medicaments} FCFA')
print(f'  Jour de stock      : {jours_stock} Jours')
print("  Jour depassement    :  0 jours" )
print("PROJECTION")
print(f'  Budget N+2 (8%/ans) : {budget_n_plus_2} FCFA' )
print("ALERTE : Densite medicale CRITIQUE (0.2 pour 1000 hab - norme OMS : 2.3)")
