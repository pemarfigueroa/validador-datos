from rut import calcula_dv
import random
import os


def random_rut():
    rut = random.randint(1000000, 25000000)
    dv = calcula_dv(rut)
    rut_str = str(rut).zfill(12) + dv
    return rut_str


def random_nombrefem():
    nombres = ["Maria", "Sofia", "Valentina", "Lucia", "Camila", "Gabriela", "Daniela", "Isabel", "Valeria",
               "Victoria", "Paula", "Claudia", "Martina", "Natalia", "Emilia", "Julia", "Alba", "Patricia"]
    nombre = (random.choice(nombres)).ljust(30).upper()
    return nombre


def random_nombremasc():
    nombres = ["Martin", "Pablo", "Cesar", "Vicente", "Valentin", "Ignacio", "Victor", "Antonio", "Agustin", "Tomas",
               "Pedro", "Adriano", "Leo", "Marcelo", "Benicio", "Fabrizio", "Fabian", "Emiliano", "Luciano", "Felipe", "Francisco"]
    nombre = (random.choice(nombres)).ljust(30).upper()
    return nombre


def random_apellido():
    apellidos = ["CANALES", "VERGARA", "MUNILLA", "RIQUELME", "CABRALES", "HARCHA", "BRUNOS", "PUEBLA", "BONTA", "GONZALEZ",
                 "RETAMAL", "VENEGAS", "YEVENES", "HUILI", "PAINIQUEO", "FIGUEROA", "JACOB", "SAN MARTIN", "FLORES", "ZAPATA"]
    apellido = (random.choice(apellidos)).ljust(30)
    return apellido


def random_saldo():
    saldo = str(random.randint(1000000, 2500000000)).zfill(15)
    return saldo


def random_fecha():
    year = random.randint(1986, 2026)
    month = random.randint(1, 12)
    day = random.randint(1, 31)
    if (year % 4) == 0:
        if month == 2 and day > 29:
            day = 29
    elif month == 2 and day >= 29:
        day = 28

    if month in (4, 6, 9, 11) and day > 30:
        day = 30
    fecha = str(year) + str(month).zfill(2) + str(day).zfill(2)
    return fecha


def armar_linea(rut, nombre, apellido_pat, apellido_mat, saldo, fecha):
    linea = rut + nombre + apellido_pat + apellido_mat + saldo + fecha
    return linea


if __name__ == "__main__":
    cant_reg = int(input("¿Cuantos registros desea en el archivo: "))
    gender = ["M", "F"]
    with open("../datos/cotizantes.txt", "w", encoding="latin-1", newline="") as archivo:
        for i in range(cant_reg):
            genero = random.choice(gender)
            rut = random_rut()
            if genero == "M":
                nombre = random_nombremasc()
            else:
                nombre = random_nombrefem()
            appat = random_apellido()
            apmat = random_apellido()
            saldo = random_saldo()
            fecha = random_fecha()
            linea = armar_linea(rut, nombre, appat, apmat, saldo, fecha)
            archivo.write(linea + "\n")
    archivo.close()
