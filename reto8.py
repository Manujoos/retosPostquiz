notes = []
r= ""
average = 0
while r=="":
    note = int(input("ingrese una nota: "))
    if 0<note<=5:
        notes.append(note)
    else:
        print("esta nota no se encuentra en el rango permitido (0 a 5)")
    r = input("Si deseas agreagr otra nota pulsa enter, de lo contrario pulsa otra tecla")
for i in notes:
    average += i
average = average/len(notes)
if average<3:
    print("REPROBASTE, tu promedio es de ", average)
elif 3<=average<=4:
    print("Pasate RASPANDO, tu promedio es de", average)
else:
    print("Aprobaste con BUENOS RESULADOS, tu promedio es de", average)
