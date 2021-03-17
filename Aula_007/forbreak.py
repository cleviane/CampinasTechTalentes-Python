
lista_frutas = ["banana", "abacaxi", "melancia", "laranja"]

print("começo programa")

for fruta in lista_frutas:
    if fruta == "abacaxi":
        break
    print(f"A fruta é {fruta}")
    #iteracao += 1

print("fim programa")

print("começo programa")

for fruta in lista_frutas:
    if fruta == "abacaxi":
        continue
    print(f"A fruta é {fruta}")
    #iteracao += 1

print("fim programa")
