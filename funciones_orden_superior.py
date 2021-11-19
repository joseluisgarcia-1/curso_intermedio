#esta función lo que hace es mostrar solo los números impares de esa lista
def run():
    """my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    result = [i for i in my_list if i % 2 != 0]
    print(result)"""
    #esta función con el filter y en modo lambda
    my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    result = list(filter(lambda x: x%2 != 0, my_list))
    print("función lamba imprime numeros impares",result)
    print("*******función map***********")
    print("ejercicio de cada numero de la lista imprimirlo elevado al cuadrado")
    my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    squares = [i**2 for i in my_list]
    print(squares)
    print(my_list)
    print("************ aplicación función map**********")
    my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    result = list(map(lambda x: x**2, my_list))
    print(result)
    print("********aplicación función reduce *********")
    my_list = [2, 2, 2, 2, 2]
    all_multipled = 1
    for i in my_list:
        all_multipled = all_multipled * i
    print(all_multipled)
    print("****ahora ejemplo aplicando la función reduce****")
    from functools import reduce
    my_list = [2, 2, 2, 2, 2]
    all_multiplied = reduce(lambda a,b:a*b, my_list)
    print(all_multiplied)
if __name__ == '__main__':
    run()
