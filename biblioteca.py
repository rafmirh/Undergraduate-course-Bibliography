from importlib.metadata import entry_points
import tkinter as tk
from tkinter import* 
from tkinter import messagebox, filedialog, ttk
import pymysql
from openpyxl import *
import pandas as pd


#####Menú principal
def menu_pantalla():
    global pantalla 
    pantalla=tk.Tk()
    pantalla.geometry("400x500")
    pantalla.title("Biblioteca Digital IRC")
    pantalla.iconbitmap("logo.ico")

    image=PhotoImage(file="indice.gif")
    image=image.subsample(2,2)
    label=Label(image=image)
    label.pack()

    Label (text="Acceso al Sistema", bg="medium aquamarine", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(text="").pack()
    Label(text="").pack()

    image2=PhotoImage(file="books.gif")
    image2=image2.subsample(5,5)
    label2=Label(image=image2)
    label2.pack()
    Label(text="").pack()
    Label(text="").pack()

#Botones de inisio de sesion, registro e invitado

    Button(text="Iniciar Sesión", height="2", width="20", command=inicio_sesion).pack()
    Label(text="").pack()

    Button(text="Registrarse", height="2", width="20", command=registrar).pack()
    Label(text="").pack()

    Button(text="Ingresar como invitado", height="2", width="20", command=semestres).pack()
    Label(text="").pack()

    pantalla.mainloop()

#Función de inicio de sesión

def inicio_sesion():
    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de Sesión")
    pantalla1.iconbitmap("logo.ico")

    Label(pantalla1, text="Ingrese su Correo y Contraseña").pack()
    Label(pantalla1, text="").pack()

    global correo_usuario_verify
    global contrasena_usuario_verify

    correo_usuario_verify=StringVar()
    contrasena_usuario_verify=StringVar()

    global correo_usuario_entry
    global contrasena_usuario_entry

    Label(pantalla1, text="Correo").pack()
    correo_usuario_entry = Entry(pantalla1, textvariable=correo_usuario_verify)
    correo_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña (Matrícula)").pack()
    contrasena_usuario_entry = Entry(pantalla1, show="*",textvariable=contrasena_usuario_verify)
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="Iniciar Sesión", command=validacion_datos).pack()

    
#Función de registro de usuario

def registrar():
   
    global pantalla2
    pantalla2 = Toplevel(pantalla)
    pantalla2.geometry("300x385")
    pantalla2.title("Registro")
    pantalla2.iconbitmap("logo.ico")

    global nombres_entry
    global Ap1_entry 
    global Ap2_entry
    global correo_entry
    global contrasena_entry
   
    nombres_entry=StringVar()
    Ap1_entry=StringVar()
    Ap2_entry=StringVar()
    correo_entry=StringVar()
    contrasena_entry=StringVar()

    #Etiquetas y cuadros de texto del formulario

    Label(pantalla2, text="Ingrese sus datos").pack()
    Label(pantalla2, text="").pack()

    Label(pantalla2, text="Nombre(s)").pack()
    nombres_entry = Entry(pantalla2)
    nombres_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Apellido Paterno").pack()
    Ap1_entry = Entry(pantalla2)
    Ap1_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Apellido Materno").pack()
    Ap2_entry = Entry(pantalla2)
    Ap2_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Correo").pack()
    correo_entry = Entry(pantalla2)
    correo_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Matrícula").pack()
    contrasena_entry = Entry(pantalla2)
    contrasena_entry.pack()
    Label(pantalla2).pack()

    Button(pantalla2, text="Registrarse", command=inserta_datos).pack()

def inserta_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="usuarios"
        )
    
    fcursor=bd.cursor()

    sql="INSERT INTO login (correo, contrasena, nombre, Ap1, Ap2) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(correo_entry.get(), contrasena_entry.get(), nombres_entry.get(), Ap1_entry.get(), Ap2_entry.get())

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")

    except:
        bd.rollback()
        messagebox.showinfo(message="No Registrado", title="Aviso")

    bd.close()

def validacion_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="usuarios"
        )

    fcursor=bd.cursor()

    fcursor.execute("SELECT contrasena FROM login WHERE correo='"+correo_usuario_verify.get()+"' and contrasena='"+contrasena_usuario_verify.get()+"'")

    if fcursor.fetchall():
        messagebox.showinfo(title="Inicio de sesión correcto", message="Usuario y contraseña correctos")
        

    else:
        messagebox.showinfo(title="Inicio de sesión incorrecto", message="Usuario y contraseña incorrectos")

    bd.close()

def menu_perfil():
    global perfil
    perfil=tk.Tk()
    perfil.geometry("400x500")
    perfil.title("Biblioteca Digital IRC")
    perfil.iconbitmap("logo.ico")

    #Botones de perfil

    Button(perfil, text="Favoritos", height="2", width="20").pack()
    Label(perfil, text="").pack()

    Button(perfil, text="Historial", height="2", width="20").pack()
    Label(perfil, text="").pack()

    Button(perfil, text="Acceso a Catálogo Digital", height="2", width="20").pack()
    Label(perfil, text="").pack()

def semestres():
    global msemestres 
    msemestres=tk.Tk()
    msemestres.geometry("400x550")
    msemestres.title("Semestres")
    msemestres.iconbitmap("logo.ico")

    Label(msemestres, text="Elija el semestre a consultar").pack()
    Label(msemestres, text="").pack()

#Botones de catálogo por semestres

    Button(msemestres, text="Primer Semestre", height="2", width="15", command=semestre1).pack()
    Label(msemestres, text="").pack()

    Button(msemestres, text="Segundo Semestre", height="2", width="15", command=semestre2).pack()
    Label(msemestres, text="").pack()
   
    Button(msemestres, text="Tercer Semestre", height="2", width="15", command=semestre3).pack()
    Label(msemestres, text="").pack()

    Button(msemestres, text="Cuarto Semestre", height="2", width="15", command=semestre4).pack()
    Label(msemestres, text="").pack()
   
    Button(msemestres, text="Quinto Semestre", height="2", width="15", command=semestre5).pack()
    Label(msemestres, text="").pack()

    Button(msemestres, text="Sexto Semestre", height="2", width="15", command=semestre6).pack()
    Label(msemestres, text="").pack()
   
    Button(msemestres, text="Séptimo Semestre", height="2", width="15", command=semestre7).pack()
    Label(msemestres, text="").pack()

    Button(msemestres, text="Octavo Semestre", height="2", width="15", command=semestre8).pack()
    Label(msemestres, text="").pack()

    #msemestres.mainloop()

    #semestres()

    #Treeview widget

def semestre1():
    global sem1 
    sem1=tk.Tk()
    sem1.geometry("400x500")
    sem1.title("Bibliografía Primer Semestre")
    sem1.iconbitmap("logo.ico")

    tvs1 = ttk.Treeview(sem1)
    tvs1.place(relheight=1, relwidth=1)

    treescrolly = tk.Scrollbar(sem1, orient="vertical", command=tvs1.yview)
    treescrollx = tk.Scrollbar(sem1, orient="horizontal", command=tvs1.xview)
    tvs1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom",fill="x")
    treescrolly.pack(side="right",fill="y")

    catsem1 = pd.read_excel ('LibrosLCDA.xlsx', sheet_name='Primero')

    tvs1["column"] = list(catsem1.columns)
    tvs1["show"] = "headings"
    for column in tvs1["columns"]:
        tvs1.heading(column, text=column)
    
    catsem1_rows = catsem1.to_numpy().tolist()
    for row in catsem1_rows:
        tvs1.insert("", "end", values=row)
    
    return None

def semestre2():
    global sem2 
    sem2=tk.Tk()
    sem2.geometry("400x500")
    sem2.title("Bibliografía Segundo Semestre")
    sem2.iconbitmap("logo.ico")

    tvs2 = ttk.Treeview(sem2)
    tvs2.place(relheight=1, relwidth=1)

    treescrolly = tk.Scrollbar(sem2, orient="vertical", command=tvs2.yview)
    treescrollx = tk.Scrollbar(sem2, orient="horizontal", command=tvs2.xview)
    tvs2.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom",fill="x")
    treescrolly.pack(side="right",fill="y")

    catsem2 = pd.read_excel ('LibrosLCDA.xlsx', sheet_name='Segundo')

    tvs2["column"] = list(catsem2.columns)
    tvs2["show"] = "headings"
    for column in tvs2["columns"]:
        tvs2.heading(column, text=column)
    
    catsem2_rows = catsem2.to_numpy().tolist()
    for row in catsem2_rows:
        tvs2.insert("", "end", values=row)
    
    return None

def semestre3():
    global sem3 
    sem3=tk.Tk()
    sem3.geometry("400x500")
    sem3.title("Bibliografía Tercer Semestre")
    sem3.iconbitmap("logo.ico")

    tvs3 = ttk.Treeview(sem3)
    tvs3.place(relheight=1, relwidth=1)

    treescrolly = tk.Scrollbar(sem3, orient="vertical", command=tvs3.yview)
    treescrollx = tk.Scrollbar(sem3, orient="horizontal", command=tvs3.xview)
    tvs3.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom",fill="x")
    treescrolly.pack(side="right",fill="y")

    catsem3 = pd.read_excel ('LibrosLCDA.xlsx', sheet_name='Tercero')

    tvs3["column"] = list(catsem3.columns)
    tvs3["show"] = "headings"
    for column in tvs3["columns"]:
        tvs3.heading(column, text=column)
    
    catsem3_rows = catsem3.to_numpy().tolist()
    for row in catsem3_rows:
        tvs3.insert("", "end", values=row)
    
    return None

def semestre4():
    global sem4 
    sem4=tk.Tk()
    sem4.geometry("400x500")
    sem4.title("Bibliografía Cuarto Semestre")
    sem4.iconbitmap("logo.ico")

    tvs4 = ttk.Treeview(sem4)
    tvs4.place(relheight=1, relwidth=1)

    treescrolly = tk.Scrollbar(sem4, orient="vertical", command=tvs4.yview)
    treescrollx = tk.Scrollbar(sem4, orient="horizontal", command=tvs4.xview)
    tvs4.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom",fill="x")
    treescrolly.pack(side="right",fill="y")

    catsem4 = pd.read_excel ('LibrosLCDA.xlsx', sheet_name='Cuarto')

    tvs4["column"] = list(catsem4.columns)
    tvs4["show"] = "headings"
    for column in tvs4["columns"]:
        tvs4.heading(column, text=column)
    
    catsem4_rows = catsem4.to_numpy().tolist()
    for row in catsem4_rows:
        tvs4.insert("", "end", values=row)
    
    return None
    
def semestre5():
    global sem5 
    sem5=tk.Tk()
    sem5.geometry("400x500")
    sem5.title("Bibliografía Quinto Semestre")
    sem5.iconbitmap("logo.ico")

    tvs5 = ttk.Treeview(sem5)
    tvs5.place(relheight=1, relwidth=1)

    treescrolly = tk.Scrollbar(sem5, orient="vertical", command=tvs5.yview)
    treescrollx = tk.Scrollbar(sem5, orient="horizontal", command=tvs5.xview)
    tvs5.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom",fill="x")
    treescrolly.pack(side="right",fill="y")

    catsem5 = pd.read_excel ('LibrosLCDA.xlsx', sheet_name='Quinto')

    tvs5["column"] = list(catsem5.columns)
    tvs5["show"] = "headings"
    for column in tvs5["columns"]:
        tvs5.heading(column, text=column)
    
    catsem5_rows = catsem5.to_numpy().tolist()
    for row in catsem5_rows:
        tvs5.insert("", "end", values=row)
    
    return None

def semestre6():
    global sem6 
    sem6=tk.Tk()
    sem6.geometry("400x500")
    sem6.title("Bibliografía Sexto Semestre")
    sem6.iconbitmap("logo.ico")

    tvs6 = ttk.Treeview(sem6)
    tvs6.place(relheight=1, relwidth=1)

    treescrolly = tk.Scrollbar(sem6, orient="vertical", command=tvs6.yview)
    treescrollx = tk.Scrollbar(sem6, orient="horizontal", command=tvs6.xview)
    tvs6.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom",fill="x")
    treescrolly.pack(side="right",fill="y")

    catsem6 = pd.read_excel ('LibrosLCDA.xlsx', sheet_name='Sexto')

    tvs6["column"] = list(catsem6.columns)
    tvs6["show"] = "headings"
    for column in tvs6["columns"]:
        tvs6.heading(column, text=column)
    
    catsem6_rows = catsem6.to_numpy().tolist()
    for row in catsem6_rows:
        tvs6.insert("", "end", values=row)
    
    return None

def semestre7():
    global sem7 
    sem7=tk.Tk()
    sem7.geometry("400x500")
    sem7.title("Bibliografía Séptimo Semestre")
    sem7.iconbitmap("logo.ico")

    tvs7 = ttk.Treeview(sem7)
    tvs7.place(relheight=1, relwidth=1)

    treescrolly = tk.Scrollbar(sem7, orient="vertical", command=tvs7.yview)
    treescrollx = tk.Scrollbar(sem7, orient="horizontal", command=tvs7.xview)
    tvs7.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom",fill="x")
    treescrolly.pack(side="right",fill="y")

    catsem7 = pd.read_excel ('LibrosLCDA.xlsx', sheet_name='Septimo')

    tvs7["column"] = list(catsem7.columns)
    tvs7["show"] = "headings"
    for column in tvs7["columns"]:
        tvs7.heading(column, text=column)
    
    catsem7_rows = catsem7.to_numpy().tolist()
    for row in catsem7_rows:
        tvs7.insert("", "end", values=row)
    
    return None

def semestre8():
    global sem8 
    sem8=tk.Tk()
    sem8.geometry("400x500")
    sem8.title("Bibliografía Octavo Semestre")
    sem8.iconbitmap("logo.ico")

    tvs8 = ttk.Treeview(sem8)
    tvs8.place(relheight=1, relwidth=1)

    treescrolly = tk.Scrollbar(sem8, orient="vertical", command=tvs8.yview)
    treescrollx = tk.Scrollbar(sem8, orient="horizontal", command=tvs8.xview)
    tvs8.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom",fill="x")
    treescrolly.pack(side="right",fill="y")

    catsem8 = pd.read_excel ('LibrosLCDA.xlsx', sheet_name='Octavo')

    tvs8["column"] = list(catsem8.columns)
    tvs8["show"] = "headings"
    for column in tvs8["columns"]:
        tvs8.heading(column, text=column)
    
    catsem8_rows = catsem8.to_numpy().tolist()
    for row in catsem8_rows:
        tvs8.insert("", "end", values=row)

    
    return None

menu_pantalla()








