#kezdes: 13:15

with open("rendel.txt", "r", encoding="utf-8") as file:
    szamlalo = 0
    adat = []
    for i in file.readlines():
        if i.strip() != "":
            adat.append(i.split())
        else:
            szamlalo += 1



#rendelesnapja rendelesleadas termekdbszam

print("2. feladat:")
print(f"A rendelések száma: {len(adat)} ")


print("3. feladat: ")
#beker = input("Kérem, adjon meg egy napot: ")
szotar = {}
for i in adat:
    szotar[i[0]] = szotar.get(i[0], 0) + 1 

#print(f"A rendelések száma az adott napon: {szotar[beker]}")

#from collections import Counter
#szotar = dict(Counter(i[0] for i in adat))

print("4. feladat: ")
print(f"{szamlalo} nap nem volt a reklámban nem érintett városból rendelés ")

legnagyobb = adat[0][-1], adat[0][0]
for i in adat:
    if int(i[-1]) > int(legnagyobb[0]):
        legnagyobb = i[-1], i[0]

print("5. feladat")
print(f"A legnagyobb darabszám: {legnagyobb[0]}, a rendelés napja: {legnagyobb[1]} ")


def osszes(varos, sorszam, *_):
    osszeg = 0
    for i in adat:
        if i[1] == varos and int(i[0]) == sorszam:
            osszeg += int(i[-1])
    return osszeg


print("7. feladat")
szotar2 = {}
for i in adat:
    if  i[0] == "21":
        szotar2[i[1]] = szotar2.get(i[1],  0) + int(i[-1])

print(f"A rendelt termékek darabszáma a 21. napon PL: {szotar2['PL']} TV: {szotar2['TV']} NR: {szotar2['NR']} ")
