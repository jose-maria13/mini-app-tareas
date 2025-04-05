from backend import handle_task_submission

def main():
    """
    Simula un formulario de entrada desde consola.
    """
    tarea = input("Ingrese el nombre de la tarea: ")
    resultado = handle_task_submission(tarea)
    print(resultado)

if __name__ == "__main__":
    main()

# Comentario sobre Escalabilidad:
# Escalabilidad: Esta interfaz puede evolucionar hacia una app web o móvil manteniendo el backend intacto.
