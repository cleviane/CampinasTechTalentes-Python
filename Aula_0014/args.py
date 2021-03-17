def world_cup_titles(country, *args):
    print('País: ', country)
    for title in args:
        print('ano: ', title)


# pode fazer tuplas de tuplas
world_cup_titles(('Brazil','Alemanha'), ('1958', '1962', '1970', '1994', '2002'))
