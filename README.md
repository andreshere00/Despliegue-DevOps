# script1-pc2

Script para automatizar el proceso de despliegue de aplicación monoltica sobre MV pesada. 

Despliegue de la aplicación en máquina virtual pesada  (2 puntos) 
En  esta  parte,  se  utilizarán  las  técnicas  más  tradicionales,  que  consisten  en  desplegar  la 
aplicación como si fuese un monolito, en una o varias máquinas virtuales pesadas.  
Para ello deberá programar un script en lenguaje Python que sea capaz de realizar una de las 
siguientes instalaciones:

• Instalación de la aplicación en una máquina virtual pesada alojada en la infraestructura 
de google cloud. 
• Instalación de la aplicación en los servidores s1 a s3 de la práctica creativa 1.  

En el directorio bookinfo/src/productpage se encuentra el código de una aplicación que 
muestra la información sobre libros escrita en Python. Esta aplicación se ejecuta llamando al 
fichero productpage_monolith.py y especificando el puerto en el que queremos que la 
aplicación reciba las peticiones (puerto 9080).  Previamente se deben instalar, usando pip, 
las dependencias especificadas en el fichero requirements.txt. 
 
• Se pide inspeccionar el código de la aplicación para que en el título aparezca el 
nombre del grupo que está realizando la práctica. Este valor deberá obtenerse por 
medio  de  la  variable  de  entorno  <GROUP_NUMBER>.  También  deberá  arrancar  la 
aplicación en un puerto diferente al predeterminado. 
 
• Se requiere que la aplicación sea accesible desde el exterior por medio de la IP pública 
que tenga asignada la VM, por ejemplo: 
 http://<ip-publica>:<puerto>/productpage
