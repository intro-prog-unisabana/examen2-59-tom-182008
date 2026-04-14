# temp_monitor.py
# Libreria de funciones para registrar lecturas de temperatura.
#
# Estructura del diccionario (monitor):
#   - 'max':      numero maximo de lecturas permitidas (int)
#   - 'readings': lista con las temperaturas de cada lectura (list)
#   - 'total':    suma total de todas las temperaturas (float)


def init(max_readings):
    return {"max": max_readings, "readings": [], "total": 0.0}
    # TODO: Implementar
    pass


def add_reading(monitor, temp):
   monitor["readings"].append(temp) 
   monitor["total"] += temp  
   return monitor
    # TODO: Implementar
pass


def count(monitor):
    return len(monitor["readings"])
    # TODO: Implementar
    pass


def average_temp(monitor):
    if not monitor["readings"]:
        return 0.0
    return monitor["total"] / len(monitor["readings"])
    # TODO: Implementar
    pass


def format_readings(monitor):
    return str(monitor["readings"])
    # TODO: Implementar
    pass


def highest_temp(monitor):
    if not monitor["readings"]:
        return None 
    return max(monitor["readings"])
    # TODO: Implementar
    pass


def coldest_window(monitor, k):
    if len(monitor["readings"]) < k:
        return None
    min_avg = float('inf')
    for i in range(len(monitor["readings"]) - k + 1):
        window = monitor["readings"] [i:i+k]
        avg = sum(window) / k
        if avg < min_avg:
            min_avg = avg  
    return min_avg
    # TODO: Implementar
    pass


def longest_rising_streak(monitor):
        if not monitor["readings"]:
            return 0 
        max_streak = 1
        current_streak = 1
        for i in range(1, len(monitor["readings"])):
            if monitor["readings"][i] > monitor["readings"][i - 1]:
                current_streak += 1
            else:
                max_streak = max(max_streak, current_streak)
                current_streak = 1
        max_streak = max(max_streak, current_streak)
        return max_streak
    # TODO: Implementar
        pass


def main():
    # crear un monitor para temperaturas de Bogota (12 horas, 6am-5pm)
    monitor = init(12)
    monitor = add_reading(monitor, 8.0)   # 6am
    monitor = add_reading(monitor, 9.5)   # 7am
    monitor = add_reading(monitor, 11.0)  # 8am
    monitor = add_reading(monitor, 13.5)  # 9am
    monitor = add_reading(monitor, 15.0)  # 10am
    monitor = add_reading(monitor, 17.5)  # 11am
    monitor = add_reading(monitor, 19.0)  # 12pm
    monitor = add_reading(monitor, 20.0)  # 1pm
    monitor = add_reading(monitor, 19.5)  # 2pm
    monitor = add_reading(monitor, 18.0)  # 3pm
    monitor = add_reading(monitor, 16.5)  # 4pm
    monitor = add_reading(monitor, 15.0)  # 5pm

    # imprimir estadisticas
    print("numero de lecturas =", count(monitor))               # 12
    print("temp promedio =", average_temp(monitor))             # 15.208...
    print("temp mas alta =", highest_temp(monitor))             # 20.0
    print("ventana mas fria (3) =", coldest_window(monitor, 3)) # 9.5
    print("racha creciente =", longest_rising_streak(monitor))  # 8

    # imprimir temperaturas
    print(format_readings(monitor))


if __name__ == "__main__":
    main()
