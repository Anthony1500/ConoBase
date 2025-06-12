<p align="center">
  <img src="images/logo_app.png" alt="ConoBase Logo" width="200">
</p>

# ConoBase

**ConoBase** es una aplicación de escritorio escrita en **Python 3** que permite
administrar y consultar categorías y subcategorías de conocimiento de manera sencilla.  
Utiliza una interfaz gráfica basada en **Qt** y gestiona los datos en archivos de texto plano.

## Características

- Creación, búsqueda y eliminación de categorías.
- Manejo de subcategorías asociadas a cada categoría.
- Almacenamiento local en archivos de texto (`recursos/`), fácil de editar y respaldar.
- Interfaz moderna basada en un `QStackedWidget` con múltiples pantallas.
- Tema oscuro opcional gracias a `qdarkstyle`.
- Navegación fluida entre categorías y subcategorías.
- Delegados personalizados para mejorar la interacción con las listas.

## Dependencias

- Python 3.10 o superior.
- [PyQt5](https://pypi.org/project/PyQt5/)
- [qdarkstyle](https://pypi.org/project/qdarkstyle/)

## Instalación

### Recomendación

Se recomienda crear un **entorno virtual** (`.venv`) para aislar las dependencias del proyecto y evitar conflictos con otros proyectos de Python.

### Preparar entorno virtual e instalar dependencias

Ejecute los siguientes comandos desde la raíz del proyecto (`ConoBase/`):

```bash
# Crear el entorno virtual
python -m venv .venv

# Activar el entorno virtual
# En Windows CMD:
.venv\Scripts\activate

# En PowerShell:
.venv\Scripts\Activate.ps1

# Instalar las dependencias necesarias (incluye PyQt5 y qdarkstyle)
pip install -r requirements.txt
```
## Ejecución 

Para iniciar la aplicación ejecute:
``` bash
python main.py
```
El programa abrirá una ventana principal donde podrá crear nuevas categorías,
consultar las existentes y gestionar subcategorías.

## Estructura del proyecto

ConoBase/
├── main.py                      # Archivo principal con la lógica de la interfaz (1400+ líneas).
├── ui/                          # Formularios de Qt (.ui) y  generadas en QT Designer.
├── requirements.txt             # Lista de dependencias del proyecto.
├── images/                      # Iconos e imágenes utilizados en la GUI (incluye logo_app.png).
└── recursos/                    # Archivos de texto donde se guardan las categorías.

