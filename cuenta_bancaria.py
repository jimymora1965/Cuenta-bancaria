class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance= 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre}, {self.apellido}\nBalance de cuenta {self.numero_cuenta}: {self.balance}"
    
    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Cantidad depositada")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")


def crear_cliente():
    nombre_cliente = input("Ingrese nombre")
    apellido_cliente = input("Ingrese el apellido")
    numero_cueta = input("Ingrese numero de cuenta")
    cliente = Cliente(nombre_cliente, apellido_cliente, numero_cueta)
    return cliente

def inicio():
    nuevo_cliente = crear_cliente()
    print(nuevo_cliente)
    opcion = 0

    while opcion != 'S':
        print("Elige: Depositar (D), Retirar (R), Salir (S)")
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input("Monto a depositar: "))
            nuevo_cliente.depositar(monto_dep)
        elif opcion == "R":
            monto_ret = int(input("Monto a retirar"))
            nuevo_cliente.retirar(monto_ret)
        print(nuevo_cliente)

    print("Gracias")

inicio()
        

    
        

    
    




