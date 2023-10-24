import tkinter as tk

# Cette fonction est appelée lorsque l'utilisateur clique sur le bouton "Inscrire".
def inscription():
    pseudo = pseudo_entry.get()  # Récupère le contenu du champ "Pseudo"
    mdp = mdp_entry.get()        # Récupère le contenu du champ "Mot de passe"
    email = email_entry.get()    # Récupère le contenu du champ "Email"
    
    # Affiche les données dans la console
    print(f"Pseudo: {pseudo}")
    print(f"Mot de passe: {mdp}")
    print(f"Email: {email}")

# Crée une fenêtre Tkinter
app = tk.Tk()
app.title("Inscription")  # Définit le titre de la fenêtre

# Crée des libellés (labels) pour chaque champ
label_pseudo = tk.Label(app, text="Pseudo:")
label_pseudo.pack()  # Affiche le libellé dans la fenêtre
pseudo_entry = tk.Entry(app)  # Crée un champ de texte pour le pseudo
pseudo_entry.pack()  # Affiche le champ de texte dans la fenêtre

label_mdp = tk.Label(app, text="Mot de passe:")
label_mdp.pack()
mdp_entry = tk.Entry(app, show="*")  # Crée un champ de texte pour le mot de passe (affiche * pour chaque caractère)
mdp_entry.pack()

label_email = tk.Label(app, text="Email:")
label_email.pack()
email_entry = tk.Entry(app)  # Crée un champ de texte pour l'email
email_entry.pack()

# Crée un bouton "Inscrire" qui appelle la fonction "inscription" lorsque cliqué
inscription_button = tk.Button(app, text="Inscrire", command=inscription)
inscription_button.pack()

# Démarre la boucle principale de Tkinter pour afficher la fenêtre
app.mainloop()
