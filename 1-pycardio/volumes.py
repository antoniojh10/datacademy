from math import pi


def cilindro():
    print("Elegiste un Cilindro")
    while True:
        try:
            radio = float(input("Ingrese el radio: "))
        except:
            print("El valor ingresado no es valido")
        else:
            break

    while True:
        try:
            height = float(input("Ingrese la altura: "))
        except:
            print("El valor ingresado no es valido")
        else:
            break

    volume = pi * height * radio ** 2
    return volume


def cubo():
    print("Elegiste un Cubo")
    while True:
        try:
            side = float(input("Ingrese el valor de un lado: "))
        except:
            print("El valor ingresado no es valido")
        else:
            break

    volume = side ** 3
    return volume


def run():
    options = {"1": "Cilindro", "2": "Cubo", "e": "Salir"}

    switcher = {
        "1": cilindro,
        "2": cubo,
    }

    print("-----------------------------")
    print("Bienvenido a la calculadora de volumenes")

    while True:
        print("Seleciona la figura que quieres calcular:")
        for key, value in options.items():
            print(f"     {key} - {value}")

        selection = input("Ingresa el número de la figura que quieres calcular: ")

        try:
            assert selection in options.keys(), "Ingresa una opcion valida"
        except AssertionError as ae:
            print(ae)
        else:
            if selection == "e":
                break

            element = switcher.get(selection)

            volume = element()

            print("El area es: " + str(volume))


if __name__ == "__main__":
    run()
