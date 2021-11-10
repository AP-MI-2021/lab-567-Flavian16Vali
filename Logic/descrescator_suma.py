from Domain.factura import get_suma

def ordonare_descrescator(factura):
    '''
    Ordoneaza descrescator facturile in functie de suma
    :param factura: Lista facturilor
    :return: Lista facturilor ordonate
    '''

    for i in range(0, len(factura) - 1):
        for j in range(i + 1, len(factura)):
            if (get_suma(factura[j]) > get_suma(factura[i])):
                aux=factura[i]
                factura[i]=factura[j]
                factura[j]=aux
    return factura
