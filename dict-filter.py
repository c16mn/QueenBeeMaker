import json

# with open("scrabble.txt", "r") as dreader, open("dict_short.txt", "w") as dwriter:
#     for line in dreader:
#         if (len(line.strip()) >= 4 and len(set(line.strip())) <= 7):
#             dwriter.write(line)

dref = {"AA": 0}
with open("dict_short.txt", "r") as ds:
	linecounter = 0
	for line in ds:
		head = line[0:2]
		if head not in dref:
			dref[head] = linecounter
		linecounter = linecounter + 1

with open("dict_ref.py", "w") as dr:
	dr.write("dref = ")
	dr.write(json.dumps(dref))





