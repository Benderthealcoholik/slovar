import random
import os
from gtts import gTTS

def loe_failist(file_path):
    #chitat fail
    with open(file_path, 'r', encoding="utf-8") as file:
        sonad = [line.strip() for line in file]
    return sonad

def kirjuta(file_path, sonad):
    #razrewit chitat
    with open(file_path, 'w', encoding="utf-8") as file:
        for sona in sonad:
            file.write(sona + '\n')

def tolge_vene(sona):
    #perevod chtoby chitat
    if sona in estonian_to_russian:
        return estonian_to_russian[sona]
    else:
        print("nechego chitat")
        lisa_sona = input("dobavit chitat? y/n ").strip().lower()
        if lisa_sona == "y":
            tolge = input("nspiwi po russki: ").strip()
            estonian_to_russian[sona] = tolge
            kirjuta("rus.txt", list(estonian_to_russian.keys()))
            kirjuta("est.txt", list(estonian_to_russian.values()))
            print("dobavleno")
            return tolge
        else:
            return None

# funcija perevod
def tolge_est(sona):
    if sona in russian_to_estonian:
        return russian_to_estonian[sona]
    else:
        print("takogo net")
        lisa_sona = input("dobavit takoe? y/n ").strip().lower()
        if lisa_sona == "y":
            tolge = input("dobavit po estonski: ").strip()
            russian_to_estonian[sona] = tolge
            kirjuta("est.txt", list(russian_to_estonian.keys()))
            kirjuta("rus.txt", list(russian_to_estonian.values()))
            print("dobavleno")
            return tolge
        else:
            return None

def test_():
    kokku_sonad = len(russian_to_estonian)
    oiged_vastused = 0
    for russian_word, estonian_word in russian_to_estonian.items():
        print(f"perevedi '{russian_word}' na estonii")
        answer = input("perevorod: ").strip().lower()
        if answer == estonian_word.lower():
            print("molodec")
            oiged_vastused += 1
        else:
            print("ne molodec")
    tapsus = (oiged_vastused / kokku_sonad) * 100
    print(f" {oiged_vastused} из {kokku_sonad} слов. Точность: {tapsus}%")

def koneleja(sona):
    keel = "ru" if sona in russian_words else "et"
    tts = gTTS(text=sona, lang=keel)
    tts.save("temp.mp3")
    os.system("start temp.mp3")
    
russian_words = loe_failist("rus.txt")
estonian_words = loe_failist("est.txt")
russian_to_estonian = {}
estonian_to_russian = {}
for russian, estonian in zip(russian_words, estonian_words):
    russian_to_estonian[russian] = estonian
    estonian_to_russian[estonian] = russian

while True:
    print("\n1. perevedi na rus")
    print("2. rus est perevodi")
    print("3. test")
    print("4. koneleja")
    print("5. uhadi")
    vastus = input("vybiraj: ").strip()
    if vastus == '1':
        estonian_word = input("vvedi est: ").strip()
        tolge = tolge_vene(estonian_word)
        if tolge:
            print(f"perevod rus: {tolge}")
    elif vastus == '2':
        russian_word = input("vvedi rus: ").strip()
        tolge = tolge_est(russian_word)
        if tolge:
            print(f"perevod est: {tolge}")
    elif vastus == '3':
        test_()
    elif vastus == "4":
        sona = input("vvedi slovo: ").strip()
        koneleja(sona)
    elif vastus == '5':
        print("dosviduli")
        break
    else:
        print("eroor")
