def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'Nombre': 'Jose', 'Apellido': 'Messi'}

    super_list = [  
        {'Nombre': 'Erling', 'Apellido': 'Haaland'},
        {'Nombre': 'Kylian', 'Apellido': 'Mbappe'},
        {'Nombre': 'Jadon', 'Apellido': 'Sancho'}
    ]

    super_dict = {
        "numbers_naturales": [1,2,3,4,5],
        "integers_numbers": [10, 20, 30, 40, 50],
        "float_numbers": [12.4, 15.6, 20.3, 55.5, 45.8]
    }
    #con este for de abajo sacamos la key y el value del super_dict, apoyados en el one para la llave
    #y el two para el value, y llamando el metodo items()
    print("*****for del super diccionario para imprimir llaves y valores")
    for one, two in super_dict.items():
        print(one, "-", two)
    #si en este for declaro las dos variables por ejemplo one y two, puedo imprimir solo one que corresponde
    # a la key y si corre
    print("***for del super diccionario para imprimir solo las llaves***")
    for one, two in super_dict.items():
        print(one)
    print("*****for de la super_list para imprimir los valores de los diccionarios que están en esa lista*****")
    for i in super_list:
        print(i["Apellido"])
    print("********for de la super_list para imprimir las llaves del los diccionarios que están en esa lista*****")
    for i in super_list:
        print(i["Nombre"])

if __name__ == '__main__':
    run()