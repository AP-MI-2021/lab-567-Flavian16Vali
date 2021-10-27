from Logic.crud import create
from Domain.cheltuiala import get_str

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

def handle_crud(cheltuieli):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisaare')
        print('b. Revenire')
        optiune=input('Optiunea aleasa este: ')
        if optiune=='1':
            cheltuieli=handle_add(cheltuieli)
        elif optiune=='a':
            handle_show_all(cheltuieli)
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
