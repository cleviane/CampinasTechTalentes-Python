def KelvinToFahrenheit(Temperature):
    # assert(Temperature >= 0),"Colder than absolute zero!"
    if Temperature >= 0:
        return((Temperature-273)*1.8)+32
# print(KelvinToFahrenheit(273))
# print(int(KelvinToFahrenheit(505.78)))
# print(KelvinToFahrenheit(-5))

# assert é para mapear
def imprime_nome(nome):
    assert(nome != "Clevi"),"O nome tem que ser diferente de Clevi"
    assert(nome != "João"), "O nome tem que ser diferente de João"
    print(nome)
# imprime_nome("Clevi")
imprime_nome("João")