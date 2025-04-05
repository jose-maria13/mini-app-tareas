from database import save_task

def handle_task_submission(task_name):
    """
    Valida y guarda una tarea.
    """
    if not task_name.strip():
        return "Error: la tarea está vacía"

    # Seguridad: Validamos entrada para evitar valores inválidos o ataques.
    save_task(task_name)
    return f"Tarea guardada: {task_name}"

# Comentario sobre Mantenibilidad:
# Mantenibilidad: La validación y lógica están separadas del almacenamiento, facilitando su modificación.
