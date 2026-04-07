monto = 100000
control = 0


def consultar():
    print("SU SALDO ACTUAL ES DE:", monto)


def retirar():
    global monto
    retiro = int(input("CUANTO ES EL MONTO QUE DESEA RETIRAR: "))
    
    if retiro > monto:
        print("FONDOS INSUFICIENTES")
    else:
        monto -= retiro
        print("SU MONTO ACTUAL ES DE:", monto)


def depositar():
    global monto
    deposito = input("INDIQUE CUENTA A LA CUAL DEPOSITAR: ")
    envio = int(input("INDIQUE EL MONTO A DEPOSITAR: "))
    
    monto += envio
    print("SU MONTO ACTUAL ES DE:", monto)


def salir():
    global control
    control = 1
    print("GRACIAS POR USAR NUESTRO CAJERO AUTOMATICO POPULAR")


while control == 0:
    optiones = int(input(
        "\nBIENVENIDO A TU CAJERO AUTOMATICO POPULAR\n"
        "==================================================\n"
        "1. CONSULTAR SALDO\n"
        "2. RETIRAR DINERO\n"
        "3. DEPOSITAR DINERO\n"
        "4. SALIR\n"
        "==================================================\n"
        "ELIGE UNA OPCION: "
    ))

    if optiones == 1:
        consultar()
    elif optiones == 2:
        retirar()
    elif optiones == 3:
        depositar()
    elif optiones == 4:
        salir()
    else:
        print("OPCION NO VALIDA")