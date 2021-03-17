frutas = ["banana", "laranja", "limÃ£o", "cereja"]

# Open a file
fo = open("frutas.txt", "w")

for fruta in frutas:
    fo.write(f"{fruta} \n")


# Close opend file
fo.close()
