# Inicializar la tabla (lista de diccionarios)
tabla = []

# Función para agregar un estudiante y su nota
def agregar_estudiante():
    nombre = input("Nombre: ")
    puntos_correctos = int(input(f"Puntos correctos de {nombre}: "))
    resultado = 5 * puntos_correctos
    nota_final = resultado / 18
    nota_final_redondeada = round(nota_final, 2)
    print(f"La nota de {nombre} es: {nota_final_redondeada:.2f}")

    # Agregar los datos a la tabla
    tabla.append({"Nombre": nombre, "Nota Final": nota_final_redondeada})

# Función para mostrar la tabla
def mostrar_tabla():
    print("\nTabla de Estudiantes y Notas Finales")
    print("====================================")
    for estudiante in tabla:
        print(f"Nombre: {estudiante['Nombre']}, Nota Final: {estudiante['Nota Final']:.2f}")

# Ciclo principal para agregar estudiantes y opciones de visualización
while True:
    print("\nOpciones:")
    print("1. Agregar estudiante")
    print("2. Mostrar tabla de estudiantes y notas")
    print("3. Salir")
    
    opcion = input("Selecciona una opción (1-3): ")
    
    if opcion == '1':
        agregar_estudiante()
    elif opcion == '2':
        mostrar_tabla()
    elif opcion == '3':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
