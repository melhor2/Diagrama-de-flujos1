print("Vamos a jugar un juego de elecciones")
print("¿Comenzamos?")
go= input() .lower()
if go=="si":
    print("Bienvenidos a los retos mortales")
    print("Escoger arena \n1-Marte \n2-Isla")
    arena= input() .lower()
    if arena=="2":
        print("Pasaste la primera eleccion \nTienes un comodin")
        print("¿Utilizar el comodin ahora o mastarde?")
        comodin= input() .lower()
        if comodin=="ahora":
            print("El comodin te da +1 Up, te encuentras a un leon, pero como tienes 1 vida de sobra")
            print("Te haces el muerto y el leon se va pensando que ya estas muerto ")
            print("Te vas antes que el leon vea que no estas muerto")
            print("Casi llegas a la meta \nTe encuentras 2 puertas")
            print("1-Camino Facil \n2-Camino dificl")
            print("¿Cual puerta escoges para abrir?")
            puerta= input() .lower()
            if puerta=="2":
                print("Al abrir la puerta te encuentra con una montaña super alta, pero antes de empezar decides tomar un descanso (Dormir) despues de 10horas descansando decides que ya es hora de subir la montaña")
                print("Despues de 2 dias subiendo la montaña, en la punta de la montaña te encuentras con el premio que tanto querias")
                print("HAS GANADO EL PREMIO DE LOS RETOS MORTALES")
                print("Que disfrutes tu premio \nEND GAME CHAMPION")
            elif puerta=="1":
                print("Como ya estas cansado decides tomar el camino facil pero cuando abres la puerta en el camino te encuentras al leon, como ya no tienes vidas mueres")
                print("GAME OVER LOSER")
                print("TRY AGAIN LOSER")
        elif comodin=="mastarde":
            print("Decides guardarlo pero en el camino se te pierde te encuentras al leon y te das de cuenta que se te perdio el comodin \nMueres por la mordida de un leon")
            print("GAME OVER LOSER")
            print("TRY AGAIN LOSER")
    elif arena=="1":
        print("Como no tienes equipo para respirar en marte \nMueres por falta de oxigeno ")
        print("GAME OVER LOSER")
        print("TRY AGAIN LOSER")
else : print("Vuelve cuando quieres jugar")