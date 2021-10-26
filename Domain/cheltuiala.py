def creeaza_cheltuiala(nr_ap, suma, data, tipul):
    '''
    Creeaza o cheltuiala
    :param nr_ap: numarul apartamentului, trebuie sa fie unic
    :param suma: cheltuiala totala
    :param data: data in care se primeste factura
    :param tipul: tipul cheltuielii, intretinerea, canal si alte cheltuieli
    :return: cheltuiala
    '''
    return {
        'nr_ap': nr_ap,
        'suma': suma,
        'data':data,
        'tipul':tipul
    }

def get_nr_ap(cheltuiala):
    '''
    Getter prntru numarul apartamentului
    :param cheltuiala: cheltuiala
    :return: numarul apartamentului
    '''
    return cheltuiala['nr_ap']

def get_suma(cheltuiala):
    '''
    Getter cheltuiala totala
    :param cheltuiala: cheltuiala
    :return: cheltuiala totala data de cheltuiala
    '''
    return cheltuiala['suma']

def get_data(cheltuiala):
    '''
    Getter data in care se primeste factura
    :param cheltuiala: cheltuiala
    :return: data in care se primeste factura data de cheltuiala
    '''
    return cheltuiala['data']

def get_tipul(cheltuiala):
    '''
    Getter tipul chltuielilor
    :param cheltuiala: cheltuiala
    :return: Tipul cheltuielilor in functie de cheltuiala
    '''
    return cheltuiala['tipul']

