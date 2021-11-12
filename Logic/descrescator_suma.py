from Domain.factura import get_suma

def ordonare_descrescator(facturi,undo_list,redo_list):
    '''
    Ordoneaza descrescator facturile in functie de suma
    :param factura: Lista facturilor
    :return: Lista facturilor ordonate
    '''

    for i in range(0, len(facturi) - 1):
        for j in range(i + 1, len(facturi)):
            if (get_suma(facturi[j]) > get_suma(facturi[i])):
                aux=facturi[i]
                facturi[i]=facturi[j]
                facturi[j]=aux
    return facturi
