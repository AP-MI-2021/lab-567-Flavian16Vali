from Logic.crud import read, update
from UserInterface.console import handle_show_all, handle_delete
from Logic.adaugare_valoare import handle_adaugare_valoare

def read_list():
    lst = []
    lst_comenzi = input("Introduceti comenzile respectand instructiunea: ")
    lst_comenzi_split = lst_comenzi.split(';')
    for com_str in lst_comenzi_split:
        lst.append(com_str)
    return lst


def user_main():
    filename = ' text.txt'
    try:
        facturi = read(filename)
    except Exception:
        print('Nu s-a putut citi fisierul')
        lst_facturi = []

    while True:
        print("Intr-o linie de comanda scrie comenzile pe care le doresti indeplinite, separate prin ';' la final scriind comanda: exit ")
        print("1.Pentru afisarea tuturor facturilor vei scrie in linia de comanda : showall")
        print("2.Pentru adaugarea unei valorei unor facturi de la o data anume veo scrie in linia de comanda: adaugare_valoare ")
        print("3.Pentru a sterge o factura vei scrie linia de comanda : delete, id ")
        print("4.Pt iesirea din meniu introduceti: exit ")

        lista_comenzi = read_list()

        if "showall" in lista_comenzi:
            print(lst_facturi)
        for index in lista_comenzi:
            if "delete" in index:
                id_din_lista = index.split(',')[1]
                handle_delete(lst_facturi, int(id_din_lista))
                update(filename, lst_facturi)
                print("Stergere realizata cu succes")
        if "adaugare_valoare" in lista_comenzi:
            lst_noua = handle_adaugare_valoare(lst_facturi)
            print(f'Lista ordonata descresc este: \n {lst_noua}')
        if "exit" in lista_comenzi:
            break


