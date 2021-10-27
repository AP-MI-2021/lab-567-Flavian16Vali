def creeaza_cheltuiala(nr_ap:int, suma:float, data:str, tipul:str):
    '''
    Creeaza o cheltuiala
    :param nr_ap: numarul apartamentului, trebuie sa fie unic
    :param suma: cheltuiala totala
    :param data: data in care se primeste factura
    :param tipul: tipul cheltuielii, intretinerea, canal si alte cheltuieli
    :return: cheltuiala
    '''
    return [nr_ap, suma, data, tipul]

def get_nr_ap(cheltuiala):
    '''
    Getter prntru numarul apartamentului
    :param cheltuiala: cheltuiala
    :return: numarul apartamentului
    '''
    return cheltuiala[0]

def get_suma(cheltuiala):
    '''
    Getter cheltuiala totala
    :param cheltuiala: cheltuiala
    :return: cheltuiala totala data de cheltuiala
    '''
    return cheltuiala[1]

def get_data(cheltuiala):
    '''
    Getter data in care se primeste factura
    :param cheltuiala: cheltuiala
    :return: data in care se primeste factura data de cheltuiala
    '''
    return cheltuiala[2]

def get_tipul(cheltuiala):
    '''
    Getter tipul chltuielilor
    :param cheltuiala: cheltuiala
    :return: tipul cheltuielilor in functie de cheltuiala
    '''
    return cheltuiala[3]

def get_str(cheltuiala):
    return f'Cheltuiala de la apartamentul {get_nr_ap(cheltuiala)}, cu valoarea: {get_suma(cheltuiala)}, la data {get_data(cheltuiala)}, fiind de tipul {get_tipul(cheltuiala)}'
