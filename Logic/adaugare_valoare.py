from copy import deepcopy
from Domain.factura import get_data


def adugare_valoare(facturi, suma, data):
    """
    Adunarea unei valori la toate facturile dintr-o dată citită.
    :param facturi: lista facturilor
    :param suma: suma adaugata
    :param data: data facturii
    :return: lista cu sumeles schimbate
    """

    new_facturi = []

    for factura in facturi:
        if get_data(factura) == data:
            factura[2] = factura[2] + suma
            new_facturi.append(factura)
        else:
            new_facturi.append(factura)
    return new_facturi


def handle_adaugare_valoare(facturi, undo_list, redo_list):

    try:
        suma = float(input("Valoarea adaugata la facturi este: "))
    except ValueError as ve:
        print("Suma invalida")
        return facturi
    data = str(input("Data in care au ajuns facturile carora le vor fi modificate sumele este: "))

    aparitie = 0
    for _factura in facturi:
        if set(get_data(_factura)) == set(data):
            aparitie = 1
    if aparitie == 0:
        raise ValueError(f"Nu exista nicio factura cu data {data} careia sa i se adauge valoare.")

    undo_list.append(deepcopy(facturi))
    redo_list.clear()

    facturi = adugare_valoare(facturi, suma, data)
    print("Adaugarea valorii la sume a fost un succes.")

    return facturi
