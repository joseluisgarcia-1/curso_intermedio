print("****función que recibe un número como parámetro y retornar una lista con todos los divisores número")
def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input("Ingresa un número: ")
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisors(int(num)))
    print("Terminó mi programa")
#isnumeric es un metodo de las strings que lo que hace es devolver verdadero si ese string se corresponde a una 
# especie de número y falso si no se corresponde, por lo tanto, si el usuario nos ingresa la letra esa línea nos 
# va devolver falso, si no, nos va devolver verdadero
if __name__ == '__main__':
    run()

