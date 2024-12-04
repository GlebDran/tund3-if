#ulesanne 1
print("\n--- ulesanne 1 ---\n")

nimi = input("Nmis on sinu nimi? ")
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
