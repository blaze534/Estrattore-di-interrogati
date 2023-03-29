# Moduli importati
import random
import tkinter as tk
from tkinter import messagebox

numero = ""
# Apertura File
with open("lista.txt", "r") as f:
    lista = f.read().splitlines()


def print_input():
    print(input_field.get())


def aggiungi_elemento():
    global numero
    if numero != "":
        with open("lista.txt", "a") as f:
            f.write(numero + "\n")
    root.destroy()

# Definizione comando
def estrazione():
    global numero
    numero = random.choice(lista)
    lista.remove(numero)
    with open("lista.txt", "w") as f:
        for item in lista:
            f.write("%s\n" % item)
    messagebox.showinfo("ESTRATTORE INTERROGAZIONI 3C ARTE", "è uscito " + numero)


# Comando annulla
def annulla():
    global numero
    ultimo_estratto = numero
    lista.append(ultimo_estratto)
    with open("lista.txt", "a") as f:
        f.write(ultimo_estratto + "\n")
    messagebox.showinfo("Annullato", numero + " riaggiunto alla lista!")


def elimina_elemento():
    global numero
    numero = input_field.get()
    if numero in lista:
        lista.remove(numero)
        with open("lista.txt", "w") as f:
            for item in lista:
                f.write("%s\n" % item)
        messagebox.showinfo("Eliminato", numero + " rimosso dalla lista!")
        input_field.delete(0, 'end')
    else:
        messagebox.showerror("ERRORE", "Elemento non presente nella lista!")


# forma gui
root = tk.Tk()
root.title("Estrattore v.1.0")
root.geometry("300x200")

# bottone per estrarre
button = tk.Button(root, text="Clicca per estrarre", command=estrazione)
button.pack()

# bottone Annulla
undo_button = tk.Button(root, text="Annulla", command=annulla)
undo_button.pack()
label = tk.Label(root, text="Metti gli Assenti ")
label.pack()
input_field = tk.Entry(root)
input_field.pack()

delete_button = tk.Button(root, text="Elimina gli assenti", command=elimina_elemento)
delete_button.pack()

label = tk.Label(root, text="Creato con </> da Biagio ")
label.pack()

root.protocol("WM_DELETE_WINDOW", aggiungi_elemento)
root.mainloop()
