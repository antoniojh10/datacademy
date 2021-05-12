def calc_triangle_area(base, height):
  return (base * height) / 2.0

def run():
  triangle_base = float(input('Ingresa el valor de la base del triángulo: '))
  triangle_height = float(input('Ingresa el valor de la altura del triángulo: '))

  triangle_area = calc_triangle_area(triangle_base, triangle_height)

  print(f"El área del triángulo es de: {triangle_area}")


if __name__ == '__main__':
  run()

