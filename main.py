#Moduli importati
import random
import tkinter as tk
from tkinter import messagebox
#Apertura File
with open("lista.txt", "r") as f:
  lista = f.read().splitlines()


#Definizione comando
def estrazione():
  numero = random.choice(lista)
  lista.remove(numero)
  with open("lista.txt", "w") as f:
    for item in lista:
      f.write("%s\n" % item)
  messagebox.showinfo("Estratto", "è uscito " + numero)


#forma gui
root = tk.Tk()
root.title("Finestra")
root.geometry("700x500")

#bottone per estrarre
button = tk.Button(root, text="Clicca per estrarre", comman=estrazione)
button.pack()

root.mainloop()
