print ("Como hacer una taza de cafe")
print("Antes de empezar, ver si tenemos los siguientes elementos")
print  ("3 Sobre de cafe \n 150mL de agua \n Una cantina \n para calentar el cafe \n 1 vaso de su preferencia \n 1 cuchara para revolver los ingredientes")
print ("¿Ya tiene los ingredientes?")
ingredientes= input () .lower()
if ingredientes == "si":
    print ("Sigue con el siguiente paso \n ¿Tiene estufa de gas?")
    estufa= input () .lower()
    if estufa == "si":
        print ("Seguir la siguiente instrucciones")
        print ("Prender la estufa y calentar los 150mL, despues en un vaso de su preferencia, con una cuchara comenzamos a revolver los ingredientes")
        print ("¿Siguio las instrucciones?")
        instrucciones = input () .lower()
        if instrucciones == "si":
            print ("¿Quieres azucar?") 
            azucar = input () .lower()
            if azucar== "si":
                print("agregar 2 o 4 cucharas de azucar y revolver para implementar el ingrediente al cafe")
                print ("Termino tu proceso")
                print ("Disfruta tu cafe<3")
                texto = "Gracias por seguir los pasos"
                letrero = ((texto))
                print(letrero)
            else:print ("Termino tu proceso, \n Disfruta tu cafe<3" ) 
        else: print ("seguir las instrucciones para que pueda disfrutar de su cafe")
    else: print ("Tiene 2 opciones, tomarselo frio o conseguir una estufa")
else: print("Comprar los ingredientes que le falta para poder continuar nuevamente")     