import tkinter as tk
from tkinter import messagebox
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

# Définition des maladies
maladies = {
    "Grippe": ["fièvre", "toux"],
    "Méningite": ["fièvre", "maux de tête", "raideur"],
    "COVID": ["positif"]
}

# Variables de réponses
questions = {
    "Avez-vous de la fièvre ?": tk.StringVar(value="Non"),
    "Avez-vous de la toux ?": tk.StringVar(value="Non"),
    "Avez-vous des maux de tête ?": tk.StringVar(value="Non"),
    "Avez-vous des raideurs ?": tk.StringVar(value="Non"),
    "Votre test COVID est-il positif ?": tk.StringVar(value="Non")
}

# Section des questions
questions_frame = tk.LabelFrame(fenetre, text="📋 Symptômes", font=("Helvetica", 12, "bold"), fg="blue", padx=10, pady=10)
questions_frame.pack(pady=10, fill="both", expand=True)

row = 0
for question, var in questions.items():
    label = tk.Label(questions_frame, text=question, font=("Helvetica", 11))
    label.grid(row=row, column=0, sticky="w", pady=5)

    # Boutons radio pour "Oui" et "Non"
    radio_oui = tk.Radiobutton(questions_frame, text="Oui", variable=var, value="Oui")
    radio_non = tk.Radiobutton(questions_frame, text="Non", variable=var, value="Non")
    radio_oui.grid(row=row, column=1, padx=10, sticky="w")
    radio_non.grid(row=row, column=2, padx=10, sticky="w")
    
    row += 1

# Fonction de diagnostic
def diagnostiquer():
    symptomes_utilisateur = []
    
    if questions["Avez-vous de la fièvre ?"].get() == "Oui":
        symptomes_utilisateur.append("fièvre")
    if questions["Avez-vous de la toux ?"].get() == "Oui":
        symptomes_utilisateur.append("toux")
    if questions["Avez-vous des maux de tête ?"].get() == "Oui":
        symptomes_utilisateur.append("maux de tête")
    if questions["Avez-vous des raideurs ?"].get() == "Oui":
        symptomes_utilisateur.append("raideur")
    if questions["Votre test COVID est-il positif ?"].get() == "Oui":
        symptomes_utilisateur.append("positif")
        
    maladies_trouvees = []
    for maladie, symptomes in maladies.items():
        if all(symptome in symptomes_utilisateur for symptome in symptomes):
         maladies_trouvees.append(maladie)

    if maladies_trouvees:
        resultat = "🩺 Vous présentez les symptômes des maladies suivantes  :\n"
        resultat += "\n".join(f"- {maladie}" for maladie in maladies_trouvees)
        messagebox.showinfo("Résultat", resultat)
    else:
        messagebox.showinfo("Résultat", "✅ Aucun signe clair d’une maladie parmi celles testées.")

# Bouton Diagnostiquer
diagnostiquer_btn = tk.Button(fenetre, text="Diagnostiquer 🧠", font=("Helvetica", 12, "bold"), fg="blue", command=diagnostiquer)
diagnostiquer_btn.pack(pady=20)



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