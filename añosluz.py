"""
Este programa calcula la distancia a la que está un objeto en años luz tenieendo cuenta el medio.

El ejemplo puede ser absurdo ya que no hay un universo de agua, pero quermos demostrar que el medio influye en la velocidad de la luz.
"""


#Definimos las velocidades de la luz en distintos medios
luz_vacio = 299792    
luz_agua = 224844
luz_aire = 299708

#Definimos la fórmula para calcular la velocidad de la luz segun el medio.
def calc_luz(velocidad_medio,kilom_in):      
        añosluz = (kilom_in/(velocidad_medio*365.25*86400))
       
        return añosluz   

   
#Introducimos al usuario al ejemplo hipotetico
print("Buenas tardes, vamos a calcular la distancia en años luz de diferentes objetos,")


try:
 #Le proponmos los tres casos y que decida el usuario uno de ellos
 pregunta = float(input("Introduce el medio por el que se propaga la luz de la distancia que quieres medir (1=vacío, 2=agua, 3=atmósfera): "))

 kilom_in=float(input("Introduce a que distancia está el objeto en kilómetros "))

except:
 print("Algún dato está mal, inténtalo de nuevo, por favor.")  
 pregunta = float(input("Introduce el medio por el que se propaga la luz de la distancia que quieres medir (1=vacío, 2=agua, 3=atmósfera): "))

 kilom_in=float(input("Introduce a que distancia esta el objeto en kilómetros "))



#Definimos lo que puede pasar en cada una de las opciones
if pregunta == 1:
    velocidad_medio = luz_vacio
   
elif pregunta == 2:

    velocidad_medio = luz_agua

elif pregunta == 3:

    velocidad_medio = luz_aire
    
    
distancia_luz = calc_luz(velocidad_medio,kilom_in)
    
print("Tu objto se situa a:",distancia_luz,"años luz")
    








