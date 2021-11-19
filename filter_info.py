DATA = [
    {
    'name': 'Lionel',
    'age': 34,
    'organization': 'Barcelona',
    'position': 'Goals',
    'language': 'Spanish',
    },
    {
    'name': 'Mbappe',
    'age': 22,
    'organization': 'Psg',
    'position': 'Goals',
    'language': 'Frances'
    },
    {
    'name': 'Verrati',
    'age': 26,
    'organization': 'Psg',
    'position': 'Assits',
    'language': 'Italian',
    },
    {'name': 'Neymar',
    'age': 30,
    'organization': 'Psg',
    'position': 'Goals',
    'language': 'Portuguese',
    },
    {
    'name': 'Donnaruma',
    'age': 22,
    'organization': 'Milan',
    'position': 'Goalie',
    'language': 'Italian',
    },
    {
    'name': 'De gea',
    'age': 30,
    'organization': 'Manchester',
    'position': 'Goalie',
    'language': 'Spanish',
    },
    {
    'name': 'Ederson',
    'age': 29,
    'organization': 'Manchester city',
    'position': 'Goalie',
    'language': 'Portuguese',
    },
    {
    'name': 'Musiala',
    'age': 17,
    'organization': 'Bayer',
    'position': 'Midfielder',
    'language': 'English',
    },
    {
    'name': 'Camavinga',
    'age': 16,
    'organization': 'Madrid',
    'position': 'Midfielder',
    'language': 'French',
    }


]
def run():
    #este es un for normal para obtener el nombre de los jugadores que su posición es "Goals", entonces me arroja
    #Lionel, Mbappe, Neymar
    for i in DATA:
        if i["position"] == "Goals":
            print(i["name"])
    """ ahora con un for de dict comprehension """
    print("**********nuevo for donde obtenemos el nombre de los jugadores que hablan italiano************")
    all_players = [players["name"] for players in DATA if players["language"] == "Italian"]
    all_goals = [players["age"] for players in DATA if players["position"] == "Goalie"]
    print(all_players) 
    print("edad de los porteros porteros",all_goals)
    print("*********funcion lambda con filter**********")
    adults = list(filter(lambda players:players['age']>18, DATA))
    print(adults)
    print("*********funcion lambda con map**********")
    #con esto traemos el nombre de los jugadores que su edad es mayor a 18
    adults = list(map(lambda players:players['name'], adults))
    print(adults)
    print("*********función que funciona con python 3.9**************")
    old_players = list(map(lambda players:players or {'old': players['age'] > 29}, DATA))
    print(old_players)

    for players in old_players:
        print(players)

if __name__ == '__main__':
    run()
