from Logic.crud import create
from Domain.cheltuiala import get_str
from Logic.crud import read
from Domain.cheltuiala import get_suma
from Domain.cheltuiala import get_data
from Domain.cheltuiala import get_tipul
from Logic.crud import update
from Domain.cheltuiala import creeaza_cheltuiala

def show_menu():
    print('1. CRUD')
    print('2. Ștergerea tuturor cheltuielilor pentru un apartament dat')
    print('x. Exit')

def handle_add(cheltuieli):
    nr_ap=int(input("Dati numarul apartamentului: "))
    suma=float(input("Dati suma cheltuielilor: "))
    data=str(input("Dati data in care s-a primit factura cheltuielilor: "))
    tipul=str(input("Dati tipul cheltuielii: "))
    return create(cheltuieli,nr_ap, suma, data, tipul)

def handle_show_all(cheltuieli):
    for cheltuiala in cheltuieli:
        print(get_str(cheltuiala))

def handle_show_details(cheltuieli):
    nr_ap=int(input("Dati numarul aprtamentului despre care doriti detalii: "))
    cheltuiala=read(cheltuieli,nr_ap)
    print(f"Suma este: {get_suma(cheltuiala)}, primita la data de {get_data(cheltuiala)}, fiind de tipul {get_tipul(cheltuiala)}")

def handle_update(cheltuieli):
    nr_ap = int(input("Dati numarul apartamentului care se actualizeaza: "))
    suma = float(input("Dati noua suma cheltuielilor: "))
    data = str(input("Dati data noua in care s-a primit factura cheltuielilor: "))
    tipul = str(input("Dati tipul nou de cheltuieli: "))
    return update(cheltuieli,creeaza_cheltuiala(nr_ap,suma,data,tipul))

def handle_crud(cheltuieli):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisaare')
        print('d. Detalii cheltuiala')
        print('b. Revenire')
        optiune=input('Optiunea aleasa este: ')
        if optiune=='1':
            cheltuieli=handle_add(cheltuieli)
        elif optiune=='2':
            handle_update(cheltuieli)
        elif optiune=='a':
            handle_show_all(cheltuieli)
        elif optiune=='d':
            handle_show_details(cheltuieli)
        elif optiune=='b':
            break
        else:
            print('Optiune invalida')
    return cheltuieli

def run_ui(cheltuielli):
    while True:
        show_menu()
        optiune=input("Optiunea aleasa este:")
        if optiune=='1':
            handle_crud(cheltuielli)
        elif optiune=='x':
            break
        else:
            print('Optiune invalida')
    return cheltuielli
