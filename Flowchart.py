print("Hoy vamos aprender como hacer un diagrama de flujo paso a paso")
print("¿Comenzamos?")
go= input() .lower()
if go=="si":
    print("Para empezar debemos entender el tema que vamos a reprensentar con el diagrama de flujo")
    print("Segundo vamos ha plantear nuestras ideas en un hoja ")
    print("¿Ya planteamos nuestra idea a un papel?")
    papel= input() .lower()
    if papel=="si":
        print("Vamos a pasar lo que hicimos en el papel a una aplicacion de diagrama de flujo de nuestra preferencia")
        print("Verificamos que los simbolos esten correctos para no equivocarnos a la hora de explicar nuestro diagrama")
    elif papel=="no":
        print("Cuando ya terminemos de plantear nuestra idea, podemos continuar con el siguiente paso")
        print("Vamos a pasar lo que hicimos en el papel a una aplicacion de diagrama de flujo de nuestra preferencia")
        print("Verificamos que los simbolos esten correctos para no equivocarnos a la hora de explicar nuestro diagrama")
    print("¿Ya terminamos de verificar los simbolos si estan bien ubicados, con su respectiva informacion?")
    simbolos= input() .lower()
    if simbolos=="si":
        print("despues de revisar, vamos a guardar el trabajo con su respectivo nombre")
        print("Subir el trabajo a la plataforma que nos asignaron o entregarselo al instructor \nYa terminamos todos los pasos, espero que te vaya bien")
        print("Gracias por seguir los pasos<3 \nFIN")
    elif simbolos=="no": 
        print("Si no verificamos si los simbolos estan bien podemos posseer algun error a la hora de explicar nuestro diagrama")
        print("¿Ya verificamos?")
        verificar= input() .lower()
        if verificar== "si":
            print("despues de revisar, vamos a guardar el trabajo con su respectivo nombre")
            print("Subir el trabajo a la plataforma que nos asignaron o entregarselo al instructor \nYa terminamos todos los pasos, espero que te vaya bien")
            print("Gracias por seguir los pasos<3 \nFIN") 
        else : print("Subimos el trabajo a la plataforma que nos asignaron o entregarselo al instructor \nYa terminamos todos los pasos, espero que te vaya bien")
else : print("Vuelve cuando estes listo")