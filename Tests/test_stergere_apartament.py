from Domain.factura import creeaza_factura
from Logic.crud import read, delete
from Logic.stergere_apartament import delete_ap


def get_data():
    return [
        creeaza_factura(1,10,500,'16/12/2020','apa'),
        creeaza_factura(2,11,700,'1/2/2020','chirie'),
        creeaza_factura(3,12,850,'6/1/2020','gaz'),
        creeaza_factura(4,13,550,'6/2/2020','caldura'),
        creeaza_factura(5,14,250,'26/2/2021','total')
    ]
def get_data1():
    return [
        creeaza_factura(1,10,500,'16/12/2020','apa'),
        creeaza_factura(3,12,850,'6/1/2020','gaz'),
        creeaza_factura(4,13,550,'6/2/2020','caldura'),
        creeaza_factura(5,14,250,'26/2/2021','total')
    ]
def get_data2():
    return [
        creeaza_factura(2, 11, 700, '1/2/2020', 'chirie'),
        creeaza_factura(3, 12, 850, '6/1/2020', 'gaz'),
        creeaza_factura(4, 13, 550, '6/2/2020', 'caldura'),
        creeaza_factura(5, 14, 250, '26/2/2021', 'total')
    ]
def test_delete_apartament():
    facturi=get_data()
    to_delete1=11
    to_delete2=10
    to_delete3=100
    assert delete_ap(facturi,to_delete1)==get_data1()
    assert delete_ap(facturi,to_delete2)==get_data2()
    assert delete_ap(facturi,to_delete3)==get_data()
