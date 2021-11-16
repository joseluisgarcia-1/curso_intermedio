def run():
    """my_dict = {}
    for i in range(1, 101):
    	my_dict[i] = i**3
    print(my_dict)"""
    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(my_dict)

        
    # con este for lo que hice fue imprimir llaves que sean los primeros 100 numeros naturales y que los valores sean esos numeros 
    #eleveados al cubo
if __name__ == '__main__':
    run()
