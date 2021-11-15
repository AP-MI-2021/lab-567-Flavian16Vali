from Domain.factura import get_id
from Domain.factura import creeaza_factura


def create(lst_facturi, id_f, nr_ap, suma, data, tipul, undo_list, redo_list):
    """
    Creaza o factura
    :param lst_facturi: lista de facturi
    :param id_f: id-ul facturii, trebuie sa fie unic
    :param nr_ap: numarul apartamentului
    :param suma: factura totala
    :param data: data in care se primeste factura
    :param tipul: tipul facturii
    :param undo_list: Lista undo
    :param redo_list: Lista redo
    :return: o noua lista formata din lst_facturi si noua factura adaugata
    """

    """if read(lst_facturi,id) is not None:
        raise Exception(f"Deja exista o factura cu id-ul {id}.")"""

    factura = creeaza_factura(id_f, nr_ap, suma, data, tipul)
    """lst_facturi.append(factura)"""

    for _factura in lst_facturi:
        if get_id(_factura) == get_id(factura):
            raise ValueError("Deja exista o factura cu acest id.")

    undo_list.append(lst_facturi)
    redo_list.clear()
    return lst_facturi + [factura]


def read(lst_facturi, id_f):
    """
    Citeste o factura din baza de date
    :param lst_facturi: lista de facturi
    :param id_f: id-ul facturii
    :return: factura cu id-ul sau lista cu toate facturile, daca id=None
    """

    if id_f is None:
        return lst_facturi
    factura_ap = None
    for factura in lst_facturi:
        if get_id(factura) == id_f:
            factura_ap = factura
    if factura_ap:
        return factura_ap
    return None


def update(lst_facturi, new_factura, undo_list, redo_list):
    """
    Actualizeaza o factura
    :param lst_facturi: lista de facturi
    :param new_factura: factura care se va actualiza, numarul apartamentului trebuie sa fie unul existent
    :param undo_list: Lista undo
    :param redo_list: Lista redo
    :return: o lista cu factura actualizata
    """
    new_facturi = []

    undo_list.append(lst_facturi)
    redo_list.clear()
    for factura in lst_facturi:
        if get_id(factura) != get_id(new_factura):
            new_facturi.append(factura)
        else:
            new_facturi.append(new_factura)
    return new_facturi


def delete(lst_facturi, id_f, undo_list, redo_list):
    """
    Eliminarea unei facturi din lista
    :param lst_facturi: lista de facturi
    :param id_f: numarul apartamentului dorit
    :param undo_list: Lista undo
    :param redo_list: Lista redo
    :return: o lista de facturi fara factura de la apartamentul CU numarul id
    """
    new_facturi = []
    for factura in lst_facturi:
        if get_id(factura) != id_f:
            new_facturi.append(factura)

    undo_list.append(lst_facturi)
    redo_list.clear()

    return new_facturi
