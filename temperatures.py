import csv
import matplotlib.pyplot as plt

     JOURS = []
     TEMPERATURES = []
     
     
     LECTURE DU FICHIER CSV
     
     def lecture_fichiertemperature(fichier_temperature)
     #fonction permettant de lire le fichier csv contenant les donnees de temperatures
     
     with open('tpt.csv', encoding'utf-8') as fichier 
     reader = csv.reader(fichier)
     
     for ligne in Extraction
     #la boucle for permet de lire chacune des lignes du fichier
     JOURS.append(ligne[0])
     TEMPERATURES.append(ligne[1])
     return JOURS,TEMPERATURES
     except Exception as e:
        print(f"Erreur lors de la lecture du fichier: {e}")
        return [], []
# Si le fichier n'existe pas ou n'est pas accessible, afficher un message d'erreur

CALCULE DE LA SERIE STATISTIQUE (valeur moy et min)

def calculStat(temperatures):
    # Fonction pour calculer la moyenne, le minimum et le maximum des températures
    if not TEMPERATURES:
        return {"moyenne": 0, "min": 0, "max": 0}
    
    # Calculer la moyenne, le minimum et le maximum
    moyenne = sum(TEMPERATURES) / len(TEMPERATURES)
    minimum = min(TEMPERATURES)
    maximum = max(TEMPERATURES)
    
    # Arrondir la moyenne à deux décimales
    return {
        "moyenne": round(moyenne, 2),
        "min": minimum,
        "max": maximum
    }
    
    
    GRAPHE DE TEMPERATURES 
    
    def generer_graphique(jours, temperatures, seuil=30):
    # Fonction pour générer un graphique des températures
    
    plt.figure(figsize=(10, 6))
    
    # Tracer les données de température
    plt.plot(jours, temperatures, marker='o', linestyle='-', color='blue', linewidth=2)
    # Ajouter une ligne pour le seuil critique
    plt.axhline(y=seuil, color='red', linestyle='--', label=f'Seuil critique ({seuil}°C)')
    
    # Ajouter des étiquettes et un titre
    plt.title('Suivi des temperature Eranove', fontsize=16)
    plt.xlabel('Jour', fontsize=12)
    plt.ylabel('Température (°C)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
   
    # Ajustement des étiquettes de l'axe des x pour éviter le chevauchement
    plt.xticks(rotation=45 if len(jours) > 7 else 0)
    
    plt.tight_layout()
    plt.savefig('graphique_temperatures.png')
    plt.show()
    
    
    Programme principale pour generer les autres fonctions du programme , l'affichage de temperqatures , calcules des series statistiques er generer un graphique
    
    # Programme de suivi de température ERANOVE

# l'utilisateur doit entrer le seuil critique de température
print("Bienvenue dans le programme de suivi de température ERANOVE.")
seuil = int(input("Veuillez Entrer le seuil critique de température: "))
    

# Nom du fichier CSV contenant les données de température
# Assurez-vous que le fichier CSV est dans le même répertoire que ce script
fichier_Temp = "temperatures.csv"
        
# Lire les données du fichier CSV
jours, temperatures = lire_fichierTemp(fichier_Temp)
    
        
# Afficher les données lues
print("\n--- DONNÉES DE TEMPÉRATURE ---")
for i in range(len(jours)):
    print(f"{jours[i]}: {temperatures[i]}°C")
        
# Calculer et afficher les statistiques
stats = calculStat(temperatures)
print("\n--- STATISTIQUES ---")
print(f"Température moyenne: {stats['moyenne']}°C")
print(f"Température minimale: {stats['min']}°C")
print(f"Température maximale: {stats['max']}°C")
        
# Détecter et afficher les températures critiques
jours_critiques = TemperatureCritiq(jours, temperatures, seuil)
print("\n--- ALERTES TEMPÉRATURE CRITIQUE ---")
if jours_critiques:
    print(f"Températures dépassant {seuil}°C les jours suivants:")
    for jour, temp in jours_critiques:
        print(f"- {jour}: {temp}°C")
else:
    print(f"Aucune température dépassant {seuil}°C détectée.")
        
# Générer le graphique
print("\nGénération du graphique...")
generer_graphique(jours, temperatures, seuil)
print("Graphique généré et sauvegardé comme 'graphique_temperatures.png'")

Bienvenue dans le programme de suivi de température

--- DONNÉES DE TEMPÉRATURE ---
lundi: 27.0°C
Mardi: 29.0°C
Mercredi: 31.0°C
Jeudi: 28.0°C
Vendredi: 32.0°C

--- STATISTIQUES ---
Température moyenne: 29.4°C
Température minimale: 27.0°C
Température maximale: 32.0°C

--- ALERTES TEMPÉRATURE CRITIQUE ---
Températures dépassant 26°C les jours suivants:
- lundi: 27.0°C
- Mardi: 29.0°C
- Mercredi: 31.0°C
- Jeudi: 28.0°C
- Vendredi: 32.0°C

Génération du graphique...