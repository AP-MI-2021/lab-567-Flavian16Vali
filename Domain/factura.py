def creeaza_factura(id:int, nr_ap:int, suma:float, data:str, tipul:str,undo_list,redo_list):
    '''
    Creeaza o factura
    :param id: id-ul facturii, trebuie sa fie unic
    :param nr_ap: numarul apartamentului
    :param suma: factura
    :param data: data in care se primeste factura
    :param tipul: tipul facturii
    :return: factura
    '''
    return [id, nr_ap, suma, data, tipul, undo_list, redo_list]

def get_id(factura):
    '''
    Getter prntru id-ul facturii
    :param factura: factura
    :return: numarul apartamentului
    '''
    return factura[0]

def get_nr_ap(factura):
    '''
    Getter prntru numarul apartamentului
    :param factura: factura
    :return: numarul apartamentului
    '''
    return factura[1]

def get_suma(factura):
    '''
    Getter factura totala
    :param factura: factura
    :return: factura totala data de factura
    '''
    return factura[2]

def get_data(factura):
    '''
    Getter data in care se primeste factura
    :param factura: factura
    :return: data in care se primeste factura data de factura
    '''
    return factura[3]

def get_tipul(factura):
    '''
    Getter tipul chltuielilor
    :param factura: factura
    :return: tipul facturilor in functie de factura
    '''
    return factura[4]

def get_str(factura):
    return f'Id-ul facturii este: {get_id(factura)}, numarul apartamentului este: {get_nr_ap(factura)}, suma este: {get_suma(factura)}, primita la data de {get_data(factura)}, fiind de tipul {get_tipul(factura)}'