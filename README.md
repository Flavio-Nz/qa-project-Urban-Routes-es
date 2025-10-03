# Proyecto Sprint 9 - Automatización de pruebas de la aplicación web

Este proyecto consiste en la automatización de pruebas para la página Urban Routes, centradas específicamente en la
funcionalidad para pedir un taxi. 

Las pruebas incluídas son las siguientes:

1.- Configurar la ruta.

2.- Seleccionar la tarifa Comfort.

3.- Rellenar el número de teléfono.

4.- Agregar una tarjeta de crédito. 

5.- Escribir un mensaje para el controlador.

6.- Pedir una manta y pañuelos.

7.- Pedir 2 helados.

8.- Visualizar el modal para buscar un taxi.

9.- Esperar a que aparezca la información del conductor en el modal.

El proyecto contenido dos archivos, el archivo data.py y el archivo main.py. En el archivo data.py se encuentran 
almacenadas todas las variables con los datos necesarios para pedir un taxi, como las direcciones, teléfono y método de pago.

Mientras que en el archivo main.py se encuentra todo el código necesario para llevar a cabo las pruebas: este se divido 
en dos partes, la primera es la clase UrbanRoutesPage, la cual contiene todos los localizadores necesarios y los métodos
que se deben usar para las pruebas.

Mientras que en la clase TestUrbanRoutes se encuentran las pruebas en sí, con las validaciones respectivas.

## Consieraciones especiales

Para ejecutar las pruebas es necesario reiniciar el servidor y luego copiar la URL 
actualizada en el atributo urban_routes_url del archivo data.py


## Tecnologías utilizadas

Para este proyecto se utilizó el IDE Pycharm, además del lenguaje de programación Python y el framework de Selenium para 
las pruebas automatizadas.

El código se almacenó en el repositorio qa-project-Urban-Routes-es de Github.

##  Requisitos previos

Asegúrate de tener instalado:
- [Python 3.9+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://chromedriver.chromium.org/) (versión compatible con tu navegador)