import tkinter as tk
from tkinter import ttk

# Función para agregar un estudiante a la tabla
def agregar_estudiante():
    nombre = nombre_entry.get()
    puntos_correctos = int(puntos_entry.get())
    resultado = 5 * puntos_correctos
    nota_final = round(resultado / 18, 1)
    
    # Insertar los datos en la tabla con la etiqueta 'center'
    tree.insert("", "end", values=(nombre, puntos_correctos, nota_final), tags=('center',))
    
    # Limpiar las entradas
    nombre_entry.delete(0, tk.END)
    puntos_entry.delete(0, tk.END)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Registro de Notas de Estudiantes")

# Configuración del frame principal
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Etiquetas y entradas para el nombre y los puntos correctos
nombre_label = ttk.Label(frame, text="Nombre:")
nombre_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

nombre_entry = ttk.Entry(frame, width=20)
nombre_entry.grid(row=0, column=1, padx=5, pady=5)

puntos_label = ttk.Label(frame, text="Puntos correctos:")
puntos_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

puntos_entry = ttk.Entry(frame, width=20)
puntos_entry.grid(row=1, column=1, padx=5, pady=5)

# Botón para agregar estudiante
agregar_button = ttk.Button(frame, text="Agregar Estudiante", command=agregar_estudiante)
agregar_button.grid(row=2, column=0, columnspan=2, pady=10)

# Configuración de la tabla
columns = ("Nombre", "Puntos Correctos", "Nota Final")
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading("Nombre", text="Nombre")
tree.heading("Puntos Correctos", text="Puntos Correctos")
tree.heading("Nota Final", text="Nota Final")

# Configuración del estilo para centrar los datos
tree.tag_configure('center', anchor='center')

# Añadir la tabla al frame
tree.grid(row=3, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

# Configuración del scrollbar para la tabla
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=3, column=2, sticky=(tk.N, tk.S))

# Ejecutar la aplicación y finalizar
root.mainloop()
