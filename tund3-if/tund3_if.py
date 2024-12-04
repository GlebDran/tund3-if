#ulesanne 1
print("\n--- ulesanne 1 ---\n")

nimi = input("Mis on sinu nimi? ")
if nimi.isalpha() and nimi.isupper():
    if nimi == "JUKU":
        print("Lähme kino")
        try: 
            vanus=int(input (f"Kui vana sa oled {nimi}? "))
            if vanus<0:
                print("VIGA")
            elif vanus<=6:
                print("Tasuta")
            elif vanus<15:
                print("lastepilet")
            elif vanus<65:
                print("täispilet")
            elif vanus<100:
                print("sooduspilet")
            else:
                print("Nii palju!!!")
        except:
            print("Täisarv oli vaja sisestada")
    else:
           print("Ootan Juku")
else:
    print("Segatud sõne")

print("\n--- ulesanne 2 ---\n")
#VARIANT 1

nimi1 = input("mis on sinu nimi? ")
nimi2 = input("mis on sinu nimi? ")
nimed= ["Kirill","Gleb"]
if nimi1.isalpha() and nimi2.isalpha():
    if nimi1 in nimed and nimi2 in nimed:
        print("Nad on pinginaabrid")
    else:
        print("Rühmakaaslased")
else:
    print("viga")
#VARIANT 2

if nimi1=="Kirill" and nimi2=="Gleb" or nimi2=="Kirill" and nimi1=="Gleb":
    print("Nad on pinginaabrid")
else:
    print("Rühmakaaslased")

print("\n--- ulesanne 3 ---\n")

try: # не дает выкинуть из программы, проверяет
    a=float(input("Toa pikkus: "))
    b=float(input("Toa laius: "))
    s=a*b
    print(f"Põranda pindala on {s} m**2")
    vastus = input("Kas tahad remondi teha?(Jah/Ei)")
    if vastus.upper()=="JAH" or vastus=="1":
        print("Remont")
        hind=float(input("Ühe meetri hind: "))
        sum=s*hind
        print(f"Remondi kulud on: {sum} €")
    elif vastus.upper()=="EI" or vastus=="0":
        print("-")
    else:
        print("Ei saa aru")
except:
    print("Numbird")

print("\n--- ulesanne 4 ---\n")