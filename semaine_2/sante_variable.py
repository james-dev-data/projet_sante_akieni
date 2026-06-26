# ========================================================================================================================
# AKIENI ACADEMY - Project Sante Publique
# Semaine 2 - Exercice 1 : Fiche Patient CHU Brazzaville
# Nom : IVANGUI
# Date : 23 juin 2026
# ========================================================================================================================


# declaration de variable de la section 1 : patient identité

nom_patient = 'MAVOUNGUO Celestine'
age_patient = 42
sexe_patient = 'F'
departement_patient = 'Brazzaville'
couverture_sociale = 'CNSS'

# section 2: variable consultation

type_consultation = 'Urgence'
cout_consultation_FCFA = 15000.0
nb_consultations = 1
remise_cnss_pct = 30.0
diagnostic_principal = 'Paludisme grave'

#secion,3: variable hopital
nom_hopital = 'CHU de Brazzaville'
ville_hopital = 'Brazzaville'
nombre_lits_totals = 320
nombre_lits_occupes = 284
nombre_de_medecin_actifs = 47

# section 4: calcul cout_total_fcfa

cout_total_fcfa = cout_consultation_FCFA*nb_consultations*(1 -remise_cnss_pct/100 )

# section 5: calcul du taux_occupation_pct

taux_occupation_pct = round(nombre_lits_occupes/nombre_lits_totals*100, 1)

# section 6: calcul du ratio_consultation_medecin
nb_consultations_hopital = 120
ratio_consultation_medecin = round(nb_consultations_hopital/nombre_de_medecin_actifs, 1)


# construction de l'affiche

print("====================================================================================")
print(f'FICHE PATIENT -  {nom_patient}')
print("====================================================================================")

print(f'    Age               : {age_patient} ans')
print(f'    Sexe              : {sexe_patient}')
print(f'    Departement       : {departement_patient}')
print(f'    Couverture        : {couverture_sociale}')
print("-------------------------------------------------------------------------------------")
print("CONSULTATION")
print(f'     Type             : {type_consultation}')
print(f'    Diagnostic        : {diagnostic_principal}')
print(f'    Cout unitaire     :{cout_consultation_FCFA} FCFA')
print(f'    Remise CNSS       : {remise_cnss_pct} %' )
print(f'    COUT TOTAL        : {cout_total_fcfa} FCFA')
print("-------------------------------------------------------------------------------------")
print(f'    HOPITAL           : {nom_hopital}')
print(f'    Ville             : {ville_hopital}')
print(f'    Lits occupé       : {nombre_lits_occupes} ( / 320 (88.8%))')
print(f'    Medecins actifs   : {nombre_de_medecin_actifs}')
print(f'    Ratio consult.    :{ratio_consultation_medecin}  consultation /  medecin ce matin' )
print("====================================================================================")
print("STATUT : Prise en charge validee")
print("====================================================================================")