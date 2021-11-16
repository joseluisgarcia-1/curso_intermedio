def run():
    palabra = str(input("ingresa una palabra: "))
    for palabra in palabra[::-1]:
        print(palabra)

if __name__ == '__main__':
    run()
