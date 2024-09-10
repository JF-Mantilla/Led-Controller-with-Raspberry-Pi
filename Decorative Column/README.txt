Este programa permite crear las matrices RGB de una imagen usando librerias de OpenCV
Usa un entorno virtual donde está instalada la libreria de Open OpenCV

== Para exportar las matrices que se cargan a la raspberry debe: == ==
1 . guardar la imagen en la carpeta "images", con el tamaño correspondiente
2 . En el archivo run.py, linea 8 debe cambiar el nombre de la imagen por la que se quiere leer


== Pasos para instalar OpenCV: ==

1. Instalar Python 3.9: www.python.org >>> download
2.  Instalar Virtual Environment 
   > pip install virtualenv 
   > pip install virtualenvwrapper-win
3.  Crear entorno virtual (pretecor)
   >  mkvirtualenv pretecor
4. Validar intalación
   > python
   > import cv2
   > print(cv2.__version__)


En el desarrollo de este programa se uso Visual Studio Code. Se debe comprobar que se esté trabajando
sobre el entorno virtual


 == Git Help ==

 A través del terminal o consola verificamos Git
   > git version

Si es primera vez usamos:
   >  git init

Esto crea un nuevo repositorio.
Hasta este punto los archivos inicializados no tienen seguimiento.

Enviar los archivos al area temporal y quedan pendientes a cambios (Pre-envio):
   > git add .

Creamos copia del proyecto:
   > git commit -m "escriba comentario aqui"

Subir a servirdor de Git (github):
> git remote add origin https://github.com/JuanF3/Pretecor-DECO-RPI.git
> git branch -M main
> git push -u origin main

Puede que le pida usuario y contraseña la primera vez

Nota: 
- Siempre que se modifica un archivo es necesario primero > add . y luego > commit -m " "
- git status -s muestra la lista de los archivo modificado o pentientes por subir
- > git log --oneline muestra la lista de copias realizadas
- git si se quiere regresar a una copia antigua se usa > git reset --hard (header aqui,por ejemplo, ab1c548)



