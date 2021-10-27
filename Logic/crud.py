from Domain.cheltuiala import get_nr_ap
from Domain.cheltuiala import creeaza_cheltuiala

def create(lst_cheltuieli,nr_ap:int, suma:float, data:str, tipul:str):
    '''

    :param lst_cheltuieli: lista de cheltuieli
    :param nr_ap: numarul apartamentului, trebuie sa fie unic
    :param suma: cheltuiala totala
    :param data: ata in care se primeste factura
    :param tipul: tipul cheltuielii, intretinerea, canal si alte cheltuieli
    :return: o nou lista formata din lst_cheltuieli si noua cheltuiala adaugata
    '''
    cheltuiala=creeaza_cheltuiala(nr_ap,suma,data,tipul)
    #lst_cheltuieli.append(cheltuiala)
    return lst_cheltuieli + [cheltuiala]


def read(lst_cheltuieli, nr_ap=None):
    '''
    Citeste o cheltuiala din baza de date
    :param lst_cheltuieli: lista de cheltuieli
    :param nr_ap: numarul apartamentului dorit
    :return: apartamentul cu numarul nr_ap sau lista cu toate cheltuielile, daca nr_ap=None
    '''
    cheltuiala_ap=None
    for cheltuiala in lst_cheltuieli:
        if get_nr_ap(cheltuiala)==nr_ap:
            cheltuiala_ap=cheltuiala
    if cheltuiala_ap:
        return cheltuiala_ap
    return lst_cheltuieli


def update(lst_cheltuieli, new_cheltuiala):
    '''
    Actualizeaza o cheltuiala
    :param lst_cheltuieli: lista de cheltuieli
    :param new_cheltuiala: cheltuiala care se va actualiza, numarul apartamentului trebuie sa fie unul existent
    :return: o lista cu cheltuiala actualizata
    '''
    new_cheltuiali= []
    for cheltuiala in lst_cheltuieli:
        if get_nr_ap(cheltuiala)!=get_nr_ap(new_cheltuiala):
            new_cheltuiali.append(cheltuiala)
        else: new_cheltuiali.append(new_cheltuiala)
    return new_cheltuiali


def delete(lst_cheltuiali, nr_ap):
    '''
    Eliminarea unei cheltuieli din lista
    :param lst_cheltuiali: lista de cheltuieli
    :param nr_ap: numarul apartamentului dorit
    :return: o lista de cheltuieli fara cheltuiala de la apartamentul CU numarul nr_ap
    '''
    new_cheltuieli= []
    for cheltuiala in lst_cheltuiali:
        if get_nr_ap(cheltuiala)!=nr_ap:
            new_cheltuieli.append(cheltuiala)
    return new_cheltuieli