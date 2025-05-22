def saisir_note(matiere):
    while True:
        try:
            note = float(input(f"Entrez la note en {matiere} (sur 20) : "))
            if 0 <= note <= 20:
                return note
            else:
                print("Erreur : La note doit être entre 0 et 20.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")

def calculer_mention(moyenne):
    if moyenne >= 16:
        return "Très bien"
    elif moyenne >= 14:
        return "Bien"
    elif moyenne >= 12:
        return "Assez bien"
    elif moyenne >= 10:
        return "Passable"
    else:
        return "Ajourné"

# --- Saisie des données ---
print("=== Gestion des Notes d’un Étudiant ===")
nom = input("Nom de l’étudiant : ")
prenom = input("Prénom de l’étudiant : ")

matieres = ["Français", "Anglais", "Physique", "Mathématiques", "Sport"]
notes = {}

for matiere in matieres:
    notes[matiere] = saisir_note(matiere)

# --- Calcul de la moyenne ---
moyenne = sum(notes.values()) / len(notes)

# --- Affichage du bulletin ---
print("\n=== Bulletin de Notes ===")
print(f"Étudiant : {prenom} {nom}")
for matiere, note in notes.items():
    print(f"{matiere} : {note}/20")

print(f"\nMoyenne générale : {moyenne:.2f}/20")
print(f"Mention : {calculer_mention(moyenne)}")