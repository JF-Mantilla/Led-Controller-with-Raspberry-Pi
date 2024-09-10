# Cargar imagenes provenientes de una carpeta
# Pretecor SAS

import cv2
import numpy as np


img = cv2.imread('images/1.jpg') #Lee la imagen de la carpeta images

b,g,r = cv2.split(img)  #Separa sus componentes RGB, genera tres matrices con el tamaño de la imagen


#Exportar matrices a carpeta txt_files

np.savetxt("txt_files/img1_b.txt",b,fmt='%d')
np.savetxt("txt_files/img1_g.txt",g,fmt='%d')
np.savetxt("txt_files/img1_r.txt",r,fmt='%d')

print("Export ok ")

# - - - Mostrar imagen - - -
#cv2.imshow('blue',b)
#cv2.imshow('green',g)
#cv2.imshow('red',r)
#cv2.waitKey(0)
#cv2.destroyAllWindows