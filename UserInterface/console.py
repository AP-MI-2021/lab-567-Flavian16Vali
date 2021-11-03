from Logic.adaugare_valoare import handle_adaugare_valoare
from Logic.crud import create, delete
from Domain.factura import get_str, get_nr_ap, get_id
from Logic.crud import read
from Domain.factura import get_suma
from Domain.factura import get_data
from Domain.factura import get_tipul
from Logic.crud import update
from Domain.factura import creeaza_factura
from Logic.stergere_apartament import handle_delete_apartament

def show_menu():
    print('1. CRUD')
    print('2. Ștergere')
    print('x. Exit')

def handle_add(facturi):
    id=int(input("Dati id-ul facturii: "))
    nr_ap=input("Dati numarul apartamentului: ")
    suma=float(input("Dati suma facturii: "))
    data=str(input("Dati data in care s-a primit factura facturilor: "))
    tipul=str(input("Dati tipul facturii: "))
    return create(facturi,id,nr_ap, suma, data, tipul)

def handle_show_all(facturi):
    for factura in facturi:
        print(get_str(factura))

def handle_show_details(facturi):
    id=int(input("Dati id-ul facturii despre care doriti detalii: "))
    factura=read(facturi,id)
    print(f"Numarul apartamentului este: {get_nr_ap(factura)}, suma este: {get_suma(factura)}, primita la data de {get_data(factura)}, fiind de tipul {get_tipul(factura)}")

def handle_update(facturi):
    id = int(input("Id-ul facturii care se actualizeaza este: "))
    nr_ap = int(input("Dati numarul noului apartament care se actualizeaza: "))
    suma = float(input("Dati noua suma facturii: "))
    data = str(input("Dati data noua in care s-a primit factura facturilor: "))
    tipul = str(input("Dati tipul nou de facturi: "))
    return update(facturi,creeaza_factura(id,nr_ap,suma,data,tipul))


def handle_delete(facturi):
    id=int(input("Dati id-ul facturii care se sterge: "))
    facturi=delete(facturi,id)
    print("Stergerea facturii a fost efectuata cu succes.")
    return facturi



def handle_crud(facturi):
    while True:
        print('1. Adaugare unei facturi')
        print('2. Modificarea unei facturi')
        print('3. Stergerea unei facturi')
        print('4. Stergerea facturilor unui apartament')
        print('5. Adunarea unei valori la toate facturile dintr-o dată citită.')
        print('a. Afisaarea tuturor facturilor')
        print('d. Detaliile unei facturi')
        print('b. Revenire')
        optiune=input('Optiunea aleasa este: ')
        if optiune=='1':
            facturi=handle_add(facturi)
        elif optiune=='2':
            facturi=handle_update(facturi)
        elif optiune=='3':
            facturi=handle_delete(facturi)
        elif optiune=='4':
            facturi=handle_delete_apartament(facturi)
        elif optiune=='5':
            facturi=handle_adaugare_valoare(facturi)
        elif optiune=='a':
            handle_show_all(facturi)
        elif optiune=='d':
            handle_show_details(facturi)
        elif optiune=='b':
            break
        else:
            print('Optiune invalida')
    return facturi

def run_ui(facturii):
    while True:
        show_menu()
        optiune=input("Optiunea aleasa este: ")
        if optiune=='1':
            handle_crud(facturii)
        elif optiune=='x':
            break
        else:
            print('Optiune invalida')
    return facturii
