from Domain.factura import creeaza_factura
from Logic.adaugare_valoare import adugare_valoare


def get_data():
    return [
        creeaza_factura(1,10,500,'16/12/2020','caldura'),
        creeaza_factura(2,11,700,'1/2/2020','chirie'),
        creeaza_factura(3,12,850,'6/1/2020','intretinere'),
        creeaza_factura(4,13,550,'6/2/2020','gaz'),
        creeaza_factura(5,14,250,'26/2/2021','apa')
    ]

def get_data1():
    return [
        creeaza_factura(1,10,500,'16/12/2020','caldura'),
        creeaza_factura(2,11,700,'1/2/2020','chirie'),
        creeaza_factura(3,12,950,'6/1/2020','intretinere'),
        creeaza_factura(4,13,550,'6/2/2020','gaz'),
        creeaza_factura(5,14,260,'26/2/2021','apa')
    ]
def test_adaugare_val():
    facturi=get_data()
    to_add1=0
    to_date1='16/12/2020'
    to_add2=10
    to_date2='29/2/2021'
    to_add3=100
    to_date3='6/1/2020'
    assert adugare_valoare(facturi,to_add1,to_date1)==get_data()
    assert adugare_valoare(facturi,to_add2,to_date2)==get_data()
    #assert adugare_valoare(facturi,to_add3,to_date3)==get_data1()