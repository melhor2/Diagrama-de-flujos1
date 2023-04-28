print("¿Quieres ir a un restaurante lujoso?")
print("Pero antes de ir tenemos que hacer una reservacion")
print("¿Comenzamos?")
go= input() .lower()
if go=="si":
    print("¿Con cuantas personas vamos a ir? \n ¿2 o mas personas?")
    personas= input() .lower()
    if personas== "2":
        print("Llamamos y preguntamos para que dia tiene una mesa disponible para 2 personas")
        print("La persona que hace las reservaciones dice: \n'Tengo disponible para el dia martes a las 8:00pm'\n ¿Le reservo ese dia?")
    elif personas== "mas personas":
        print("Llamamos y preguntamos para que dia tiene una mesa disponible para la cantidad de personas que vamos a invitar personas")
        print("La persona que hace las reservaciones dice: \n'Tengo disponible para el dia martes a las 8:00pm'\n ¿Le reservo ese dia?")
    reservacion= input() .lower()
    if reservacion=="si":
        print("Reservamos para ese dia, le decimos a las personas que queramos a invitar al resturante")
        print("Dia : 31/04/2023 \nHora : 8:00pm \nLocalizacion : Av Calle 66 # 69 B44")
        print("Verificar si los datos estan bien") 
        datos= input("¿Los datos estan bien?") .lower()
        if datos=="si":
            print("Que disfurtes de la cena \n    Gracias por seguir los pasos")
            print("FIN")
        else : print("Corregir los datos que estan errados para que no tengamos incovenientes a la hora de entrar al restaurante \nQue disfurtes de la cena \n    Gracias por seguir los pasos") 
    else :print("Lo llamamos el dia Sabado, porque abren la agenda y volver a repetir el procedimiento \n FIN")   
else : print("Vuelve cuando estes listo")