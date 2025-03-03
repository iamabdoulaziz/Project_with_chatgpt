import random
import tkinter as tk

# Constantes
MAX_VIES = 3
MAX_NOMBRE = 20

# Générer un nombre aléatoire entre 1 et MAX_NOMBRE
def generer_nombre():
    return random.randint(1, MAX_NOMBRE)

# Fonction pour vérifier la tentative
def verifier(choix):
    global vies, nombre_magique
    if choix < 1 or choix > MAX_NOMBRE:
        lbl_message.config(text="Veuillez entrer un nombre entre 1 et 10.")
    elif choix < nombre_magique:
        vies -= 1
        lbl_vies.config(text=f"Vies restantes : {vies}")
        lbl_message.config(text="Trop petit ! Essayez encore.")
    elif choix > nombre_magique:
        vies -= 1
        lbl_vies.config(text=f"Vies restantes : {vies}")
        lbl_message.config(text="Trop grand ! Essayez encore.")
    else:
        lbl_message.config(text="Bravo ! Vous avez trouvé le nombre magique 🎉.")
        disable_buttons()  # Désactiver les boutons après la victoire

    # Vérifier si le joueur a épuisé ses vies
    if vies == 0:
        lbl_message.config(text=f"Dommage ! Le nombre magique était {nombre_magique}.")
        disable_buttons()  # Désactiver les boutons après la défaite

# Fonction pour désactiver tous les boutons après la fin du jeu
def disable_buttons():
    for btn in buttons:
        btn.config(state="disabled")

# Fonction pour relancer le jeu
def relancer_jeu():
    global vies, nombre_magique
    vies = MAX_VIES
    nombre_magique = generer_nombre()
    lbl_vies.config(text=f"Vies restantes : {MAX_VIES}")
    lbl_message.config(text="")
    # Réactiver les boutons et remettre tous les boutons à leur état normal
    for btn in buttons:
        btn.config(state="normal", relief="raised")

# Fonction pour griser un bouton après un clic
def griser_bouton(btn):
    btn.config(state="disabled", relief="sunken")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Jeu du Nombre Magique")

# Widgets
lbl_instruction = tk.Label(root, text="Devinez le nombre entre 1 et 10", font=("Arial", 12))
lbl_instruction.pack(pady=10)

lbl_vies = tk.Label(root, text=f"Vies restantes : {MAX_VIES}", font=("Arial", 12))
lbl_vies.pack(pady=5)

lbl_message = tk.Label(root, text="", font=("Arial", 12))
lbl_message.pack(pady=10)

# Créer les boutons pour chaque choix de nombre (1 à MAX_NOMBRE)
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

buttons = []
for i in range(1, MAX_NOMBRE + 1):
    btn = tk.Button(buttons_frame, text=str(i), command=lambda i=i: [verifier(i), griser_bouton(i)], font=("Arial", 12), width=4)
    btn.grid(row=(i-1)//5, column=(i-1)%5, padx=5, pady=5)  # Disposition sur plusieurs lignes
    buttons.append(btn)

# Bouton de relance
btn_relancer = tk.Button(root, text="Relancer le jeu", command=relancer_jeu, font=("Arial", 12))
btn_relancer.pack(pady=10)

# Initialisation du jeu
vies = MAX_VIES
nombre_magique = generer_nombre()

# Lancer l'application
root.mainloop()
