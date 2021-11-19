def run():
    """squares = []
    for i in range(1,101):
        if i % 3 != 0:
            squares.append(i**2)
    print(squares)"""
    #con ese condicional que coloqué, lo que le estoy pidiendo a la máquina es que me imprima los números que no son divisibles por 3
    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    print("new for******",squares)
    """
    lo que hacemos con este for es lo siguiente: 
    i elevado al cuadrado para todas las i del rango entre 1 y 101 solo si i modulo 3 es distinto de cero(0)
    """

if __name__ == '__main__':
    run()
