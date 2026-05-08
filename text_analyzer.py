# ---- Funciones provistas (NO modificar) ----
def count_vowels(text):
    """Dado un texto, retorna la cantidad de vocales (a, e, i, o, u) que contiene."""
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

def count_consonants(text):
    """Dado un texto, retorna la cantidad de consonantes que contiene."""
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in "aeiou":
            count += 1
    return count

# ---- Funciones a implementar ----

def total_letters(text):
    """
    Retorna la cantidad total de letras en el texto.
    Debe USAR las funciones count_vowels y count_consonants.
    """

    conso= count_consonants (text)
    vocal= count_vowels (text)
    letraas= conso + vocal

    return letraas


def vowel_percentage(text):
    """
    Retorna el porcentaje de vocales sobre el total de letras, redondeado a 1 decimal.
    Si no hay letras, retorna 0.0.
    Debe USAR las funciones count_vowels y total_letters.

    Ejemplo: "hola" tiene 2 vocales de 4 letras → 50.0
    """

    if total_letters(text) == 0:
        return 0.0

    percentage= (100 * count_vowels(text)) / total_letters(text)
    return round(percentage,1)

def analyze_text(text):
    """
    Retorna un string con el análisis completo del texto usando el siguiente formato:
    "V:{vowels} C:{consonants} T:{total} P:{percentage}%"

    Debe USAR las funciones count_vowels, count_consonants, total_letters y vowel_percentage.

    Ejemplo: analyze_text("hola") → "V:2 C:2 T:4 P:50.0%"
    """
    V = count_vowels(text)
    C = count_consonants(text)
    T = total_letters(text)
    P = vowel_percentage(text)

    return f"V:{V} C:{C} T:{T} P:{P}%"
