print ("Como preparar un embrion frito (huevo frito)")
print ("Tener los siguientes ingredientes")
print ("Aceite \nSal \n3 o mas huevos, depende el hambre que tenga \n1 sarten para fritar el huevo")
print ("¿Ya tiene todos los ingredientes anteriormente mencionados?")
ingredientes = input () .lower()
if ingredientes == "si":
    print ("Podemos continuar")
    print ("¿Tiene estufa?")
    estufa = input () .lower()
    if estufa== "si":
        print ("1-Prender la estufa, el fuego debe estar al maximo \n2-poner el sarten en el fogon de la estufa \n3-Coger el aceite de nuestra preferencia y echarle al sarten \n ¿El aceite ya esta caliente?")
        print("OJO PARA VER SI EL ACEITE YA ESTA CALIENTEN NO TIENE QUE METER LA MANO")
        aceite=input ("Le pregunto otravez \n¿El aceite ya esta caliente?")
        if aceite== "si":
            indicaciones = input ("¿Siguio las indicaciones?") .lower()
            if indicaciones=="si":
                print ("Rompemos los huevos en un plato")
                print("DEBE DE TENER MUCHO CUIDADO CON EL SIGUIENTE PASO, SI LE TIENE MIEDO AL ACEITE BUSQUE A UN MAYOR DE EDAD QUE LO AYUDE ")
                next=input("¿Ya estas listo para los siguientes pasos que son los mas riesgosos?") .lower()
                if next=="si":
                    print("buscamos la tapa del saten ")
                    Tapa= input("¿Ya encontramos la tapa de la sarten?") .lower()
                    if Tapa=="si":
                      print("echamos el huevo y le ponemos la tapa para que el aceite no ensucie mucho la estufa")
                      print("le bajamos el volumen para que se cocine lentamente \n Si quiere con la llema dura dejelo unos 18mn si lo quiere con la llema blandita dejelos unos 10mn")
                      print("¿Ya sabe en que plano poner su huevo frito?")
                    elif Tapa== "no":
                        print("Buscamos la tapa del sarten y se lo ponemos, si no tiene pongale una que se asemeje a la medida del sarten")
                        print("Y le ponemos la tapa para que no ensucie mucho la estufa")  
                        print("le bajamos el volumen para que se cocine lentamente \n Si quiere con la llema dura dejelo unos 18mn si lo quiere con la llema blandita dejelos unos 10mn")
                        print("¿Ya sabe en que plano poner su huevo frito?")
                    plato= input() .lower()
                    if plato=="si":
                        print("Poner el huevo en el plato")
                        print("Despues de poner el huevo en el plato, apagar la estufa \n revisar que todos los fogones no esten saliendo gas")
                        print("¿Le gusta la sal?")
                        sal= input() .lower()
                        if sal=="si":
                            print ("Echarle sal al gusto")
                            print ("Ya puede comerce el huevo con todo el gusto del mundo \n Que lo disfrute<3")
                            texto = "Gracias por seguir los pasos"
                            letrero = ((texto))
                            print(letrero) 
                        else: print("Ya puede comerce el huevo con todo el gusto del mundo \n Que lo disfrute<3")
                        texto = "Gracias por seguir los pasos"
                        letrero = ((texto))
                        print(letrero) 
                    else: print ("Ver rapido en que plato o en donde lo va a servir y volver a empezar en donde se quedo")
                else:print("Vuelva cuando este listo")
            else : print ("PORFAVOR SEGUIR LAS INDICACIONES PARA QUE TODO SALGA COMO LO PLANEADO")
        else: print("Espere a que este caliente para que pueda seguir con el siguiente paso")
    else:print ("Conseguir una estufa o decirle a alguien que se la preste y vuelve a empezar")
else:print("Conseguir los ingredientes para poder hacer el huevo frito \nVuelve a empezar cuando tengas los ingredientes")

            

