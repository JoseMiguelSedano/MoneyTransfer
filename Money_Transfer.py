"Proyecto Money Transfer"


from abc import ABC, abstractmethod


class Transaccion(ABC):
    "Clase Transaccion"
    def __init__(self, id, tipo, monto, categoria, fecha):
        self.__id = id
        self.__tipo = tipo
        self.__monto = monto
        self.__categoria = categoria
        self.__fecha = fecha

    @property
    def id(self):
        return self.__id

    @property
    def tipo(self):
        return self.__tipo

    @property
    def monto(self):
        return self.__monto

    @property
    def categoria(self):
        return self.__categoria

    @property
    def fecha(self):
        return self.__fecha

    def mostrar_tipo(self):
        "Mostrar tipo"


class Ingreso(Transaccion):
    def mostrar_tipo(self):
        return "Ingreso"


class Gasto(Transaccion):
    def mostrar_tipo(self):
        return "Gasto"


def menu():
    "Funcion del menu principal"
    while True:
        print("<<< MONEY TRANSFER >>>")
        print("Bienvenido al sistema de Money Transfer")
        print("1. Transaccion")
        print("2. Saldo")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            while True:
                tipo = input("Ingrese el tipo de transaccion a realizar (I / G): ")
                if tipo == 'I':
                    print("Tipo de transacción: Ingreso")
                    id = 1
                    monto = float(input("Ingrese el monto: "))
                    categoria = input("Ingrese la categoría: ")
                    fecha = input("Ingrese la fecha: ")
                    nuevo_ingreso = Ingreso(id, "Ingreso", monto, categoria, fecha)
                    print(f"{nuevo_ingreso.mostrar_tipo()} registrado")
                    print()
                    break

                elif tipo == 'G':
                    print("Tipo de transacción: Gasto")
                    id = 1
                    monto = float(input("Ingrese el monto: "))
                    categoria = input("Ingrese la categoría: ")
                    fecha = input("Ingrese la fecha: ")
                    nuevo_gasto = Gasto(id, "Gasto", monto, categoria, fecha)
                    print(f"{nuevo_gasto.mostrar_tipo()} registrado")
                    print()
                    break

                else:
                    print("Tipo de transacción no válido. Intente nuevamente")
                    print()

        elif opcion == "2":
            None
        elif opcion == "3":
            print("Gracias por usar Money Transfer")
            print("Hasta luego :D")
            break
        else:
            print("Opción no valida, intente nuevamente")

menu()
