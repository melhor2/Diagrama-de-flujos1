print("¿Te gusta la pizza?")
respuesta=input() .lower()
if respuesta=='si':
    print("Menos mal jaja, vamos aprender hacer una pizza desde nuestra casa")
    print("Antes de empezar ¿tenemos los siguientes ingredientes?")
    print("Lista de ingredientes \n-Salsa de tomate \n-Masa para pizza (ya echa la masa) \n-Bloque de queso \n-2kL champiñones \n-2 pechugas de pollo")
    print("¿Tenemos los siguientes ingredientes?")
    respuesta2=input() .lower()
    if respuesta2=="si":
        print("Comencemos con la preparacion \n1-hervir los champiñones \n2-En otra olla poner a hervir la pechuga")
        print("Ir amazando la masa para que vaya cogiendo forma de un circulo")
        print("¿Ya tiene forma de un circulo?")
        circulo= input() .lower()
        if circulo=="si":
            print("Le echamos la salsa de tomate, bien esparcida por toda la masa de la pizza")
            print("Ya cuando tengamos la salsa bien esparcida podemos ir a ver si las pechugas y los champiñones ya estan cocinados ")
            print("¿Ya estan cocinados las pechugas y los champiñones?")
        elif circulo=="no":
            print("Seguimos amazando para que tengamos la forma de un circulo \nCuando ya este la forma del circulo pasamos con el siguiente paso")
            print("Le echamos la salsa de tomate, bien esparcida por toda la masa de la pizza")
            print("Ya cuando tengamos la salsa bien esparcida podemos ir a ver si las pechugas y los champiñones ya estan cocinados ")
            print("¿Ya estan cocinados las pechugas y los champiñones?") 
        cocinado= input() .lower()
        if cocinado=="si":
            print("Las sacamos y dejamos que repose el pollo para desmenuzarlo")
            print("mientrar vamos a quitarle el agua a los champiñones y vamos a poner un sarten con aceite para fritarlos para que tengan un rico sabor a la hora de comer la pizza")
            print("¿Ya estan los champiñones freidos?")
        elif cocinado=="no":
            print("Los dejamos un rato mas hasta que se cocinen \nCuando ya esten cocinados podemos seguir con el siguiente paso")
            print("Las sacamos y dejamos que repose el pollo para desmenuzar el pollo")
            print("mientrar vamos a quitarle el agua a los champiñones y vamos a poner un sarten con aceite para fritarlos para que tengan un rico sabor a la hora de comer la pizza")
            print("¿Ya estan los champiñones freidos?")
        champi= input() .lower()
        if champi=="si":
            print("En un plato con papel de cocina los ponemos ahi para que se quite el exceso de aceite")
        elif champi=="no":
            print("Los dejamos que esten bien freidos")
            print("y en un plato con papel de cocina los ponemos ahi para que se quite el exceso de aceite ")
        print("¿Ya esta la pechuga tibia para desmenuzar?")
        desmenuzar= input() .lower()
        if desmenuzar=="si":
            print("La desmenuzamos en pedazos no tan grandes para que alcance para toda la pizza")
        elif desmenuzar=="no":
            print("esperamos ha que este tibia la pechuga")
            print("cuando ya este tibia podemos seguir con el siguiente paso")
            print("La desmenuzamos en pedazos no tan grandes para que alcance para toda la pizza")
        print("¿Ya desmenuzamos toda la pechuga?")
        listo=input() .lower()
        if listo=="si":
            print("Agregamos los ingredientes que son las pechugas ya desmenuzadas y los champiñones ya freidos, a la masa con la salsa de tomate")
            print("Cojemos el bloque de queso y con un rayador de cocina comenzamos a rayar el queso y esparcirlo por toda la pizza que no quede ningun lado sin queso")
        elif listo=="no":
            print("Cuando ya desmenuzemos las pechugas seguimos con el siguiente paso")
            print("Agregamos los ingredientes que son las pechugas ya desmenuzadas y los champiñones ya freidos, a la masa con la salsa de tomate")
            print ("Cojemos el bloque de queso y con un rayador de cocina comenzamos a rayar el queso y esparcirlo por toda la pizza que no quede ningun lado sin queso")
        print("Ponemos el horno entre 450 y 500 grados Fahrenheit (lo que equivale de 250 a 260 grados centígrados)")
        print("Durante 12 a 16 minutos, dejamos la pizza en el horno")
        print("Ya pasaron 12 minutos, miramos si ya la pizza ")
        print("¿Ya esta lista la pizza? ")
        minutos=input() .lower()
        if minutos=="si":
            print("La sacamos")
        elif minutos=="no":
            print("Las dejamos los 16 minutos y la sacamos")
        print("Partimos la pizza en 6 pedazos \nY servimos para comer")
        print("Que disfrutes tu pizza hecha en casa")
        print("Gracias por seguir los pasos<3")
    else:print("Compramos los ingredientes para hacer nuestra pizza")
else:print("Busca otro tutorial, porque este no es para ti")


