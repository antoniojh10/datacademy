from math import sqrt


def calc_triangle_area(base, height):
    area = (base * height) / 2.0
    return round(area, 2)


def try_equilateral(base, height):
    h_equilateral = sqrt(base ** 2 - (base / 2) ** 2)
    if round(h_equilateral, 2) == round(height, 2):
        return True
    return False


def try_isosceles(base, height):
    pass


def guess_triangle_type(base, height):
    is_quilateral = try_equilateral(base, height)
    if is_quilateral:
        return "equilátero"

    is_isosceles = try_isosceles(base, height)
    if is_isosceles:
        return "isósceles"

    return "escaleno"


def run():
    status = "base"

    while status == "base":
        try:
            triangle_base = float(input("Ingresa el valor de la base del triángulo: "))
        except ValueError:
            print("Ingresa un número")
        else:
            status = "altura"

    while status == "altura":
        try:
            triangle_height = float(input("Ingresa el valor de la altura del triángulo: "))
        except ValueError:
            print("Ingresa un número")
        else:
            status = "area"

    triangle_area = calc_triangle_area(triangle_base, triangle_height)

    print(f"El área del triángulo es de: {triangle_area}")

    print(
        """
    Quieres saber el tipo de triángulo triangulo? (Necesitaremos que otro lado diferente de la base)
    1 - Si
    2 - No
    """
    )
    bonus_option = input("Escribe 1 o 2: ")

    while bonus_option != "1" and bonus_option != "2":
        print("Error, ingresa 1 para Si o 2 para No")
        bonus_option = input("Escribe 1 o 2: ")

    if bonus_option == "1":
        status = "bonus_1"
        while status == "bonus_1":
            try:
                second_side = float(input("Ingresa el valor otro lado del triángulo (diferente de la base): "))
                if second_side < triangle_height:
                    raise ValueError("El lado B debe medir al menos lo mismo que la altura")
            except ValueError as ve:
                print(f"{ve}. Ingresa un número")
            else:
                status = "bonus_2"

        triangle_type = guess_triangle_type(triangle_base, triangle_height, second_side)
        print(f"El triángulo es de tipo {triangle_type}")


if __name__ == "__main__":
    run()
