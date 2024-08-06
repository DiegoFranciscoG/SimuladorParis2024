import random

# Diccionarios para almacenar eventos, participantes y medallas
eventos = {}
participantes = {}
medallero = {}

def registrar_evento():
    """Registrar un nuevo evento deportivo."""
    nombre_evento = input("Ingrese el nombre del evento: ")
    eventos[nombre_evento] = []
    print(f"Evento '{nombre_evento}' registrado con éxito.")

def registrar_participante():
    """Registrar un nuevo participante."""
    nombre = input("Ingrese el nombre del participante: ")
    pais = input("Ingrese el país del participante: ")
    if pais not in medallero:
        medallero[pais] = {'oro': 0, 'plata': 0, 'bronce': 0}
    participantes[nombre] = pais
    print(f"Participante '{nombre}' de {pais} registrado con éxito.")

def simular_evento():
    """Simular un evento asignando medallas a los participantes."""
    if not eventos:
        print("No hay eventos registrados.")
        return
    if len(participantes) < 3:
        print("Se requieren al menos 3 participantes para simular un evento.")
        return
    
    # Seleccionar un evento aleatorio
    evento = random.choice(list(eventos.keys()))
    
    # Seleccionar tres participantes aleatoriamente
    competidores = random.sample(list(participantes.keys()), 3)
    
    # Asignar medallas
    oro, plata, bronce = competidores
    eventos[evento] = [oro, plata, bronce]
    
    # Actualizar el medallero
    medallero[participantes[oro]]['oro'] += 1
    medallero[participantes[plata]]['plata'] += 1
    medallero[participantes[bronce]]['bronce'] += 1
    
    print(f"\nResultados del evento '{evento}':")
    print(f"Medalla de oro: {oro} ({participantes[oro]})")
    print(f"Medalla de plata: {plata} ({participantes[plata]})")
    print(f"Medalla de bronce: {bronce} ({participantes[bronce]})")

def generar_informe():
    """Generar un informe final con los resultados de los eventos y el ranking de países."""
    if not eventos:
        print("No se han simulado eventos.")
        return
    
    print("\n--- Informe Final ---\n")
    print("Ganadores por evento:")
    for evento, ganadores in eventos.items():
        print(f"Evento '{evento}':")
        print(f"  Oro: {ganadores[0]} ({participantes[ganadores[0]]})")
        print(f"  Plata: {ganadores[1]} ({participantes[ganadores[1]]})")
        print(f"  Bronce: {ganadores[2]} ({participantes[ganadores[2]]})")
    
    print("\nRanking de países:")
    ranking = sorted(medallero.items(), key=lambda x: (x[1]['oro'], x[1]['plata'], x[1]['bronce']), reverse=True)
    for pais, medallas in ranking:
        print(f"{pais}: Oro: {medallas['oro']}, Plata: {medallas['plata']}, Bronce: {medallas['bronce']}")

def menu():
    """Menú principal del programa."""
    while True:
        print("\n--- Juegos Olímpicos París 2024 ---")
        print("1. Registrar evento")
        print("2. Registrar participante")
        print("3. Simular evento")
        print("4. Generar informe")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_evento()
        elif opcion == '2':
            registrar_participante()
        elif opcion == '3':
            simular_evento()
        elif opcion == '4':
            generar_informe()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    menu()
