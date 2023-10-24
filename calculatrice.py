import tkinter as tk

# Fonction pour effectuer une addition
def addition(n1, n2):
    return n1 + n2

# Fonction pour effectuer une soustraction
def soustraction(n1, n2):
    return n1 - n2

# Fonction pour effectuer une multiplication
def multiplication(n1, n2):
    return n1 * n2

# Fonction pour effectuer une division
def division(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Erreur : Division par zéro"

# Fonction pour effectuer le calcul en fonction du choix de l'utilisateur
def calculer():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_choice.get()

    if operation == "Addition":
        result = addition(num1, num2)
    elif operation == "Soustraction":
        result = soustraction(num1, num2)
    elif operation == "Multiplication":
        result = multiplication(num1, num2)
    elif operation == "Division":
        result = division(num1, num2)
    else:
        result = "Opération non valide"

    result_label.config(text=f"Résultat : {result}")

# Créer la fenêtre principale
app = tk.Tk()
app.title("Calculatrice")

# Créer des libellés pour les nombres et le résultat
label_num1 = tk.Label(app, text="Nombre 1:")
label_num1.pack()
entry_num1 = tk.Entry(app)
entry_num1.pack()

label_num2 = tk.Label(app, text="Nombre 2:")
label_num2.pack()
entry_num2 = tk.Entry(app)
entry_num2.pack()

# Créer une liste déroulante pour choisir l'opération
operation_choice = tk.StringVar()
operation_choice.set("Addition")
operations = ["Addition", "Soustraction", "Multiplication", "Division"]
operation_menu = tk.OptionMenu(app, operation_choice, *operations)
operation_menu.pack()

# Créer un bouton pour effectuer le calcul
calculate_button = tk.Button(app, text="Calculer", command=calculer)
calculate_button.pack()

# Créer un libellé pour afficher le résultat
result_label = tk.Label(app, text="Résultat :")
result_label.pack()

# Démarrer la boucle principale de Tkinter
app.mainloop()
