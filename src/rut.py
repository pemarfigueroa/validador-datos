def calcula_dv(rut):
    rut_aux = int(rut)
    i = 2
    suma_rut = 0
    while rut_aux > 0:
        digito = rut_aux % 10
        suma_rut += digito * i
        rut_aux //= 10
        if i == 7:
            i = 2
        else:
            i += 1
    dv_aux = suma_rut % 11
    if dv_aux == 1:
        dv = 'K'
    elif dv_aux == 0:
        dv = '0'
    else:
        dv = str(11 - dv_aux)
    return dv


def valida_DV(rut, dv):
    dv_aux = calcula_dv(rut)
    dv_rut = str(dv).upper().strip()
    valido = (dv_aux == dv_rut)
    return valido


if __name__ == "__main__":
    rut1 = valida_DV(55331, 'K')
    print(rut1)
    rut1 = valida_DV(55331, 'k ')
    print(rut1)
    rut1 = valida_DV(57346, 9)
    print(rut1)
    rut1 = valida_DV(57346, '8 ')
    print(rut1)
    rut1 = valida_DV("0000057346", "9")
    print(rut1)
