from copy import deepcopy

from Domain.factura import get_suma

def ordonare_descrescator(facturi:list,undo_list:list,redo_list:list):
    '''
    Ordoneaza descrescator facturile in functie de suma
    :param facturi: Lista de facturi
    :param undo_list: Lista precedenta a facturilor
    :param redo_list: Lista modificata a facturilor
    :return: 
    '''

    undo_list.append(deepcopy(facturi))
    redo_list.clear()

    for i in range(0, len(facturi) - 1):
        for j in range(i + 1, len(facturi)):
            if (get_suma(facturi[j]) > get_suma(facturi[i])):
                aux=facturi[i]
                facturi[i]=facturi[j]
                facturi[j]=aux
    return facturi
