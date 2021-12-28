
with open("scrabble.txt", "r") as dreader, open("dict_short.txt", "w") as dwriter:
    for line in dreader:
        if (len(line.strip()) >= 4 and len(set(line)) <= 7):
            dwriter.write(line)

