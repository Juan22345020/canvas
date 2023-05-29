import tkinter as tk
from tkinter import ttk

def comparar_seguros():
    edad = entrada_edad.get()
    tipo_seguro = entrada_tipo_seguro.get()

    # Lógica para comparar los seguros y generar recomendaciones
    # Aquí se muestra un ejemplo básico con 20 seguros ficticios
    seguros = [
        {"nombre": "Seguro A", "cobertura": "Básica", "precio": 100},
        {"nombre": "Seguro B", "cobertura": "Completa", "precio": 150},
        {"nombre": "Seguro C", "cobertura": "Básica", "precio": 120},
        {"nombre": "Seguro D", "cobertura": "Completa", "precio": 200},
        {"nombre": "Seguro E", "cobertura": "Básica", "precio": 80},
        # Agrega más seguros aquí
    ]

    recomendaciones = []
    for seguro in seguros:
        if seguro["cobertura"] == tipo_seguro:
            recomendaciones.append(seguro)

    # Mostrar recomendaciones en el canvas_resultados
    canvas_resultados.delete("all")
    canvas_resultados.create_text(200, 100, text="Recomendaciones:", font=("Arial", 14), fill="black")
    y = 140
    for i, recomendacion in enumerate(recomendaciones):
        nombre = recomendacion["nombre"]
        cobertura = recomendacion["cobertura"]
        precio = recomendacion["precio"]
        texto = f"{nombre} - Cobertura: {cobertura} - Precio: {precio}"
        canvas_resultados.create_text(200, y, text=texto, font=("Arial", 12), fill="black")
        y += 30

#ventana = tk.Tk()
ventana = tk.Tk()

ventana.title("Comparador y Recomendador de Seguros Médicos")

# Configurar estilo
estilo = ttk.Style()
estilo.configure('TFrame', background='#e6f2ff')
estilo.configure('TButton', background='#4d94ff')
estilo.configure('TLabel', background='#e6f2ff', foreground='#000000', font=('Arial', 12))
estilo.configure('Header.TLabel', font=('Arial', 16, 'bold'))

# Frame principal
frame_principal = ttk.Frame(ventana)
frame_principal.pack(padx=20, pady=20)

# Título
label_titulo = ttk.Label(frame_principal, text="Comparador y Recomendador de Seguros Médicos", style='Header.TLabel')
label_titulo.pack(pady=10)

# Sección de ingreso de datos
frame_datos = ttk.Frame(frame_principal)
frame_datos.pack(pady=20)

# Etiqueta y entrada para la edad
label_edad = ttk.Label(frame_datos, text="Edad:")
label_edad.grid(row=0, column=0, padx=10, pady=10)
entrada_edad = ttk.Entry(frame_datos)
entrada_edad.grid(row=0, column=1, padx=10, pady=10)

# Etiqueta y entrada para el tipo de seguro
label_tipo_seguro = ttk.Label(frame_datos, text="Tipo de Seguro:")
label_tipo_seguro.grid(row=1, column=0, padx=10, pady=10)
entrada_tipo_seguro = ttk.Entry(frame_datos)
entrada_tipo_seguro.grid(row=1, column=1, padx=10, pady=10)

# Botón de comparar seguros
boton_comparar = ttk.Button(frame_datos, text="Comparar", command=comparar_seguros)
boton_comparar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Resultados de la comparación
label_resultados = ttk.Label(frame_principal, text="Resultados:")
label_resultados.pack(pady=10)

canvas_resultados = tk.Canvas(frame_principal, width=400, height=200, bg='#ffffff')
canvas_resultados.pack()

# Personaliza el canvas con información adicional y gráficos
# ...

ventana.mainloop()