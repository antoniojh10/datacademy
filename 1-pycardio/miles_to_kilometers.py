def kilometers_to_miles(kilometers):
    miles = round(kilometers / 1.609344, 4)
    print(f"El resultado es {miles} millas")
    return miles


def miles_to_kilometers(miles):
    kilometers = round(miles * 1.609344, 4)
    print(f"El resultado es {kilometers} kilometros")
    return kilometers


def transform(option):
    options_name = {1: "millas", 2: "kilometros"}

    try:
        value_to_transform = float(input(f"Ingresa el valor en {options_name[option]}: "))
    except:
        print("Error. Tienes que ingresar un número")
    else:
        if option == 1:
            miles_to_kilometers(value_to_transform)
        if option == 2:
            kilometers_to_miles(value_to_transform)


def run():
    print("Bienvenido al transformador de unidades, elige una de las siguientes opciones")

    options = [1, 2, 3]

    while True:
        print("-----------------------------------------------------------------------")
        option_selected = input(
            """
        1 - Millas a kilometros
        2 - Kilometros a millas
        3 - Salir
        """
        )

        try:
            assert option_selected.isnumeric(), "Ingresa una opcion valida"
            option_selected = int(option_selected)
            assert option_selected in options, "Ingresa una opcion valida"
        except AssertionError as ae:
            print(ae)
        else:
            if option_selected == 1 or option_selected == 2:
                transform(option_selected)
            else:
                break

    print("Ten un gran día")


if __name__ == "__main__":
    run()
