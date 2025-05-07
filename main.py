import tkinter as tk

#Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Super-Diagnostiqueur 0107002 🤖 ")
fenetre.geometry("700x500") #Largeur et Hauteur

# Titre
titre_label = tk.Label(
    fenetre,
    text="👋 Bienvenue dans le Super-Diagnostiqueur 🤖",
    font=("Helvetica", 16, "bold"),
    fg="blue"
)
titre_label.pack(pady=12)  # padding vertical

# Instructions
instructions = tk.Label(
    fenetre,
    text="Je vous aide à détecter certaines maladies simples à partir de vos symptômes.\nVeuillez répondre aux questions qui vont suivre.",
    justify="center"
)
instructions.pack(pady=10)

# Variables de réponses
questions = {
    "Avez-vous de la fièvre ?": tk.StringVar(value="Non"),
    "Avez-vous de la toux ?": tk.StringVar(value="Non"),
    "Avez-vous des maux de tête ?": tk.StringVar(value="Non"),
    "Avez-vous des raideurs ?": tk.StringVar(value="Non"),
    "Votre test COVID est-il positif ?": tk.StringVar(value="Non")
}

# Section des questions
questions_frame = tk.LabelFrame(fenetre, text="📋 Symptômes", font=("Helvetica", 12, "bold"), padx=10, pady=10)
questions_frame.pack(pady=10, fill="both", expand=True)

row = 0
for question, var in questions.items():
    label = tk.Label(questions_frame, text=question, font=("Helvetica", 11))
    label.grid(row=row, column=0, sticky="w", pady=5)

    menu = tk.OptionMenu(questions_frame, var, "Oui", "Non")
    menu.config(width=10)
    menu.grid(row=row, column=1, padx=10)
    
    row += 1



# Avertissement
avertissement = tk.Label(
    fenetre,
    text="⚠️ Ce système ne remplace pas un avis médical professionnel.",
    font=("Helvetica", 10, "italic"),
    fg="red"
)
avertissement.pack(side="bottom", pady=20)

# Lancement de l’interface
fenetre.mainloop()


# Message de bienvenue
""""
print("\n                        👋 Bienvenue dans le Super-Diagnostiqueur 🤖        \n")
print("Je vous aide à détecter rapidement certaines maladies simples à partir de vos symptômes. Veuillez répondre aux questions qui vont suivre.")
print("⚠️ Ce système ne remplace pas un avis médical professionnel.\n")

#les maladies
maladies = {
    "Grippe": ["fièvre", "toux"],
    "Méningite": ["fièvre", "maux de tête", "raideur"],
    "COVID": ["positif"]
}
#symptômes utilisateur
symptomes_utilisateur = []

#Les questions
print("Veuillez répondre aux questions suivantes par 'oui' ou 'non' ")

# Vérifier si l'utilisateur a de la fièvre
fievre = input("Avez-vous de la fievre ?\n").strip().lower()
if fievre == "oui":
    symptomes_utilisateur.append("fièvre")

# Vérifier si l'utilisateur a de la toux
toux = input("Avez-vous de la toux ?\n").strip().lower()
if toux == "oui":
    symptomes_utilisateur.append("toux")

# Vérifier si l'utilisateur a des maux de tête
maux_tete = input("Avez-vous des maux de tête ?\n").strip().lower()
if maux_tete == "oui":
    symptomes_utilisateur.append("maux de tête")

# Vérifier si l'utilisateur a des raideurs
raideur = input("Avez-vous des raideurs ?\n").strip().lower()
if raideur == "oui":
    symptomes_utilisateur.append("raideur")

# Vérifier si l'utilisateur est positif au covid
covid = input("Votre test COVID est-il positif ?\n").strip().lower()
if covid == "oui":
    symptomes_utilisateur.append("positif")


# Vérification
maladies_trouvees = []
for maladie, symptomes in maladies.items():
    if all(symptome in symptomes_utilisateur for symptome in symptomes):
        maladies_trouvees.append(maladie)
# Afficher les maladies
if maladies_trouvees:
    print("\n Vous présentez les symptômes des maladies suivantes :")
    for maladie in maladies_trouvees:
        print("-",maladie)
else:
    print("\n Aucun diagnostic possible avec les symptômes fournis.")
"""