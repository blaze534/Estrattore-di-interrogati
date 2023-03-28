#Moduli importati
import random
import tkinter as tk
from tkinter import messagebox
numero = ""
#Apertura File
with open("lista.txt", "r") as f:
    lista = f.read().splitlines()
#Definizione comando    
def estrazione():
    global numero
    numero = random.choice(lista)
    lista.remove(numero)
    with open("lista.txt", "w") as f:
        for item in lista:
            f.write("%s\n" % item)
    messagebox.showinfo("ESTRATTORE INTERROGAZIONI 3C ARTE", "è uscito "+ numero)
#Comando annulla
def annulla():
  global numero
  ultimo_estratto = numero
  lista.append(ultimo_estratto)
  with open("lista.txt", "a") as f:
    f.write(ultimo_estratto + "\n")
  messagebox.showinfo("Annullato",numero+ " riaggiunto alla lista!")
  


#forma gui
root = tk.Tk()
root.title("Estrattore v.1.0")
root.geometry("300x200")


#bottone per estrarre
button = tk.Button(root, text="Clicca per estrarre", comman=estrazione)
button.pack()

#bottone Annulla
undo_button = tk.Button(root, text="Annulla", command=annulla)
undo_button.pack()

label = tk.Label(root, text="Creato con </> da Biagio\n maggiori informazioni qui ")
label.pack()

root.mainloop()
