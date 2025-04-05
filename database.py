# Lista que simula una base de datos
task_storage = []

def save_task(task_name):
    """
    Guarda la tarea en la lista simulando una base de datos.
    """
    task_storage.append(task_name)
    return True

# Comentario sobre Escalabilidad:
# Escalabilidad: Podríamos reemplazar esta lista por una base de datos real (SQL o NoSQL) para manejar miles de tareas.
