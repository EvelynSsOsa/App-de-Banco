class Persona():
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance=2500):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance ## es el dinero que va a tener en su cuenta por defecto

    def depositar(self):
        deposito= int(input("¿Cúanto dinero desea depositar?"))
        self.balance += deposito
        return f'Operación exitora!! \n Usted a depositado: ${deposito} \n Su saldo total es de: ${self.balance}'

    def retiro(self):
        while True:
            retirar = int(input("¿Cúanto dinero desea retirar?"))
            if retirar > self.balance:
                print("Lo sentimos,no cuentas con los fondos suficientes \n ")
            else:
                self.balance -= retirar
                return f'Operación exitosa!! \n el saldo total es de {self.balance} \n usted a retirado $ {retirar} en total'

    def __str__(self):
        return f'El nombre del usuaio es: {self.nombre} {self.apellido}, y tiene un total de {self.balance} fondos en su ceunta'
## aqui tenemos un  metodo que nos ayuda a poder imprimir los atributos de instancia, y para poder
## ver estos atributos de instancia es necesario, crear una instancia de esta misma clase
## e impirmir la instancia... con eso podremos ver en pantalla el retorno de esta función/metodo especial


## aquí termina la clase cliente



## fuera de la clase cliente
def crear():
    print("\n Necesitamos identificar nuestro cliente, para ello ayudamos contestando a lo siguiente: ")
    nom = input("\n Ingrese su nombre: ")
    ape = input("\n Ingrese su apellido: ")
    nu_cuenta = input("\n Ingrese su numero de cuenta: ")
    usuario = Cliente(nom, ape, nu_cuenta)
    return usuario

usuario = None ## 1ero declaramos a la instancia de la función y la inicializamos en "None"

def iniciar(usuario):
    while True:
        print('Bienvenido a tu cuenta de banco \n')
        print('Por donde quieres comenzar?')
        print('\n 1.-Crear cuenta de banco')
        print('\n 2.-Consultar saldo')
        print('\n 3.-Depositar saldo')
        print('\n 4.-Retiro de efectivo')
        print('\n 5.- Salir de la app')
        elec = int(input('Elige una opción:'))
        if elec == 1:## al no tener cuenta creada, solo mandamos a llamar a la función crear
            usuario = crear()## por medio de la instancia "usuario"
            #return usuario

        elif elec == 2:
            if usuario == None: ## en dado caso de haber seleccionado la opción 2 y no tener una cuenta aun
                usuario = crear()## creamos una cuenta
                print(usuario)## y ya luego mostramos el saldo actual
            else:  ## suponiendo que ya se ha iniciado sesión
                print(usuario)
            #return usuario

        elif elec == 3:
            if usuario == None:
                usuario = crear()
                print(usuario.depositar())
            else:
                print(usuario.depositar())
            #return usuario

        elif elec == 4:
            if usuario == None:
                usuario = crear()
                print(usuario.retiro())
            else:
                print(usuario.retiro())
            #return usuario

        elif elec == 5:
            re = input("¿Quieres salir de la app? s/n: ")
            if re == "si":
                print("Adios!!")
                return usuario

        else:
            print("Esa opción no es valida o no existe")


usuario = iniciar(usuario)













