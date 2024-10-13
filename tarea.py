import tkinter as tk
from tkinter import ttk 
from ttkthemes import ThemedTk
from tkinter import PhotoImage
from tkinter import messagebox
import math
import time
import pygame
from time import sleep

# Función para calcular el área según la figura seleccionada
def mostrar_campos_figura(event):
    figura = combo.get()
    # Limpia los campos anteriores
    limpiar_campos()
    
    if figura == "Cuadrado":
        label_1.config(text="Lado:")
        label_1.pack(pady=5)
        entry_1.pack(pady=5)
        boton_area.pack(pady=10)

    elif figura == "Rectángulo":
        label_1.config(text="Base:")
        label_2.config(text="Altura:")
        label_1.pack(pady=5)
        entry_1.pack(pady=5)
        label_2.pack(pady=5)
        entry_2.pack(pady=5)
        boton_area.pack(pady=10)

    elif figura == "Triángulo":
        label_1.config(text="Base:")
        label_2.config(text="Altura:")
        label_1.pack(pady=5)
        entry_1.pack(pady=5)
        label_2.pack(pady=5)
        entry_2.pack(pady=5)
        boton_area.pack(pady=10)

    elif figura == "Círculo":
        label_1.config(text="Radio:")
        label_1.pack(pady=5)
        entry_1.pack(pady=5)
        boton_area.pack(pady=10)

    elif figura == "Polígono Regular":
        label_1.config(text="Perímetro:")
        label_2.config(text="Apotema:")
        label_1.pack(pady=5)
        entry_1.pack(pady=5)
        label_2.pack(pady=5)
        entry_2.pack(pady=5)
        boton_area.pack(pady=10)

def calcular_area():
    figura = combo.get()
    try:
        if figura == "Cuadrado":
            lado = float(entry_1.get())
            area = lado ** 2
        elif figura == "Rectángulo":
            base = float(entry_1.get())
            altura = float(entry_2.get())
            area = base * altura
        elif figura == "Triángulo":
            base = float(entry_1.get())
            altura = float(entry_2.get())
            area = 0.5 * base * altura
        elif figura == "Círculo":
            radio = float(entry_1.get())
            area = math.pi * (radio ** 2)
        elif figura == "Polígono Regular":
            perimetro = float(entry_1.get())
            apotema = float(entry_2.get())
            area = (perimetro * apotema) / 2
        resultado.config(text=f"Área: {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")

# Función para limpiar campos de entrada
def limpiar_campos():
    label_1.pack_forget()
    label_2.pack_forget()
    entry_1.pack_forget()
    entry_2.pack_forget()
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    boton_area.pack_forget()
    resultado.config(text="Área:")
    
#Funcion para claculadora de botones    

#Funcion para ingreso de nuemros y operaciones

def click_boton(item):
    global expresion
    expresion += str(item)
    input_text.set(expresion)
    
# Función para calcular el resultado
def calcular():
    global expresion
    try:
        resultado = str(eval(expresion))  # Evalúa la expresión ingresada
        input_text.set(resultado)
        expresion = resultado
    except:
        input_text.set("Error")
        expresion = ""

# Función para limpiar la pantalla
def limpiar():
    global expresion
    expresion = ""
    input_text.set("")
    

# Configuración de la ventana principal
window = ThemedTk(theme="adapta")
window.title=("Evidencias")

# Crear un widget Notebook (pestañas)
notebook = ttk.Notebook(window)
notebook.pack(pady=10, expand=True)

# Pestaña 1: Calculadora de Áreas
frame1 = ttk.Frame(notebook)
notebook.add(frame1, text="Calculadora de Áreas")

# Combobox para seleccionar la figura
label_figura = ttk.Label(frame1, text="Seleccione la figura:")
label_figura.pack(pady=5)

combo = ttk.Combobox(frame1, values=["Cuadrado", "Rectángulo", "Triángulo", "Círculo", "Polígono Regular"], state="readonly")
combo.pack(pady=5)
combo.bind("<<ComboboxSelected>>", mostrar_campos_figura)

# Etiquetas y campos de entrada para los valores
label_1 = ttk.Label(frame1)
label_2 = ttk.Label(frame1)
entry_1 = ttk.Entry(frame1)
entry_2 = ttk.Entry(frame1)

# Botón para calcular el área
boton_area = ttk.Button(frame1, text="Calcular Área", command=calcular_area)

# Resultado del cálculo
resultado = ttk.Label(frame1, text="Área:")
resultado.pack(pady=5)

# Pestaña 2: Calculadora Básica Botones
frame2 = ttk.Frame(notebook, width=200, height=280)
notebook.add(frame2, text='Calculadora')


# Variable para almacenar la expresión ingresada
expresion = ""
input_text = tk.StringVar()

# Marco para la pantalla de la calculadora
pantalla = tk.Entry(frame2, textvariable=input_text, font=('arial', 18, 'bold'), bd=20, insertwidth=4, width=14, borderwidth=4, justify="right")
pantalla.grid(row=0, column=0, columnspan=4)

# Botones de la calculadora
botones = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    'C', '0', '=', '+'
]

fila = 1
columna = 0

# Crear los botones y agregarlos a la ventana
for boton in botones:
    if boton == '=':
        tk.Button(frame2, text=boton, width=10, height=3, command=calcular).grid(row=fila, column=columna)
    elif boton == 'C':
        tk.Button(frame2, text=boton, width=10, height=3, command=limpiar).grid(row=fila, column=columna)
    else:
        tk.Button(frame2, text=boton, width=10, height=3, command=lambda b=boton: click_boton(b)).grid(row=fila, column=columna)
    
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1


# Pestaña 3: Temporizador con

# Inicializar pygame para el sonido de la alarma
pygame.init()
# Función para el temporizador con alarma

def iniciar_temporizador():
    try:
        minutos = int(entry_minutos.get())
        segundos = int(entry_segundos.get())
        total_segundos = minutos * 60 + segundos
        actualizar_tiempo_restante(total_segundos)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")

def actualizar_tiempo_restante(segundos_restantes):
    if segundos_restantes >= 0:
        minutos_restantes = segundos_restantes // 60
        segundos_restantes = segundos_restantes % 60
        tiempo_formateado = f"{minutos_restantes:02d}:{segundos_restantes:02d}"
        label_tiempo.config(text=tiempo_formateado)
        # Actualiza cada segundo
        window.after(1000, actualizar_tiempo_restante, segundos_restantes - 1)
    else:
        sonar_alarma()

def sonar_alarma():
    pygame.mixer.music.load("c:\perifericos\Alarm-Clock.mp3")  # Cargar un archivo de sonido
    pygame.mixer.music.play()

frame3 = ttk.Frame(notebook, width=200, height=280)
notebook.add(frame3, text="Temporizador")

# Configuración del temporizador
label_temporizador = ttk.Label(frame3, text="Ingrese el tiempo para el temporizador:")
label_temporizador.pack(pady=10)

# Campos de entrada para minutos y segundos
entry_minutos = ttk.Entry(frame3, width=5)
entry_minutos.pack(pady=5)
entry_minutos.insert(0, "Minutos")

entry_segundos = ttk.Entry(frame3, width=5)
entry_segundos.pack(pady=5)
entry_segundos.insert(0, "Segundos")

# Botón para iniciar el temporizador
boton_iniciar = ttk.Button(frame3, text="Iniciar Temporizador", command=iniciar_temporizador)
boton_iniciar.pack(pady=10)

# Mostrar tiempo restante
label_tiempo = ttk.Label(frame3, text="00:00", font=("Helvetica", 24))
label_tiempo.pack(pady=10)

#Pestaña 4 Integrantes

frame4 = ttk.Frame(notebook, width=200, height=280)
notebook.add(frame4, text='Integrantes')


# direcciones de imagenes
imagen = PhotoImage(file=r"c:\perifericos\INTEGRANTES\INTEGRANTES\rap.png")
imagen1 = PhotoImage(file=r"c:\perifericos\INTEGRANTES\INTEGRANTES\goku.png")
imagen2 = PhotoImage(file=r"c:\perifericos\INTEGRANTES\INTEGRANTES\gato.png")
imagen3 = PhotoImage(file=r"c:\perifericos\INTEGRANTES\INTEGRANTES\jk.png")


# TITULOS
tk.Label(frame4, text='NOMBRES').grid(column=1, row=0)
tk.Label(frame4, text='MATRICULAS').grid(column=2, row=0)
tk.Label(frame4, text='NUMERO DE LISTA ').grid(column=3, row=0)
tk.Label(frame4, text='IMAGENES ').grid(column=4, row=0)

# integrantes
tk.Label(frame4, text='JUAN JOSE BAUTISTA ESPINOSA ').grid(column=1, row=2)
tk.Label(frame4, text='CARLOS CASTRO CERECEDO  ').grid(column=1, row=3)
tk.Label(frame4, text='PAOLA LEZAMA SALAS').grid(column=1, row=4)
tk.Label(frame4, text='IAN MISAEL MOYOTL MOYOTL ').grid(column=1, row=1)

# MATRICULAS
tk.Label(frame4, text='231403169').grid(column=2, row=2)
tk.Label(frame4, text='231403001').grid(column=2, row=3)
tk.Label(frame4, text='231403009').grid(column=2, row=4)
tk.Label(frame4, text='231403044').grid(column=2, row=1)

# NUMEROS DE LISTA
tk.Label(frame4, text='1').grid(column=3, row=2)
tk.Label(frame4, text='3 ').grid(column=3, row=3)
tk.Label(frame4, text='9').grid(column=3, row=4)
tk.Label(frame4, text='13').grid(column=3, row=1)

# IMAGENES
tk.Label(frame4, image=imagen1).grid(column=4, row=2)
tk.Label(frame4, image=imagen2).grid(column=4, row=3)
tk.Label(frame4, image=imagen3).grid(column=4, row=4)
tk.Label(frame4, image=imagen).grid(column=4, row=1)

# Barra de progreso
progress = ttk.Progressbar(frame4, orient="horizontal", length=400, mode="determinate")
progress.grid(column=1, row=5, columnspan=4, pady=20)

# Función para actualizar la barra de progreso y cerrar la ventana cuando termine
def update_progress():
    progress["value"] = 0  # Inicializa la barra en 0
    for i in range(10):
        sleep(0.9)  # Simula trabajo o carga
        progress["value"] += 10  # Incrementa la barra
        frame4.update_idletasks()  # Actualiza la ventana para reflejar cambios
    
    frame4.destroy()  # Cierra la ventana cuando la barra llegue al 100%

# Botón para iniciar la barra de progreso
start_button = tk.Button(frame4, text="Iniciar", command=update_progress)
start_button.grid(column=1, row=6, columnspan=4)




window.mainloop()