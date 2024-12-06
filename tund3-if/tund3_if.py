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

hind = float(input("Mis hind on? : "))
if hind >= 700:
    hind = hind - (hind * 0.3)  # Применяем скидку 30%
    print(f"Sai allahindlus 30%, uus hind on {hind}")
else:
    print(f"soodustus pole, hind on {hind}")

print("\n--- ulesanne 5 ---\n")

temp = float(input("Mis on toatemperatuur? : "))

if temp > 18:
    print(f" {temp} on üle 18 kraadi, kõik on korras!")
else:
    print(f" {temp} on madalam kui 18 kraadi.")

print("\n--- ulesanne 6 ---\n")

kasv = float(input("Mis on sinu kasv? "))
if kasv<=160:
    print("lühike kasv")
elif kasv<180:
    print("keskmine kasv")
elif kasv>180:
    print("kõrg kasv")

print("\n--- ulesanne 7 ---\n")


sugu = str(input("Mis on sinu sugu? M/N "))
if sugu.upper()=="M":
    print("Tere mees")
elif sugu.upper()=="N":
    print("Tere naine")

kasv= float(input("Mis on sinu kasv? "))
if kasv<=160:
    print("lühike kasv")
elif kasv<180:
    print("keskmine kasv")
elif kasv>180:
    print("kõrg kasv")


print("\n--- ulesanne 8 ---\n")


from decimal import ROUND_UP
import random
vopros = input(str("Хочешь купить продукты? (да/нет): "))
if vopros.upper() == "ДА":
    print("покупки: ")
    tovar = ["молоко", "хлеб", "масло"] # создаем список товаров
    cena = [random.randint(50, 100), random.randint(20, 50), random.randint(100, 200)] #генерирую случайные цифры, тип ИНТ
    obshaja_summa = 0
    pokupka = input(f"хотите купить? {tovar[0]} за {cena[0]}€ ? (да/нет): ") # молоко (исчесление идет с 0 поэтому первый товар нулевой - молоко)
    if pokupka.upper() == "ДА":
        kolichestvo = int(input(f"сколько {tovar[0]} товаров хотите купить? "))
        obshaja_summa += cena[0] * kolichestvo
        print(f"Вы купили {kolichestvo} {tovar[0]} на сумму {cena[0] * kolichestvo}€")

    
    pokupka = input(f"хотите купить? {tovar[1]} за {cena[1]}€ ? (да/нет): ") # хлеб (второй товар исчесление с нуля поэтому - цифра 1)
    if pokupka.upper() == "ДА":
        kolichestvo = int(input(f"сколько {tovar[1]} товаров хотите купить? "))
        obshaja_summa += cena[1] * kolichestvo
        print(f"Вы купили {kolichestvo} {tovar[1]} на сумму {cena[1] * kolichestvo}€")

    
    pokupka = input(f"хотите купить? {tovar[2]} за {cena[2]}€ ? (да/нет): ") # масло (третрий товар исчесление с нуля пэтому - цифра 2)
    if pokupka.upper() == "ДА":
        kolichestvo = int(input(f"сколько {tovar[2]} товаров хотите купить? "))
        obshaja_summa += cena[2] * kolichestvo
        print(f"Вы купили {kolichestvo} {tovar[2]} на сумму {cena[2] * kolichestvo}€")

    # Выводим итоговую сумму
    print(f"Общая сумма: {obshaja_summa}")

elif vopros.upper() == "НЕТ":
    print("До свидания!")

else:
    print("Непонятный ответ!")

print("\n--- ulesanne 9 ---\n")

storona1 = float(input("Введите первую сторону квадрата: "))
storona2 = float(input("Введите вторую сторону квадрата: "))
storona3 = float(input("Введите третью сторону квадрата: "))
storona4 = float(input("Введите четвертую сторону квадрата: "))


if storona1 == storona2 == storona3 == storona4: # если все стороны равны, то это квадрат, если есть одно отличие то нет
    print("Это квадрат!")
else:
    print("Это не квадрат!")

print("\n--- ulesanne 10 ---\n")

import datetime
tekushij_god = datetime.datetime.now().year

den_rozhdenie = int(input("Введите день рождения: "))
mesjac_rozhdenija = int(input("Введите месяц рождения: "))
god_rozdenija = int(input("Введите год рождения: "))
vozrast = tekushij_god - god_rozdenija
if mesjac_rozhdenija < datetime.datetime.now().month or (mesjac_rozhdenija == datetime.datetime.now().month and den_rozhdenie < datetime.datetime.now().day):
    vozrast += 1
if vozrast % 10 == 0:
    jubilej = True
else:
    jubilej = False
if jubilej:
    print("юбилей!")
else:
    print("Это не юбилей.")

print("\n--- ulesanne 11 ---\n")

hind = float(input("введи цену? : "))
if hind >= 10:
    hind = hind - (hind * 0.1)  # Применяем скидку 30%
    print(f"получаешь скидку 10%, новая цена {hind}")
elif hind<=10:
     hind = hind -(hind*0.2)
     print(f"получаешь скидку 20%, новая цена {hind}")
else:
    print("скидки нет")

print("\n--- ulesanne 12 ---\n")

sugu = str(input("Какой ваш пол? М/Ж: "))
if sugu.upper() == "М":
    print("Привет, мужчина")
    vanus = int(input("Введи свой возраст: "))
    if 16 <= vanus <= 18:
        print("Возраст подходит")
    else:
        print("Возраст не подходит")
elif sugu.upper() == "Ж":
    print("Женщин не приглашали")
else:
    print("Неправильный ввод. Введите М или Ж")

print("\n--- ulesanne 13 ---\n")

import math

ljudi = int(input("введите кол-во пассажиров: "))
mesta = int(input("введите кол-во мест: "))
kolvo_avtobusov = (ljudi + mesta - 1) // mesta # % это способ округлить результат деления в большую сторону без использования дополнительных библиотек
ljudi_v_poslednem_avtobuse = ljudi % mesta if ljudi % mesta != 0 else mesta
# % — оператор остатка от деления
print(f"Необходимо {kolvo_avtobusov} автобусов.")
print(f"В последнем автобусе будет {ljudi_v_poslednem_avtobuse} человек.")