def hacer_cierre(cont_a, cont_b, cont_c, dinero):
    dinero_final = 0
    dinero_final += cont_a * 5000
    dinero_final += cont_b * 7500
    dinero_final += cont_c * 18000
    return dinero - dinero_final


def calcular_dia():
    global total_a, total_b, total_c
    cont_a = 0
    cont_b = 0
    cont_c = 0
    dinero = (int(input("Ingrese el dinero recaudado.")))
    letra = "A"
    while letra != "D":
        letra = input("Ingrese el tipo de vehículo. A. Automóvil, B. Bus, C. Camión y D. Salir")
        if letra == "A":
            cont_a += 1
            total_a += 1
        elif letra == "B":
            cont_b += 1
            total_b += 1
        elif letra == "C":
            cont_c += 1
            total_c += 1
    return hacer_cierre(cont_a, cont_b, cont_c, dinero)


def principal():
    global total_a, total_b, total_c
    a = 1
    mayor = 0
    dia_mayor = 0
    total_descuadre = 0
    while a <= 30:
        print("Información para el día " + str(a))
        dinero = calcular_dia()
        # mayor = 0
        if dinero == 0:
            print("El día " + str(a) + " se obtuvo un cierre exitoso.")
        else:
            if dinero < 0:
                dinero *= -1
            if dinero > mayor:
                mayor = dinero
                dia_mayor = a
            total_descuadre += dinero
            print("El día " + str(a) + " NO se obtuvo un cierre exitoso, hubo un descuadre de " + str(dinero))
        a += 1
    print("El valor total recolectado para los automóviles fue de " + str((total_a * 5000)))
    print("El valor total recolectado para los buses fue de " + str((total_b * 7500)))
    print("El valor total recolectado para los camiones fue de " + str((total_c * 18000)))
    print("El día donde se presento el mayor descuadre fue el día " + str(dia_mayor) + " con un descuadre de " +
          str(mayor))
    print("El total del descuadre del mes fue de " + str(total_descuadre))

total_a = 0
total_b = 0
total_c = 0
principal()
