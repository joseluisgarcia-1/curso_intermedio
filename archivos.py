def read():
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as f:
        for i in f:
            numbers.append(int(i))
    print(numbers)
#con esta función lo que hago es abrir un archivo que está creado en una carpeta, en este caso la carpeta files 
#y el archivo numbers.txt 
def write():
    """names = ['Messi', 'Cristiano', 'Mbappe', 'Reus', 'Cavani', 'Dembelé']
    with open("./files/names.txt", "w", encoding="utf-8") as f:
        for i in names:
            f.write(i)
            f.write("\n")"""
    names = ["Hola", "como", "estas"]
    with open("./files/names.txt", "a", encoding="utf-8") as f:
        for i in names:
            f.write(i)
            f.write("\n")
"""con este función lo que hicimos fue crear una lista de datos de nombres, y debo tener en cuenta que el archivo
names.txt no estaba creado previamente, de todos modos, con el  línea de código se cr el archivo con esos datos
y teniendo en cuenta que se le colocó el encoding=utf-8 para que acepte tildes"""
"""en la siguiente función vamos a usar el metodo "a" de append, de agregar quiere decir modo de escritura sin
sobrescritura y por ejemplo ahora a 'Cristiano' lo cambio por 'Hazard' y lo que hace es a lo que ya estaba
agregar los nuevos datos que se le pasan por ejemplo a la lista names = ['Messi', 'Cristiano', 'Mbappe', 'Reus', 'Cavani', 'Dembelé']
se agrega ota lista con otros datos, por ejemplo así
names = ['Messi', 'Hazard', 'Mbappe', 'Reus', 'Cavani', 'Dembelé]"""
"""y si por ejemplo agrego una nueva lista, también se agrega con sus propios datos por ejemplo, si a las anteriores listas les agrego
esta lista names = ["Hola", "como, "estas"], entonces en el documento se crean esos datos"""

def run():
    write()

if __name__ == '__main__':
    run()