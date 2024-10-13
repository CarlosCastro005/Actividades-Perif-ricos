import tkinter as tk
from tkinter import ttk 
from ttkthemes import ThemedTk
from tkinter import messagebox
import pygame

# Pestaña 3: Temporizador con alarma
# Configuración de la ventana principal
window = ThemedTk(theme="adapta")
window.title("Evidencias")

# Crear un widget Notebook (pestañas)
notebook = ttk.Notebook(window)
notebook.pack(pady=10, expand=True)

# Inicializar pygame para el sonido de la alarma
pygame.mixer.init()

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
    try:
        pygame.mixer.music.load("c:/perifericos/Alarm-Clock.mp3")  # Asegúrate de que la ruta sea correcta
        pygame.mixer.music.play()
    except pygame.error as e:
        messagebox.showerror("Error", f"No se pudo reproducir el sonido: {e}")

# Crear la tercera pestaña para el temporizador
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

# Iniciar el bucle principal de la interfaz gráfica
window.mainloop()