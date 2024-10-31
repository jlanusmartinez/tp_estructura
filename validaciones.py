def validar_numero_telefono(numero):
    # Verificaa que el numero tiene exactamente 10 caracteres y que todos sean digitos
    if len(numero) == 10 and numero.isdigit():
        return True
    return False
