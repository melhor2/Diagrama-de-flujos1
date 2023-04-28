print("¿Quieres adoptar un gato?")
adoptar= input() .lower()
if adoptar=="si":
    print("Vamos a la fundacion 'New Family' \nOpcion que nos da la fundacion \n1-Gato macho \n4 años \nraza :Americano de pelo duro \nColor :Gris con negro ")
    print("2-Gato embra \n2 años \nraza : Bengalí \nColor : cafe con negro")
    print("Elegir 1 o 2")
    opcion= input() .lower()
    if opcion=="1":
        print("Antes de hacer el papeleo para adoptar el gato, tenemos que ver si el gato te acepta como tu nueva familia")
    elif opcion=="2":
        print("Antes de hacer el papeleo para adoptar el gato, tenemos que ver si el gato te acepta como tu nueva familia")
    print("¿El gato te acepto?")
    aceptacion= input() .lower()
    if aceptacion=="si":
        print("Podemos proceder al siguiente \nEl papeleo para adoptar el gato")
        print("Ya te puedes llevar el gato para tu casa \nEspero que seas feliz con tu nuevo gato")
        print("¿Estas feliz por tu nuevo gato?")
        estado=input() .lower()
        if estado=="si":
            print("Que bien, que los disfrutes")
            print("Gracias por seguir los pasos \n FIN")
        else: print("Tranquilo que con tu nuevo gato vas a ser SUPER FELIZ")  
        print("Gracias por seguir los pasos \n FIN")  
    else: print("FIN DE LA ADAPTACION DEL GATO :(")
else:print("Vuelve cuando estes listo")