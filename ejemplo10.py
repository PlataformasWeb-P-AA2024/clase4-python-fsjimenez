archivo = open("data/atp_tennis.csv", "r")
lineas = archivo.readlines()

lineas = [l.split("|") for l in lineas]

for x in lineas:
	print(x[9])
