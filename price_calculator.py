# ________________________________________FUNCIONES PROVISTAS________________________________________

def apply_discount(price, discount_pct):
    """Dado un precio y un porcentaje de descuento, retorna el precio con el descuento aplicado."""
    return price * (1 - discount_pct / 100)

def apply_tax(price, tax_pct):
    """Dado un precio y un porcentaje de impuesto, retorna el precio con el impuesto aplicado."""
    return price * (1 + tax_pct / 100)

    # ________________________________________RESOLUCION EJERCICIO 5_______________________________________

#________________________________________FINAL PRICE________________________________________

def final_price(price, quantity, discount_pct, tax_pct):
    """
    Calcula el precio final de una compra.
    Debe USAR las funciones apply_discount y apply_tax.

    Pasos:
      1. Calcular el subtotal (price * quantity).
      2. Aplicar el descuento al subtotal usando apply_discount.
      3. Aplicar el impuesto al resultado usando apply_tax.
      4. Retornar el resultado redondeado a 2 decimales usando round().
    """

    subtotal = price * quantity

    con_descuento = apply_discount(subtotal, discount_pct)
    con_impuesto = apply_tax(con_descuento, tax_pct)

    redondeado = round(con_impuesto, 2)

    return redondeado

#________________________________________BEST DEAL________________________________________


def best_deal(price_a, qty_a, disc_a, price_b, qty_b, disc_b, tax_pct):
    """
    Dados dos productos A y B (cada uno con su precio, cantidad y descuento)
    y un porcentaje de impuesto común, retorna el string "A" o "B"
    según cuál tenga el menor precio final.
    Si son iguales, retorna "A".
    Debe USAR la función final_price para resolver el ejercicio.
    """

    total_A = price_a * qty_a
    descuento_A = apply_discount(total_A, disc_a)
    impuesto_A = apply_tax(descuento_A, tax_pct)
    precio_final_A = impuesto_A

    total_B = price_b * qty_b
    descuento_B = apply_discount(total_B, disc_b)
    impuesto_B = apply_tax(descuento_B, tax_pct)
    precio_final_B = impuesto_B

    if precio_final_A > precio_final_B:
        final_price = "B"
    elif precio_final_A < precio_final_B:
        final_price = "A"
    else:
        final_price = "A"

    return final_price