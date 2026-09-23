# WEB SCRAPING SCRIPT

```text
 __        __     _     ____                               
 \ \      / /__ _| |__ / ___|  ___ _ __ __ _ _ __   _ __   ___ _ __ 
  \ \ /\ / / _ \ | '_ \\___ \ / __| '__/ _` | '_ \ | '_ \ / _ \ '__|
   \ V  V /  __/ | |_) |___) | (__| | | (_| | |_)  | |_) |  __/ |   
    \_/\_/ \___|_|_.__/|____/ \___|_|  \__,_| .__/  .__/  \___|_|   
                                            |_|    |_|           
```

**Script en Python diseñado para realizar web scraping automáticamente y
extraer datos de una página web específica.**

---

## El problema que resuelve

Recopilar información de páginas web manualmente puede resultar lento y
repetitivo, especialmente cuando es necesario obtener una gran cantidad de
datos.

Este proyecto automatiza ese proceso mediante **web scraping**, permitiendo
extraer información de páginas web para utilizarla posteriormente en análisis
de datos, desarrollo de productos, investigación de mercado, generación de
leads, entre otros usos.

## ¿Qué es Web Scraping?

El **web scraping** es una técnica utilizada para extraer información de
sitios web.

En lugar de recopilar los datos manualmente, un script puede realizar
peticiones a una página, obtener su contenido HTML y analizarlo para extraer
la información necesaria.

---

## Cómo funciona

Este script de Python utiliza varias librerías para realizar el proceso de
web scraping.

| Librería           | Función                                                               |
| ------------------ | --------------------------------------------------------------------- |
| **Beautiful Soup** | Analiza documentos HTML y XML y permite extraer información de ellos. |
| **Requests**       | Realiza peticiones HTTP para obtener el contenido de una página web.  |
| **Pandas**         | Permite organizar y procesar los datos extraídos.                     |

### Beautiful Soup

**Beautiful Soup** es una librería de Python utilizada para extraer datos de
archivos HTML y XML.

Permite analizar estos documentos y generar un árbol de elementos que facilita
la búsqueda y extracción de información concreta de una página web.

### Requests

**Requests** es una librería de Python que permite realizar peticiones HTTP
de forma sencilla.

En este proyecto se utiliza para obtener el contenido HTML de la página web
que posteriormente será analizado mediante Beautiful Soup.

### Pandas

**Pandas** permite organizar y manipular los datos obtenidos durante el
proceso de scraping, facilitando su posterior análisis o almacenamiento.

---

## Primeros pasos

### Requisitos

Antes de ejecutar el script necesitas tener instalado:

* **Python**
* **pip**
* Una **conexión a Internet**

Las librerías necesarias son:

* Beautiful Soup
* Requests
* Pandas

### Instalación

Puedes instalar las dependencias mediante `pip`:

```bash
pip install bs4
pip install requests
pip install pandas
```

También puedes instalar todas las dependencias de una sola vez:

```bash
pip install bs4 requests pandas
```

---

## Cómo ejecutar el script

Una vez instalado Python y las librerías necesarias, abre una terminal dentro
de la carpeta del proyecto y ejecuta:

```bash
python index.py
```

El script comenzará el proceso de scraping y extraerá los datos de la página
web configurada.

---

## ¿Qué obtienes?

Al ejecutar el script obtendrás los **datos extraídos automáticamente de la
página web configurada**.

El resultado puede utilizarse posteriormente para:

* Análisis de datos.
* Investigación de mercado.
* Desarrollo de productos.
* Recopilación de información.
* Automatización de tareas.
* Generación de datasets.

El formato final de los datos dependerá de cómo esté configurado el script.

---

## Estructura del proyecto

La estructura proyecto sería:

```text
.
├── index.py
└── README.md
```

### `index.py`

Contiene el código Python encargado de realizar las peticiones HTTP, analizar
el contenido de la página y extraer los datos.

### `README.md`

Contiene la documentación necesaria para instalar y utilizar el proyecto.

---

## Preguntas frecuentes

**¿Necesito tener Python instalado?**

Sí. El script está desarrollado en Python, por lo que necesitas tener Python
instalado en tu sistema.

**¿Necesito instalar las librerías manualmente?**

Sí. Antes de ejecutar el script debes instalar las dependencias necesarias
mediante `pip`.

```bash
pip install bs4 requests pandas
```

---

## Uso responsable

Antes de realizar web scraping sobre cualquier sitio web, revisa sus
**Términos de Uso** y respeta las reglas establecidas por el propietario del
sitio.

No todas las páginas web permiten realizar scraping y algunas pueden imponer
restricciones sobre los datos que pueden recopilarse o sobre la frecuencia de
las peticiones.

Además, evita realizar un número excesivo de solicitudes en poco tiempo, ya
que podrías sobrecargar el servidor y afectar al funcionamiento del sitio web
o de otros usuarios.

> **Uso responsable:** utiliza esta herramienta respetando los términos,
> políticas y restricciones aplicables al sitio web que estés consultando.

---

## Aviso legal

Este proyecto se proporciona **"tal cual"**, sin garantías de ningún tipo.

El usuario es responsable de asegurarse de que el uso del script cumple con
las condiciones de uso, políticas y legislación aplicables a los sitios web
sobre los que se utilice.

---

**Proyecto:** Web Scraping Script
