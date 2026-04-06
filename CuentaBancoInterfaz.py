## este script es para la interfaz con streamlit

import streamlit as st
import json
from datetime import datetime
import pandas as pd

## configuración de la pagina:
st.set_page_config(
    page_title = "Cuenta de Banco",
    page_icon = "💳",
    layout = "wide"
)

st.markdown("""
<style>
.stButton>button {
    background-color: #FF6B00;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
} 
.stButton>button:hover {
    background-color: #ff8c1a;
}
</style>
""", unsafe_allow_html=True)




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
        deposito = st.number_input("¿Cuánto quieres depositar?", min_value=0)
        if st.button("Hacer Deposito 💰", key = 'btn_deposito'):
            if deposito <= 0:
                st.warning("Lo sentimos, pero no fue posible realizar tu deposito \n")
            else:
                self.balance += deposito
                actualizar_usuario(self)
                st.session_state.movimientos.append({
                    "Tipo": "Deposito",
                    "Monto": deposito,
                    "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
                })
                st.success(f'Operación exitora!! \n Usted a depositado: ${deposito:,.2f} \n Su saldo total es de: ${self.balance:,.2f}')
                st.rerun()


    def retiro(self):
        retirar = st.number_input("¿Cúanto dinero desea retirar?", min_value=0)
        if st.button("Hacer retiro 💸", key = 'btn_retirar'):
            if retirar <= 0:
                st.warning("Ingrese un monto valido")
            elif retirar > self.balance:
                st.error("Lo sentimos,no cuentas con los fondos suficientes")

            else:
                self.balance -= retirar
                actualizar_usuario(self)
                st.session_state.movimientos.append({
                    "Tipo": "Retiro",
                    "Monto": retirar,
                    "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
                })
                st.success(f'Operación exitosa!! \n el saldo total es de {self.balance:,.2f} \n usted a retirado $ {retirar:,.2f} en total')
                st.rerun()

    def __str__(self):
        return f'El nombre del usuaio es: {self.nombre} {self.apellido}, y tiene un total de {self.balance:,.2f} fondos en su ceunta'
## aqui tenemos un  metodo que nos ayuda a poder imprimir los atributos de instancia, y para poder
## ver estos atributos de instancia es necesario, crear una instancia de esta misma clase
## e impirmir la instancia... con eso podremos ver en pantalla el retorno de esta función/metodo especial


## aquí termina la clase cliente

def guardar_usuario(usuario):
    try:
        with open("usuarios.json", "r") as f:
                data = json.load(f)
    except:
        data = []

    data.append({
        "nombre": usuario.nombre,
        "apellido": usuario.apellido,
        "cuenta": usuario.numero_cuenta,
        "balance": usuario.balance,
        "movimientos": st.session_state.movimientos
    })

    with open("usuarios.json", "w") as f:
            json.dump(data, f)



## fuera de la clase cliente
def crear():
    st.write("Vamos a crear tu cuenta de banco!!")
    nom = st.text_input("Nombre: ")
    ape = st.text_input("1er Apellido: ")
    nu_cuenta = st.text_input("Ingrese su numero de cuenta: ")
    if st.button("Crear cuenta 💳 😃"):
        usuario = Cliente(nom, ape, nu_cuenta)
        guardar_usuario(usuario)
        st.success("La cuenta ha sido creada con exito!!")
        return usuario
## esta instancia "usuario" -> viene de la función "crear()"
## como estamos usando "streamlit" ya no podemos inicializar la instancia así nadamas
##"usuario = None" -> antes declaramos a la instancia de la función y la inicializabamos en "None"
######AHORA#######
if "usuario" not in st.session_state: ## decimos que si aun no existe ningun usuario
    st.session_state.usuario = None ## que entonces sea creado y que se inicialice en "None"

if "movimientos" not in st.session_state:## aqui decimos que si aun no existe un historial de movimientos en memoria
    st.session_state.movimientos = []## entonces vamos a crear una lista(hitorial) donde podamos guardar movimientos de cuenta

if st.session_state.usuario is None: ## si no hay ningun usuario que haya inciado sesión/ logeado
    st.info("Hola Bienvenido a tu app de banco, para comenzar crea una cuenta")## mostramos esto en pantalla
else: ## si ya esta dentro entonces se muestra esto en pantalla
    st.success("Sesión iniciada")

def actualizar_usuario(usuario_actual):
    try:
        with open("usuarios.json","r") as f:## decimos que vamos a abrir el JSON como "f" -> con f indicamos que lo vamos a usar
            data = json.load(f) ## con "load(f)" decimos que ese archivo lo vamos a transformar en una lista

    except:## esta es una instrucción en dado caso de que no tengamos un archivo
        data = [] ## vamos a crear una lista vacia que se llama "data"

    for user in data: ## decimos que por cada "user"(iterador) que hay dentro de "data":
        ## si cuando "user" esta en "cuenta" contiene algo identico o coincide a lo que tenemos en el parametro "usuario_actual" en "numero de cuenta"
        if user["cuenta"] == usuario_actual.numero_cuenta:
            user["balance"] = usuario_actual.balance## entonces cuando el iterador "user" este en  "balance" se igualara a
            # "usuario_actual.balance"... que es el parametro que pasamos a la función
    with open ("usuarios.json","w") as f: ## despues abrimos el fomrato en modo lectura y lo abrimos como f
        json.dump(data,f) ## y como parametro de "dump", pasamos a la lista data

def iniciar(usuario):

        st.markdown("""
        <h1 style='text-align: center; color: #FF6B00; font-size: 50px; margin-bottom: 0;'>
        💳 Banco Blash
        </h1>
        <p style='text-align: center; color: gray; margin-top: 0;'>
        Tu dinero, pero con seguto 
         </p>
        """, unsafe_allow_html=True)

        st.divider()

        option = st.radio('Por donde quieres comenzar?',[
            "Crear cuenta bancaria 👤", "Consultar saldo 💳❓", "Deposito 💵", "Retiro💸",
            "Movimientos 📊","Salir 🚪🏃🏻‍♂️"
        ])
        ## al no tener cuenta creada, solo mandamos a llamar a la función crear
        ##antes la madabamos a llamar así "usuario = crear()"->  por medio de la instancia "usuario"
        #####AHORA CON STREAMLIT

        if option == "Crear cuenta bancaria 👤":
            nuevo_usuario = crear()
            if nuevo_usuario is not None:
                st.session_state.usuario = nuevo_usuario


        elif option == "Consultar saldo 💳❓":
            if st.session_state.usuario is None: ## en dado caso de haber seleccionado la opción 2 y no tener una cuenta aun
                st.warning("Si aún no tienes cuenta te recomendamos crear una ☝🏼👴🏼")
            else:  ## suponiendo que ya se ha iniciado sesión
                usuario = st.session_state.usuario
                st.markdown('### Información de tu cuenta: ')
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"""
                    <div style="
                        background-color:#1C1F26;
                        padding:20px;
                        border-radius:15px;
                        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
                    ">
                        <h4>👤 {usuario.nombre} {usuario.apellido}</h4>
                        <p>Cuenta: {usuario.numero_cuenta}</p> 
                        <p>💰 Saldo: ${usuario.balance:,.2f}</p>
                    </div>
                    """, unsafe_allow_html=True)

                with col2:
                    st.metric("💳 Saldo disponible", f"${usuario.balance:,.2f}")
            #return usuario

        elif option == "Deposito 💵":
            if st.session_state.usuario is None:
                st.warning("Si aún no tienes cuenta te recomendamos crear una ☝🏼👴🏼")
            else:
                st.session_state.usuario.depositar()
            #return usuario

        elif option ==  "Retiro💸" :
            if st.session_state.usuario is None:
                st.warning("Si aún no tienes cuenta te recomendamos crear una ☝🏼👴🏼")
            else:
                st.session_state.usuario.retiro()
            #return usuario

        elif option == "Movimientos 📊":
            if st.session_state.usuario is None:
                st.warning("Si aún no tienes cuenta te recomendamos crear una ☝🏼👴🏼")
            else:
                if len(st.session_state.movimientos) == 0:
                    st.info("Aún no tienes movimientos")
                else:
                    df = pd.DataFrame(st.session_state.movimientos)
                    st.dataframe(df, use_container_width = True)

        elif option ==  "Salir🚪🏃🏻‍♂️":
            st.session_state.usuario = None
            st.info("Adios!! has salido de tu cuenta ")

        else:
            print("Esa opción no es valida o no existe")

iniciar(st.session_state.usuario)
