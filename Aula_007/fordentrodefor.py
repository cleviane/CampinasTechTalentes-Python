lista_matriz = [["a","b","c"],# posições da matriz
                ["d","e","f"],
                ["g","h","i"]]

#for denrto do for 
for it1 in lista_matriz:
    print(it1)
    for it2 in it1:
        print(f"O item é: {it2}")