from Domain.factura import get_id
from Domain.factura import creeaza_factura

def create(lst_facturi,id:int, nr_ap:int, suma:float, data:str, tipul:str,
           undo_list:list, redo_list:list):
    '''

    :param lst_facturi: lista de facturi
    :param id: id-ul facturii, trebuie sa fie unic
    :param nr_ap: numarul apartamentului
    :param suma: factura totala
    :param data: data in care se primeste factura
    :param tipul: tipul facturii
    :param undo_list:
    :return: o noua lista formata din lst_facturi si noua factura adaugata
    '''

    """if read(lst_facturi,id) is not None:
        raise Exception(f"Deja exista o factura cu id-ul {id}.")"""

    factura=creeaza_factura(id,nr_ap,suma,data,tipul)
    #lst_facturi.append(factura)

    for _factura in lst_facturi:
        if get_id(_factura) == get_id(factura):
            raise ValueError("Deja exista o factura cu acest id.")


    undo_list.append(lst_facturi)
    redo_list.clear()
    return lst_facturi + [factura]


def read(lst_facturi, id):
    '''
    Citeste o factura din baza de date
    :param lst_facturi: lista de facturi
    :param id: id-ul facturii
    :return: factura cu id-ul sau lista cu toate facturile, daca id=None
    '''
    factura_ap=None
    for factura in lst_facturi:
        if get_id(factura)==id:
            factura_ap=factura
    if factura_ap:
        return factura_ap
    return lst_facturi


def update(lst_facturi, new_factura, undo_list, redo_list):
    '''
    Actualizeaza o factura
    :param lst_facturi: lista de facturi
    :param new_factura: factura care se va actualiza, numarul apartamentului trebuie sa fie unul existent
    :return: o lista cu factura actualizata
    '''
    new_facturi= []

    undo_list.append(lst_facturi)
    redo_list.clear()
    for factura in lst_facturi:
        if get_id(factura)!=get_id(new_factura):
            new_facturi.append(factura)
        else: new_facturi.append(new_factura)

    return new_facturi


def delete(lst_facturi, id, undo_list, redo_list):
    '''
    Eliminarea unei facturi din lista
    :param lst_facturi: lista de facturi
    :param id: numarul apartamentului dorit
    :return: o lista de facturi fara factura de la apartamentul CU numarul id
    '''
    new_facturi= []
    for factura in lst_facturi:
        if get_id(factura)!=id:
            new_facturi.append(factura)

    undo_list.append(lst_facturi)
    redo_list.clear()

    return new_facturi
