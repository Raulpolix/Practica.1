    #Definimos las veelocidades de la luz en distintos medios
luzvacio = 299792    
luzagua = 224844
luzaire = 299708
   
    #Introducimos al usuario al ejemplo hipotetico
print("Buenas tardes, vamos a calcular la distancia en años luz de diferentes objeetos,")

    #Le proponmos los tres casos y que decida el usuario uno de ellos
pregunta = float(input("Introduce el medio por el que se propaga la luz de la distancia que quierees medir (1=vacio, 2=agua, 3=atmosfera): "))
   
    #Definimos lo que pude pasar en cada una de las opciones
if pregunta > 0 and pregunta < 2:
    
    def calc_luzvacio(kilometros):      #Formula para el medio "vacio"
        añosluz = (kilometros/(luzvacio*365.25*86400))
       
        return añosluz   
      
       #Introducimos los kilometros de separacion con el objto
    kilom_in=float(input("Introduce a que distancia esta el objeto en cuestion "))

    luzvacio_calc= calc_luzvacio(kilom_in)
    print("Tu objeto está a :",luzvacio_calc,"Años luz")
    
elif pregunta >1 and pregunta <3:

    def calc_luzagua(kilometros):   #Formula para el medio "agua"
        añosluz = (kilometros/(luzagua*365.25*86400))
       
        return añosluz
    
             #Introducimos los kilometros de separacion con el objto
    kilom_in=float(input("Introduce a que distancia esta el objeto en cuestion "))

    luzagua_calc= calc_luzagua(kilom_in)
    print("Tu objeto está a :",luzagua_calc,"Años luz")

else:
    def calc_luzaire(kilometros):   #Formula para el medio "aire"
        añosluz = (kilometros/(luzaire*365.25*86400))
       
        return añosluz
    
             #Introducimos los kilometros de separacion con el objto
    kilom_in=float(input("Introduce a que distancia esta el objeto en cuestion "))

    luzaire_calc= calc_luzaire(kilom_in)
  
    print("Tu objeto está a :",luzaire_calc,"Años luz")







