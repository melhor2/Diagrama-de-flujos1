print("Viene nuestro cantante favorito \nQueremos ir a verlo")
print("Presupuesto para las entradas \nPresupuesto : 1.600.000")
print("1-¿Vamos a comparar las boletas online? \n2-¿Vamos a comprar las boletas presencial en los puntos autorizados?")
print("Elegir opcion 1 o 2")
boletas= input() .lower()
if boletas=='1':
    print("Entrar al navegador de su preferencia y entrar al sitio web que este autorizado para comprar la boleta")
    print("Preguntar o ver que boletos tiene disponible, con sus precios \n¿Para que boletos nos alcanza? \n1-Vip : 1.500.000 \n2-SemiVip : 1.000.000")
    print("Presupuesto : 1.600.000 \nElegir opcion 1 o 2")
elif boletas== "2":
    print("Ir a los puntos autorizados (el que nos quede cerca)")
    print("Preguntar o ver que boletos tiene disponible, con sus precios \n¿Para que boletos nos alcanza? \n1-Vip : 1.500.000 \n2-SemiVip : 1.000.000")
    print("Presupuesto : 1.600.000 \nElegir opcion 1 o 2")
precios= input() .lower()
if precios== "1":
    print("¿Quieres pagar los boletos con la tarjeta de credito? \nO \n¿tarjeta de debito?")
    print("Elegir : Credito o Debito")
elif precios=="2":
    print("¿Quieres pagar los boletos con la tarjeta de credito? \nO \n¿tarjeta de debito?")
    print("Elegir : Credito o Debito")
pago= input() .lower()
if pago == "credito":
    print("Pagarle con la tarjeta de credito la cantidad de boletos que compramos")
    print("Verificar que nuestros datos en la boleta esten bien para no tener ningun incoveniente al momento de entrar")
    print("¿Todos los datos estan bien?")
elif pago== "debito":
    print("Pagarle con la tarjeta de debito la cantidad de boletos que compramos")
    print("Verificar que nuestros datos en la boleta esten bien para no tener ningun incoveniente al momento de entrar")
    print("¿Todos los datos estan bien?")
Verificacion= input() .lower()
if Verificacion=="si":
    print("El dia del concierto es el 31/04/2023 \nQue los disfurtes<3")
    print("Gracias por seguir nuestros pasos")
    print("FIN")
elif Verificacion=="no":
    print("Decirle a la operadora que le cambie los boletos que hay una informacion incorrecta y no queremos tener incovenientes al entrar")
    print("El dia del concierto es el 31/04/2023 \nQue los disfurtes<3")
    print("Gracias por seguir nuestros pasos")
    print("FIN")