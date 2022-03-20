def run():
    palabra = str(input("ingresa la palabra que quiere probar: "))
    for palabra in palabra[::-1]:
        print(palabra)

if __name__ == '__main__':
    run()
