import tkinter as tk
from tkinter import ttk, messagebox

# Función para calcular el esfuerzo, tiempo, tamaño del equipo y costo basado en COCOMO I
def calcular_cocomo():
    try:
        kloc = float(entry_kloc.get())
        tipo_proyecto = combo_tipo.get()
        costo_por_persona_mes = float(entry_costo.get())  # Costo por persona-mes

        # Parámetros de COCOMO I
        parametros = {
            "Orgánico": (2.4, 1.05, 2.5, 0.38),
            "Semi Acoplado": (3.0, 1.12, 2.5, 0.35),
            "Acoplado": (3.6, 1.20, 2.5, 0.32),
        }

        if tipo_proyecto not in parametros:
            raise ValueError("Selecciona un tipo de proyecto válido.")

        a, b, c, d = parametros[tipo_proyecto]

        # Cálculos
        esfuerzo = a * (kloc ** b)  # Persona-mes
        tiempo = c * (esfuerzo ** d)  # Meses
        equipo = esfuerzo / tiempo  # Personas
        costo_total = esfuerzo * costo_por_persona_mes  # Costo total del proyecto

        # Mostrar resultados
        label_resultado.config(
            text=(f"Resultados:\n"
                  f"Esfuerzo: {esfuerzo:.2f} persona-mes\n"
                  f"Tiempo: {tiempo:.2f} meses\n"
                  f"Tamaño del equipo: {equipo:.2f} personas\n"
                  f"Costo total: ${costo_total:,.2f}")
        )
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

# Función para limpiar los campos
def limpiar_campos():
    entry_kloc.delete(0, tk.END)
    combo_tipo.set("")
    entry_costo.delete(0, tk.END)
    label_resultado.config(text="Resultados:")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora COCOMO I")
ventana.geometry("600x500")
ventana.resizable(False, False)

# Colores y diseño
ventana.config(bg="#f0f8ff")

# Título
titulo = tk.Label(
    ventana,
    text="Calculadora de Estimación de Costos - COCOMO I",
    font=("Arial", 14, "bold"),
    bg="#4682b4",
    fg="white",
    pady=10,
)
titulo.pack(fill=tk.X)

# Subtítulo KLOC
subtitulo = tk.Label(
    ventana,
    text="(KLOC: Miles de Líneas de Código Fuente)",
    font=("Arial", 10),
    bg="#f0f8ff",
    fg="black",
)
subtitulo.pack()

# Frame de entradas
frame_entrada = tk.Frame(ventana, bg="#f0f8ff", pady=20)
frame_entrada.pack()

# Entrada de KLOC
label_kloc = tk.Label(frame_entrada, text="Tamaño del proyecto (KLOC):", bg="#f0f8ff", font=("Arial", 12))
label_kloc.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_kloc = tk.Entry(frame_entrada, font=("Arial", 12))
entry_kloc.grid(row=0, column=1, padx=10, pady=10)

# Tipo de proyecto
label_tipo = tk.Label(frame_entrada, text="Tipo de proyecto:", bg="#f0f8ff", font=("Arial", 12))
label_tipo.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
combo_tipo = ttk.Combobox(frame_entrada, font=("Arial", 12), state="readonly")
combo_tipo["values"] = ["Orgánico", "Semi Acoplado", "Acoplado"]
combo_tipo.grid(row=1, column=1, padx=10, pady=10)

# Costo por persona-mes
label_costo = tk.Label(frame_entrada, text="Costo por persona-mes ($):", bg="#f0f8ff", font=("Arial", 12))
label_costo.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
entry_costo = tk.Entry(frame_entrada, font=("Arial", 12))
entry_costo.grid(row=2, column=1, padx=10, pady=10)

# Botones
frame_botones = tk.Frame(ventana, bg="#f0f8ff")
frame_botones.pack(pady=10)

btn_calcular = tk.Button(
    frame_botones,
    text="Calcular",
    font=("Arial", 12, "bold"),
    bg="#32cd32",
    fg="white",
    padx=20,
    command=calcular_cocomo,
)
btn_calcular.grid(row=0, column=0, padx=10)

btn_limpiar = tk.Button(
    frame_botones,
    text="Limpiar",
    font=("Arial", 12, "bold"),
    bg="#ff6347",
    fg="white",
    padx=20,
    command=limpiar_campos,
)
btn_limpiar.grid(row=0, column=1, padx=10)

# Resultados
label_resultado = tk.Label(
    ventana,
    text="Resultados:",
    bg="#f0f8ff",
    font=("Arial", 12),
    justify=tk.LEFT,
    anchor="w",
)
label_resultado.pack(fill=tk.BOTH, padx=20, pady=20)

# Iniciar la ventana
ventana.mainloop()
