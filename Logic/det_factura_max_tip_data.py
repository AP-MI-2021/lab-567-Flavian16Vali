from Domain.factura import get_tipul, get_str
from Domain.factura import get_suma

def get_tip(facturi):
    '''
    Cream o lista cu toate tipurile de facturi
    :param factura: Lista facturi
    :return: Lista cu toate tipurile de facturi
    '''
    tip_fac=[]
    for factura in facturi:
        aux=get_tipul(factura)
        ok=0
        for i in tip_fac:
            if set(i)==set(aux):
                ok=1
        if ok==0:
            tip_fac.append(aux)
    return tip_fac

def get_det_fac_max(facturi):
    '''
    Determinarea facturii maxime in functie de tip
    :param facturi: Lista facturi
    :return: Lista cu toate facturile maxime in functie de tip
    '''
    val_max=-1
    lista_tip_facturi=get_tip(facturi)
    for tip_factura in lista_tip_facturi:
        for factura in facturi:
            if set(get_tipul(factura))==set(tip_factura):
                if get_suma(factura)>val_max:
                    val_max=get_suma(factura)
        for factura in facturi:
            if get_suma(factura)==val_max:
                print("Valoarea maxima pentru tipul de factura: ",tip_factura, ", fiind: ", get_str(factura))
                break
