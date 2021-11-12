from Logic.adaugare_valoare import handle_adaugare_valoare
from Logic.crud import create, delete
from Domain.factura import get_str, get_nr_ap
from Logic.crud import read
from Domain.factura import get_suma
from Domain.factura import get_data
from Domain.factura import get_tipul
from Logic.crud import update
from Domain.factura import creeaza_factura
from Logic.det_factura_max_tip_data import get_det_fac_max
from Logic.stergere_apartament import delete_ap
from Logic.descrescator_suma import ordonare_descrescator
from Logic.sume_lunare_apartament import suma_ap
from Logic.undo_redo import do_undo, do_redo


def show_menu():
    print('1. CRUD')
    print('2. Ștergerea tuturor facturilor pentru un apartament dat.')
    print('3. Adunarea unei valori la toate facturile dintr-o dată citită.')
    print('4. Determinarea celei mai mari facturi pentru fiecare tip de cheltuială.')
    print('5. Ordonarea facturilor descrescător după sumă.')
    print('6. Afișarea sumelor lunare pentru fiecare apartament.')
    print('u. Undo.')
    print('r. Redo.')
    print('a. Afisaarea tuturor facturilor.')
    print('d. Detaliile unei facturi.')
    print('x. Exit')

def handle_add(facturi,undo_list,redo_list):
    id=int(input("Dati id-ul facturii: "))
    nr_ap=int(input("Dati numarul apartamentului: "))
    suma=float(input("Dati suma facturii: "))
    data=str(input("Dati data in care s-a primit factura facturilor: "))
    tipul=str(input("Dati tipul facturii: "))
    return create(facturi,id,nr_ap, suma, data, tipul,undo_list,redo_list)

def handle_show_all(facturi):
    for factura in facturi:
        print(get_str(factura))

def handle_show_details(facturi):
    id=int(input("Dati id-ul facturii despre care doriti detalii: "))
    factura=read(facturi,id)
    print(f"Numarul apartamentului este: {get_nr_ap(factura)}, suma este: {get_suma(factura)}, primita la data de {get_data(factura)}, fiind de tipul {get_tipul(factura)}")

def handle_update(facturi,undo_list,redo_list):
    id = int(input("Id-ul facturii care se actualizeaza este: "))
    nr_ap = int(input("Dati numarul noului apartament care se actualizeaza: "))
    suma = float(input("Dati noua suma facturii: "))
    data = str(input("Dati data noua in care s-a primit factura facturilor: "))
    tipul = str(input("Dati tipul nou de facturi: "))
    return update(facturi,creeaza_factura(id,nr_ap,suma,data,tipul),undo_list,redo_list)


def handle_delete(facturi,undo_list,redo_list):
    id=int(input("Dati id-ul facturii care se sterge: "))
    facturi=delete(facturi,id,undo_list,redo_list)
    print("Stergerea facturii a fost efectuata cu succes.")
    return facturi

def handle_delete_apartament(facturi,undo_list,redo_list):
    nr_ap=int(input("Dati numarul apartamentului caruia i se sterg facturile: "))
    facturi=delete_ap(facturi,nr_ap,undo_list,redo_list)
    print(("Stergerea tuturor facturilor apartamentului selectat a fost efectuata cu succes."))
    return facturi


def handle_undo(facturi,undo_list,redo_list):
    undo_result=do_undo(undo_list,redo_list,facturi)
    if undo_result is not None:
        return undo_result
    return facturi


def handle_redo(facturi,undo_list,redo_list):
    redo_result=do_redo(undo_list,redo_list,facturi)
    if redo_result is not None:
        return redo_result
    return facturi


def handle_crud(facturi, undo_list, redo_list):
    while True:
        print('1. Adaugare unei facturi.')
        print('2. Modificarea unei facturi.')
        print('3. Stergerea unei facturi.')
        print('u. Undo.')
        print('r. Redo.')
        print('b. Revenire.')
        handle_show_all(facturi)
        optiune=input('Optiunea aleasa este: ')
        if optiune=='1':
            facturi=handle_add(facturi,undo_list,redo_list)
        elif optiune=='2':
            facturi=handle_update(facturi,undo_list,redo_list)
        elif optiune=='3':
            facturi=handle_delete(facturi,undo_list,redo_list)
        elif optiune=='u':
            facturi=handle_undo(facturi,undo_list,redo_list)
        elif optiune=='r':
            facturi=handle_redo(facturi,undo_list,redo_list)
        elif optiune=='a':
            handle_show_all(facturi)
        elif optiune=='d':
            handle_show_details(facturi)
        elif optiune=='b':
            break
        else:
            print('Optiune invalida')
    return facturi

def run_ui(facturi, undo_list, redo_list):
    while True:
        show_menu()
        handle_show_all(facturi)
        optiune=input("Optiunea aleasa este: ")
        if optiune=='1':
            facturi=handle_crud(facturi,undo_list,redo_list)
        elif optiune=='2':
            facturi=handle_delete_apartament(facturi,undo_list,redo_list)
        elif optiune=='3':
            facturi=handle_adaugare_valoare(facturi,undo_list,redo_list)
        elif optiune=='4':
            get_det_fac_max(facturi)
        elif optiune=='5':
            facturi = ordonare_descrescator(facturi, undo_list, redo_list)
        elif optiune=='6':
            suma_ap(facturi)
        elif optiune=='u':
            facturi=handle_undo(facturi,undo_list,redo_list)
        elif optiune=='r':
            facturi=handle_redo(facturi,undo_list,redo_list)
        elif optiune=='a':
            handle_show_all(facturi)
        elif optiune=='d':
            handle_show_details(facturi)
        elif optiune=='x':
            break
        else:
            print('Optiune invalida')
    return facturi
