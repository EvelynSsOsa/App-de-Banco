# 🏦 App de Banco

> Pequeña aplicación web desarrollada con **Streamlit** que permite la gestión de cuentas bancarias, realizar depósitos y retiros de forma sencilla e intuitiva.

---

## ✨ Funcionalidades

| Función | Descripción |
|---------|-------------|
| 🌸 **Consultar historial** | Visualiza todos los movimientos con fecha y hora exacta |
| 🌸 **Creación de usuarios** | Registra nuevos usuarios en el sistema |
| 🌸 **Retiro** | Realiza retiros de tu cuenta |
| 🌸 **Depósito** | Realiza depósitos a tu cuenta |
| 🌸 **Consulta de saldo** | Verifica tu saldo disponible en todo momento |
| 🌸 **Persistencia de datos** | Los datos se guardan en archivos JSON |

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Descripción |
|------------|-------------|
| 🐍 **Python** | Lenguaje de programación principal |
| 🎈 **Streamlit** | Framework para la interfaz gráfica |
| 🐼 **Pandas** | Manipulación y análisis de datos |
| 📦 **JSON** | Almacenamiento persistente de datos |
| 🧬 **POO** | Programación Orientada a Objetos |

---

## 🌟 Características destacadas

| Característica | Descripción |
|----------------|-------------|
| 🪷 **Interfaz moderna** | Estilo fintech (prototipo) |
| 🪷 **Diseño responsivo** | Se adapta a diferentes dispositivos |
| 🪷 **Tarjetas visuales** | Muestran información del usuario de forma atractiva |
| 🪷 **Formato de dinero** | Estilo banco: `$2,500.00` |
| 🪷 **Inputs interactivos** | Para ingreso de montos en depósitos y retiros |
| 🪷 **Session State** | Manejo de estado con Streamlit |
| 🪷 **Persistencia JSON** | Datos guardados en archivos JSON |

---

## 📁 Estructura del proyecto
📦 App-de-Banco/
│
├── 📄 CuentaBanco.py # Lógica de la cuenta bancaria (POO)
├── 📄 CuentaBancoInterfaz.py # Interfaz de usuario con Streamlit
├── 📄 usuarios.json # Base de datos de usuarios
├── 📁 .streamlit/
│ └── 📄 config.toml # Configuración de Streamlit
└── 📄 README.md # Documentación del proyecto 



---

## 🖼️ Vista previa de la aplicación

A continuación, te muestro cómo se ve el banco digital en funcionamiento:

---

### 💐 Saldo inicial del usuario

Pantalla principal mostrando el **saldo inicial** de la cuenta.

<p align="center">
  <img width="700" alt="Saldo inicial" src="https://github.com/user-attachments/assets/8dedd80f-6501-4fe0-9f93-de6116870402" />
</p>

---

### 💐 Realizando un depósito

Interfaz interactiva para **ingresar montos** y realizar depósitos.

<p align="center">
  <img width="700" alt="Realizando depósito" src="https://github.com/user-attachments/assets/7b349bf1-6223-42b9-aad6-66e6aa53b362" />
</p>

---

### 💐 Consultar saldo después del depósito

Verificamos el **nuevo saldo** después de haber realizado un depósito.

<p align="center">
  <img width="700" alt="Saldo después del depósito" src="https://github.com/user-attachments/assets/9506381c-328d-4e91-be3b-b6b1480d762b" />
</p>

---

### 💐 Realizando un retiro

Interfaz para **realizar retiros** de la cuenta bancaria.

<p align="center">
  <img width="700" alt="Realizando retiro" src="https://github.com/user-attachments/assets/ba3f184b-0007-491c-ad3b-48170c5621d7" />
</p>

---

### 💐 Saldo restante después del retiro

Consultamos el **saldo actualizado** después de haber realizado un retiro.

<p align="center">
  <img width="700" alt="Saldo después del retiro" src="https://github.com/user-attachments/assets/d2231e56-9f43-4d42-b6d5-f780b35516ee" />
</p>

---

### 💐 Historial de movimientos

Visualización completa del **historial de transacciones** con fecha y hora.

<p align="center">
  <img width="700" alt="Historial de movimientos" src="https://github.com/user-attachments/assets/997bbb4e-9b6c-40b1-9e7a-847336de0add" />
</p>

---

## 📌 Nota

> Todas las imágenes fueron capturadas durante la ejecución real de la aplicación.  
> El diseño es un **prototipo estilo fintech** y puede seguir evolucionando.

--- 
## Este proyecto fue creado con mucho esfuerzo para simular la gestión de una cuenta bancaria de manera didáctica y visual.


## 🚀 Cómo ejecutar el proyecto

```bash
# Clona el repositorio
git clone https://github.com/tu-usuario/App-de-Banco.git

# Entra al directorio
cd App-de-Banco

# Instala las dependencias
pip install streamlit pandas

# Ejecuta la aplicación
streamlit run CuentaBancoInterfaz.py







