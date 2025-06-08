contacts = [
    {
        "name": "Anička",
        "email": "anicka@email.com",
        "phone": "777 777 777"
    },
    {
        "name": "Nikol",
        "email": "nikol@email.com",
        "phone": "777 777 777"
    }
]

#def hlavni_menu():
# vypsala: 
# 1. zobrazit kontakty
# 2. přidat kontakt 
# 3. ukončit

# načte vstup uživatele (input)

# zobrazí (print)

#def hlavni_menu():
   # print("1. zobrazit kontakty")
    #print("2. přidat kontakt")
   # print("3. ukončit")
    #volba = input("Zadejte číslo volby: ")
   # print(f"Vybrali jste možnost: {volba}")

# Pro otestování funkce:
#hlavni_menu():

contacts = [
    {
        "name": "Anička",
        "email": "anicka@email.com",
        "phone": "777 777 777"
    },
    {
        "name": "Nikol",
        "email": "nikol@email.com",
        "phone": "777 777 777"
    }
]

def zobraz_kontakty():
    print("\nSeznam kontaktů:")
    for i, kontakt in enumerate(contacts, 1):
        print(f"{i}. {kontakt['name']} - {kontakt['email']} - {kontakt['phone']}")
    print()

def pridej_kontakt():
    name = input("Zadejte jméno: ")
    email = input("Zadejte email: ")
    phone = input("Zadejte telefon: ")
    contacts.append({
        "name": name,
        "email": email,
        "phone": phone
    })
    print("Kontakt byl přidán!\n")

def hlavni_menu():
    while True:
        print("1. zobrazit kontakty")
        print("2. přidat kontakt")
        print("3. ukončit")
        volba = input("Zadejte číslo volby: ")

        if volba == "1":
            zobraz_kontakty()
        elif volba == "2":
            pridej_kontakt()
        elif volba == "3":
            print("Ukončuji program.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.\n")

# Spuštění programu
hlavni_menu()
