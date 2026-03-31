class cajero:
    def __init__(self):
        self.monto=100000
        
        self.control=0
        while self.control==0:
            self.bienvenidad="BIENVENIDO A TU CAJERO AUTOMATICO POPULAR"
            self.optiones=int(input("INGRESE LA OPERACION QUE DESSE REALIZAR:\n==================================================\n" 
            "1. CONSULTAR SALDO\n" 
            "2. RETIRAR DINERO\n" 
            "3. DEPOSITAR DINERO\n" 
            "4. SALIR\n==================================================\n"))

            
            if self.optiones==1:
                self.consultar()
            elif self.optiones==2:
                self.retirar()
            elif self.optiones==3:
                self.depositar()
            elif self.optiones==4:
                self.salir()
            else:
                print("OPCION NO VALIDA")
        
    

    def consultar(self):
        print("SU SALDO ACTUAL ES DE:",self.monto)
      
    def retirar(self):
        self.retiro=int(input("CUANTO ES EL MONTO QUE DESEEA RETIRAR:"))
        self.monto-= self.retiro
        print("SU MONTO ACTUAL ES DE:",self.monto)

    def depositar(self):
        self.deposito=input("INDIQUE CUENTA A CUAL DEPOSITAR:")
        self.envio=int(input("INDIQUE EL MONTO A DEPOSITAR:"))
        self.monto-= self.envio
        print("SU MONTO ACTUAL ES DE:",self.monto)

    def salir(self):
        self.control=1
        print("GRACIAS POR USAR NUESTRO CAJERO AUTOMATICO POPULAR")


ca=cajero()


