# temp_monitor_client.py
# Programa cliente que lee temperaturas de un archivo
# e imprime la racha creciente mas larga.

import temp_monitor


def main():
    name = input("Nombre del archivo:")
     # TODO: Pedir el nombre del archivo al usuario usando input()
    archivo = open(name, "r")
    n = int(archivo.readline().strip())
    # TODO: Abrir el archivo y leer el numero de lecturas n
    monitor = temp_monitor.init(n)
     # TODO: Crear el monitor usando temp_monitor.init(n)
    for _ in range(n):
        temp = float(archivo.readline().strip())
        monitor = temp_monitor.add_reading(monitor, temp)
    archivo.close()
    # TODO: Leer las n temperaturas y agregarlas con temp_monitor.add_reading()
    result = temp_monitor.longest_rising_streak(monitor)
    print (result)
    # TODO: Imprimir la racha creciente mas larga usando temp_monitor.longest_rising_streak()
    
    pass


if __name__ == "__main__":
    main()
