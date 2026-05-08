# ---- Funciones provistas (NO modificar) ----

def is_even(n):
    return n % 2 == 0


def is_positive(n):
    """Dado un número entero n, retorna True si es mayor a 0, False en caso contrario."""
    return n > 0


# ---- Función a implementar ----

def classify_number(n):
    """
    Dado un número entero n, retorna un string que lo clasifica.
    Debe USAR las funciones is_even e is_positive para resolver el ejercicio.

    Clasificaciones posibles:
      - "positive even"   (positivo y par)
      - "positive odd"    (positivo e impar)
      - "negative even"   (negativo y par)
      - "negative odd"    (negativo e impar)
      - "zero"            (el número es 0)
    """

    if n==0:
        return "zero"

    elif is_even(n) == True and is_positive(n) == True:
        return "positive even"

    elif is_even(n) == True and is_positive(n) == False:
        return "negative even"

    elif is_even(n) == False and is_positive(n) == True:
        return "positive odd"

    else:
        return "negative odd"

