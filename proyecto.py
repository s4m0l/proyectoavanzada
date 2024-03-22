from datetime import datetime, timedelta

# Clase Tarea
class Tarea:
    def __init__(self, titulo, descripcion, fecha_vencimiento):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.completada = False

# Clase ListaTareas
class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea '{tarea.titulo}' fue agregada.")

    def marcar_completada(self, tarea):
        tarea.completada = True
        print(f'La tarea {tarea.titulo} fue completada.')

    def obtener_tareas_pendientes(self):
        return [tarea for tarea in self.tareas if not tarea.completada]

    def obtener_tareas_completadas(self):
        return [tarea for tarea in self.tareas if tarea.completada]

# Clase Notificador (Observer)
class Notificador:
    def __init__(self, lista_tareas):
        self.lista_tareas = lista_tareas

    def notificar_tareas_proximas(self):
        tareas_pendientes = self.lista_tareas.obtener_tareas_pendientes()
        hoy = datetime.now().date()
        for tarea in tareas_pendientes:
            if tarea.fecha_vencimiento and tarea.fecha_vencimiento <= hoy + timedelta(days=1):
                print(f"La tarea '{tarea.titulo}' está próxima a su fecha de vencimiento, hazla pronto")

# Clase GestorTareas (Singleton)
class GestorTareas:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.lista_tareas = ListaTareas()
            cls._instance.notificador = Notificador(cls._instance.lista_tareas)
        return cls._instance

    def agregar_tarea(self, titulo, descripcion, fecha_vencimiento):
        tarea = Tarea(titulo, descripcion, fecha_vencimiento)
        self.lista_tareas.agregar_tarea(tarea)

    def marcar_completada(self, titulo):
        for tarea in self.lista_tareas.tareas:
            if tarea.titulo == titulo:
                self.lista_tareas.marcar_completada(tarea)
                print(f"La tarea '{tarea.titulo}' fue completada.")

    def mostrar_tareas_pendientes(self):
        tareas_pendientes = self.lista_tareas.obtener_tareas_pendientes()
        if tareas_pendientes:
            print("Tareas pendientes:")
            for tarea in tareas_pendientes:
                print(f"- {tarea.titulo}")
        else:
            print("No hay tareas pendientes.")

    def mostrar_tareas_completadas(self):
        tareas_completadas = self.lista_tareas.obtener_tareas_completadas()
        if tareas_completadas:
            print("Tareas completadas:")
            for tarea in tareas_completadas:
                print(f"- {tarea.titulo}")
        else:
            print("No hay tareas completadas.")

# Función para mostrar el menú
def menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar tareas pendientes")
    print("4. Mostrar tareas completadas")
    print("5. Salir")

# Ejemplo de uso
gestor = GestorTareas()

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        titulo = input("Ingrese el título de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        fecha_str = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
        fecha_vencimiento = datetime.strptime(fecha_str, "%Y-%m-%d")
        gestor.agregar_tarea(titulo, descripcion, fecha_vencimiento)
    elif opcion == "2":
        titulo = input("Ingrese el título de la tarea completada: ")
        gestor.marcar_completada(titulo)
    elif opcion == "3":
        gestor.mostrar_tareas_pendientes()
    elif opcion == "4":
        gestor.mostrar_tareas_completadas()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
