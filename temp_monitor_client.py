# temp_monitor_client.py
# Programa cliente que lee temperaturas de un archivo
# e imprime la racha creciente mas larga.

import temp_monitor


def main():
    name = input("Nombre del archivo:")

    archivo = open(name, "r")
    n = int(archivo.readline().strip())

    monitor = temp_monitor.init(n)

    for _ in range(n):
        temp = float(archivo.readline().strip())
        monitor = temp_monitor.add_reading(monitor, temp)
    archivo.close()
    
    result = temp_monitor.longest_rising_streak(monitor)
    print (result)
    
    
    pass


if __name__ == "__main__":
    main()
