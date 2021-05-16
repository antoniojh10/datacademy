def calc_triangle_area(base, height):
    area = (base * height) / 2.0
    return round(area, 2)


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


if __name__ == "__main__":
    run()
