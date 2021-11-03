from Domain.factura import get_data
from Domain.factura import get_suma


def adugare_valoare(lst_facturi,suma,data):
    '''
    Adunarea unei valori la toate facturile dintr-o dată citită.
    :param lst_facturi: lista facturilor
    :param suma: suma adaugata
    :return: lista cu sumeles schimbate
    '''
    new_facturi= []
    for factura in lst_facturi:
        if set(get_data(factura))==set(data):
            new_facturi.append(factura)
            factura[2]=factura[2]+suma
        else:
            new_facturi.append(factura)
    return new_facturi


def handle_adaugare_valoare(facturi):
    suma=float(input("Valoarea adaugata la sume este: "))
    data=str(input("Data in care au ajuns facturile care le vor fi modificate sumele este: "))
    facturi=adugare_valoare(facturi,suma,data)
    print("Adaugarea valorii la sume a fost un succes.")
    return facturi