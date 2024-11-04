def validar_numero_telefono(numero):
    # Verifica que el numero tiene exactamente 10 caracteres y que todos sean digitos
    if len(numero) == 10 and numero.isdigit():
        return True
    return False

def validar_codigo_telefono(codigo):
    # Verificar que el codigo tiene 4 digitos y coincide con el codigo correcto
    if len(codigo) == 4 and codigo.isdigit():
        return True
    return False

def validar_id_unico(id_unico, conj_ids):
    # Verificar que el ID no esta repetido
    if id_unico in conj_ids:
        return False
    return True