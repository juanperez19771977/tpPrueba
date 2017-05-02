while True:

    #tableros
    #tablero nivel 1
    tablero1 = {"a1": "0", "b1": "0", "c1": ".", "d1": "0", "e1": "0",
               "a2": "0", "b2": ".", "c2": "0", "d2": ".", "e2": "0",
               "a3": ".", "b3": "0", "c3": "0", "d3": "0", "e3": ".",
               "a4": "0", "b4": ".", "c4": "0", "d4": ".", "e4": "0",
               "a5": "0", "b5": "0", "c5": ".", "d5": "0", "e5": "0"}

    #tablero nivel 2
    tablero2 = {"a1": ".", "b1": "0", "c1": ".", "d1": "0", "e1": ".",
               "a2": "0", "b2": "0", "c2": ".", "d2": "0", "e2": "0",
               "a3": ".", "b3": "0", "c3": ".", "d3": "0", "e3": ".",
               "a4": "0", "b4": ".", "c4": "0", "d4": ".", "e4": "0",
               "a5": "0", "b5": ".", "c5": "0", "d5": ".", "e5": "0"}

    #tablero nivel 3
    tablero3 = {"a1": "0", "b1": ".", "c1": ".", "d1": ".", "e1": "0",
               "a2": "0", "b2": "0", "c2": ".", "d2": "0", "e2": "0",
               "a3": ".", "b3": ".", "c3": "0", "d3": ".", "e3": ".",
               "a4": "0", "b4": ".", "c4": "0", "d4": ".", "e4": ".",
               "a5": "0", "b5": ".", "c5": "0", "d5": "0", "e5": "."}

    #tablero nivel 4
    tablero4 = {"a1": "0", "b1": "0", "c1": ".", "d1": "0", "e1": "0",
               "a2": ".", "b2": ".", "c2": ".", "d2": ".", "e2": ".",
               "a3": "0", "b3": "0", "c3": ".", "d3": "0", "e3": "0",
               "a4": ".", "b4": ".", "c4": ".", "d4": ".", "e4": "0",
               "a5": "0", "b5": "0", "c5": ".", "d5": ".", "e5": "."}

    #tablero nivel 5
    tablero5 = {"a1": ".", "b1": ".", "c1": ".", "d1": "0", "e1": "0",
               "a2": ".", "b2": ".", "c2": ".", "d2": "0", "e2": "0",
               "a3": ".", "b3": ".", "c3": ".", "d3": ".", "e3": ".",
               "a4": "0", "b4": "0", "c4": ".", "d4": ".", "e4": ".",
               "a5": "0", "b5": "0", "c5": ".", "d5": ".", "e5": "."}


    #1 Mensaje de bienvenida y opciones
    print ("Bienvenido")
    print ("")

    #1.1 menu
    seleccion = input ("Seleccionar nivel (1-5) o '0' para salir: ")
    if seleccion == "1":
        tablero = tablero1
    elif seleccion == "2":
        tablero = tablero2
    elif seleccion == "3":
        tablero = tablero3
    elif seleccion == "4":
        tablero = tablero4
    elif seleccion == "5":
        tablero = tablero5
    elif seleccion == "0":
        quit()
    else:
        print ("Opcion invalida")

    #2 JUEGO

    print (tablero["a1"],tablero["b1"],tablero["c1"],tablero["d1"],tablero["e1"])
    print (tablero["a2"],tablero["b2"],tablero["c2"],tablero["d2"],tablero["e2"])
    print (tablero["a3"],tablero["b3"],tablero["c3"],tablero["d3"],tablero["e3"])
    print (tablero["a4"],tablero["b4"],tablero["c4"],tablero["d4"],tablero["e4"])
    print (tablero["a5"],tablero["b5"],tablero["c5"],tablero["d5"],tablero["e5"])
    print ("")
    print ("Elegir una celda del tablera usando LETRAS para las columnas y NUMEROS para las filas, ej: A3")

    #cinco turnos/opciones
    for i in range (0,5):
        print ("")
        opcion = input("Opcion: ")

        #descomponer opcion
        letra  = opcion[0]
        numero = opcion[1]

        #Cinco celdas que cambian

        #cambios 1, 2 y 5
        cambio1 = letra + numero
        if tablero[cambio1] == "0":
            tablero[cambio1] = "."
        else:
            tablero[cambio1] = "0"

        #cambio2
        numero2 = str(int(numero)-1)
        if int(numero2) > 0:
            cambio2 = letra + numero2
            if tablero[cambio2] == "0":
                tablero[cambio2] = "."
            else:
                tablero[cambio2] = "0"

        #cambio5
        numero5 = str(int(numero) + 1)
        if int(numero5) < 6:
            cambio5 = letra + numero5
            if tablero[cambio5] == "0":
                tablero[cambio5] = "."
            else:
                tablero[cambio5] = "0"

        #cambios 3 y 4
        lista = ("a","b","c","d","e")

        if int((lista.index(letra))-1) > 0:
            letra3 = lista[int(lista.index(letra))-1]
            cambio3 = str(letra3) + str(numero)
            if tablero[cambio3] == "0":
                tablero[cambio3] = "."
            else:
                tablero[cambio3] = "0"

        if int((lista.index(letra)) + 1) < 4:
            letra4 = lista[int(lista.index(letra)) + 1]
            cambio4 = str(letra4) + str(numero)
            if tablero[cambio4] == "0":
                tablero[cambio4] = "."
            else:
                tablero[cambio4] = "0"

        print ("")
        print (tablero["a1"],tablero["b1"],tablero["c1"],tablero["d1"],tablero["e1"])
        print (tablero["a2"],tablero["b2"],tablero["c2"],tablero["d2"],tablero["e2"])
        print (tablero["a3"],tablero["b3"],tablero["c3"],tablero["d3"],tablero["e3"])
        print (tablero["a4"],tablero["b4"],tablero["c4"],tablero["d4"],tablero["e4"])
        print (tablero["a5"],tablero["b5"],tablero["c5"],tablero["d5"],tablero["e5"])

    #mensaje final
    print ("")
    puntos = list(tablero.values())
    if puntos.count(".") == 25:
        print ("Puntaje final: 500")
    else:
        print ("Puntaje final: -300")

    print ("")
    reiniciar = input("reiniciar? (S/N): ")
    if reiniciar == "n":
        quit()

