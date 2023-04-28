print("Bienvenido a mi rutina diaria")
print("¿Listo para ver que hago todos los dias de mi vida?")
go= input() .lower()
if go=="si":
    print("¿A que horas crees que me levanto? \n1-6:00am \n2-7:00am")
    hora= input() .lower()
    if hora=="1":
        print("Si, me levanto a las 6:00am jaja ")
    elif hora=="2":
        print("Algunas veces me levanto a las 7:00am, me levanto a esa hora cuando me acuesto muy tardeee")
    print("Despues de levantarme alisto a mi perro y lo saco para que haga sus necesidades")
    print("aprovecho tambien para comprar el pan para el desayuno")
    print("Tiendo mi cama y me meto a bañar")
    print("Para ustedes ¿Creen que yo me hago el desayuno o me lo hace mi abuelita?")
    print("Escribir : Usted se lo hace, si creen que yo me lo hago \nescribir : Le hacen el desayuno ")
    desayuno= input() .lower()
    if desayuno=="usted se lo hace":
        print("Si, la mayoria de veces yo me lo hago")
    elif desayuno=="le hacen el desayuno":
        print("Algunas veces, si me coge la tarde arreglando la cama o bañandome, mi abuelita me hace el favor")
    print("Prendo el computador mientras me desayuno para entrar con todas las energias al bootcamp")
    print("Voy ingresando a todas la aplicaciones que necesite o vaya a necesitar en el proceso")
    print("¿Entro a la clase?")
    clase= input() .lower()
    if clase=="si":
        print("Asies, si entro a clase, toca ser cumplido con los deberes y los estudios")
    elif clase=="no":
        print("Obivamente que si entro a clase, toca ser comprometido con nuestros deberes o nuestros estudios")
    print("Sigo las instrucciones que me dan los instructores y hago mis trabajos hasta terminarlos para entregarlos a tiempo")
    print("Si acabo los trabajos rapido, veo videos relacionados a temas o temas nuevos que me interesa aprender" )
    print("A la hora de almuerzo tengo 2 opciones saco al perro o almuerzo")
    print("¿Cual creen que hago?")
    print("Escribir : Almuerzo, si salgo ha almorzar \nEscribir : Saca al perro, si aplazo mi almuerzo para sacar a mi perro")
    almuerzo= input() .lower()
    if almuerzo=="almuerzo":
        print("Pocas veces almuerzo a las 1, porque no me da hambre o desayune mucho que no tengo hambre")
    elif almuerzo=="saca al perro":
        print("Siempre lo hago, pero obviamente almuerzo al 2 descanso ")
    print("llega las 6:00pm y se acaba la clase y nuevamente saco a mi perro a jugar")
    print("Despues de llegar del parque con mi perro, veo si tengo unos trabajos pendientes y los realizo y si no tengo trabajos apago la pc")
    print("Ceno y me cepillo los dientes")
    print("¿A que horas creen que me duermo? \n1-11:00pm \n2-1:30am")
    dormir= input() .lower()
    if dormir=="1":
        print("Si, siempre me duermo a esa hora porque ya estoy supremamente cansado")
    elif dormir=="2":
        print("Solo me acuesto a esa hora los sabados o domingos jajaja")
    print("Gracias por ver mi rutina diaria<3 \nFIN A DORMIR")
else : print("Vuelve cuando quieras saber que hago todos los dias")
