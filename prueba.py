from importlib.metadata import entry_points
import tkinter as tk
from tkinter import* 
from openpyxl import*
from tkinter import filedialog, messagebox, ttk
import pandas as pd
from biblioteca import semestres

def menu_perfil():
    global perfil
    perfil=Tk()
    perfil.geometry("400x250")
    perfil.title("Mi Perfil - Biblioteca Digital IRC")
    perfil.iconbitmap("logo.ico")

    #Botones de perfil

    Label(perfil, text="").pack()
    Label(perfil, text="").pack()

    Button(perfil, text="Favoritos", height="2", width="20").pack()
    Label(perfil, text="").pack()

    Button(perfil, text="Historial", height="2", width="20").pack()
    Label(perfil, text="").pack()

    Button(perfil, text="Acceso a Catálogo Digital", height="2", width="20", command=semestres).pack()
    Label(perfil, text="").pack()

    perfil.mainloop()

menu_perfil()


