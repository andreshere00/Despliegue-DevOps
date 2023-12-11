# Despliegue de una esplicación escalable.

Script para automatizar el proceso de despliegue de aplicación monoltica sobre MV pesada. 

## **Despliegue de la aplicación en máquina virtual pesada  (2 puntos)**
En  esta  parte,  se  utilizarán  las  técnicas  más  tradicionales,  que  consisten  en  desplegar  la 
aplicación como si fuese un monolito, en una o varias máquinas virtuales pesadas.  
Para ello deberá programar un script en lenguaje Python que sea capaz de realizar una de las 
siguientes instalaciones:

- Instalación de la aplicación en una máquina virtual pesada alojada en la infraestructura 
de Google Cloud. 
- Instalación de la aplicación en los servidores s1 a s3 de la práctica creativa 1.  

En el directorio `bookinfo/src/productpage` se encuentra el código de una aplicación que 
muestra la información sobre libros escrita en Python. Esta aplicación se ejecuta llamando al 
fichero `productpage_monolith.py` y especificando el puerto en el que queremos que la 
aplicación reciba las peticiones (puerto `9080`).  Previamente se deben instalar, usando `pip`, 
las dependencias especificadas en el fichero requirements.txt. 
 
- Se pide inspeccionar el código de la aplicación para que en el título aparezca el 
nombre del grupo que está realizando la práctica. Este valor deberá obtenerse por 
medio  de  la  variable  de  entorno `<GROUP_NUMBER>`.  También  deberá  arrancar  la 
aplicación en un puerto diferente al predeterminado. 
 
- Se requiere que la aplicación sea accesible desde el exterior por medio de la IP pública 
que tenga asignada la VM, por ejemplo:

`http://<ip-publica>:<puerto>/productpage`.

Esta parte se ha desarrollado en el script `script1.py`.

## **Segmentación de una aplicación monolítica en microservicios utilizando docker compose (2 puntos)**

Como se comentó anteriormente, la aplicación de esta práctica consta de dos servicios 
desarrollados en Python. Sin embargo, para su puesta en ejecución, se utilizó un único 
contenedor. En esta parte de la práctica se va a utilizar un enfoque orientado a microservicios. 
Para ello, se va a segmentar la aplicación, separando cada servicio para que funcione de 
forma independiente. Además, se van a añadir dos servicios más: `Reviews` y `Ratings`.

Como puede observar en la figura, se va a considerar una aplicación "políglota", donde cada 
uno los microservicios que componen la aplicación está desarrollado en un lenguaje de 
programación distinto. La aplicación se compone de los siguientes microservicios:
- Product Page (python)
- Details (ruby)
- Reviews (Java) - Existen tres versiones de este servicio: la primera muetra las reviews 
sin estrellas, la segunda con estrellas de color negro y la tercera con estrellas de color 
rojo.
- Ratings (NodeJS)

**Se pide:**

- Definir un fichero `Dockerfile` para cada uno de los servicios listados anteriormente.
- Crear las imágenes de cada uno de los servicios de acuerdo al siguiente formato de 
nombre: `<numero_de_grupo>/<nombre_de_microservicio>` (Incluir la creación 
de las tres versiones del servicio de reviews. Para especificar la versión se hace uso 
de la variable de entorno `SERVICE_VERSION` cuyos valores pueden ser `v1`, `v2` o `v3`)
- Definir un fichero docker-compose para desplegar cada uno de los contenedores 
cuyas imágenes fueron creadas anteriormente, recordando mantener las variables de 
entorno correspondientes. El nombre de cada contenedor debe ser definido de 
acuerdo a la siguiente convención `<numero_de_grupo>-<nombre_del_servicio>`. 
Se recomienda fuertemente el uso de volúmenes para ejecutar los ficheros de cada 
uno de los servicios.
- La web debe ser completamente funcional y accesible desde el exterior.
- Asimismo, la web debe funcionar con las tres versiones del microservicio review. Para 
ello, se harán pruebas con cada una de las versiones de dichos contenedores. Sin 
embargo, solo una versión puede estar activo y ejecutándose a la vez
Consideraciones especiales para la definición de los ficheros Dockerfile de cada uno de los 
microservicios:
- **ProductPage:** para este contenedor se debe usar la imagen base de python3, instalar 
las librerías definidas en el fichero requirements.txt y ejecutar el archivo 
productpage.py.
- **Details:**
  - Imagen base a utilizar `ruby:2.7.1-slim`.
  - Copiar el fichero `details.rb` en la ruta `/opt/microservices/` dentro del 
contenedor.
  -  Especificar dos variables de entorno: `SERVICE_VERSION` con valor `v1` y 
`ENABLE_EXTERNAL_BOOK_SERVICE` con valor `true`.
  - Exponer el puerto `9080`.
Ejecutar el fichero `details.rb` usando la instrucción ruby y añadir el puerto 
ex: `["ruby","fichero","puerto"]`.
- **Reviews:**
   - Compilar y empaquetar los ficheros necesarios ejecutando, dentro de la ruta  `src/reviews/reviews-wlpcfg`, el siguiente comando: `docker run --rm -u root -v "$(pwd)":/home/gradle/project -w 
 /home/gradle/project gradle:4.8.1 gradle clean build`.
   - Construir la imagen utilizando el fichero `Dockerfile` alojado en el directorio `src/reviews/reviews-wlpcfg` (Inspeccionar el contenido para asignar bien  las rutas y variables de entorno). No olvidar respetar la convención de nombres de los contenedores.
Al construir el fichero `docker-compose`, añadir la variable de entorno 
`ENABLE_RATINGS=true` para que se muestren los ratings.
- **Ratings:**
  - Imagen base a utilizar `node:12.18.1-slim`.
  - Copiar los ficheros `package.json` y `ratings.js` a la ruta 
`/opt/microservices/ dentro del contenedor`.
  - Especificar la variable de entorno SERVICE_VERSION con valor v1
  - Instalar las dependencias
  - Exponer el puerto 9080
  -  Ejecutar el fichero `ratings.js`, usando la instrucción `node` y añadir el puerto 
ex: `["node","ratings.js","puerto"]`.

Incluya en la memoria de la práctica las diferencias con la versión de un único contenedor. 

Incluir en la memoria la línea del despliegue del docker-compose
