def tablero(n):
    #tablero nivel 1
    tablero1 = {"a1": "0", "b1": "0", "c1": ".", "d1": "0", "e1": "0",
                "a2": ".", "b2": ".", "c2": ".", "d2": ".", "e2": ".",
                "a3": "0", "b3": "0", "c3": ".", "d3": "0", "e3": "0",
                "a4": ".", "b4": ".", "c4": ".", "d4": ".", "e4": "0",
                "a5": "0", "b5": "0", "c5": ".", "d5": ".", "e5": "."}

    # tablero nivel 2
    tablero1 = {"a1": ".", "b1": ".", "c1": ".", "d1": "0", "e1": "0",
                "a2": ".", "b2": ".", "c2": ".", "d2": "0", "e2": "0",
                "a3": ".", "b3": ".", "c3": ".", "d3": ".", "e3": ".",
                "a4": "0", "b4": "0", "c4": ".", "d4": ".", "e4": ".",
                "a5": "0", "b5": "0", "c5": ".", "d5": ".", "e5": "."}

    #JUEGO
    print(tablero["a1"], tablero["b1"], tablero["c1"], tablero["d1"], tablero["e1"])
    print(tablero["a2"], tablero["b2"], tablero["c2"], tablero["d2"], tablero["e2"])
    print(tablero["a3"], tablero["b3"], tablero["c3"], tablero["d3"], tablero["e3"])
    print(tablero["a4"], tablero["b4"], tablero["c4"], tablero["d4"], tablero["e4"])
    print(tablero["a5"], tablero["b5"], tablero["c5"], tablero["d5"], tablero["e5"])
    print("")
    print("Elegir una celda del tablera usando LETRAS para las columnas y NUMEROS para las filas, ej: A3")

