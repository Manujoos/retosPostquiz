participants = []
times = []
c = 1
r = ""
while r == "":
    participants.append(input(f"Ingrese el nombre del parcitipante numero {c} "))
    times.append(input(f"Ingrese el tiempo de este participante {c} "))
    c += 1
    r = input("Para agregar otro participante pulsa enter ")

print("---------------------- terminó la competencia ----------------------")

for l1, l2 in zip(participants, times):
    print("El participante", l1, "hizo un tiempo de ", l2)

min = times[0]
for i in times:
    if i < min:
        min = i
position = times.index(min)

print("¡EL GANADOR ES!")
print(participants[position], "Con un tiempo de ", min)





