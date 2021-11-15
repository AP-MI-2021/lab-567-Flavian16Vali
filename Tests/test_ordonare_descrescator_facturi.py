from Domain.factura import creeaza_factura
from Logic.descrescator_suma import ordonare_descrescator


def get_data():
    return [
        creeaza_factura(1, 10, 500, '16/12/2020', 'caldura'),
        creeaza_factura(2, 11, 700, '1/2/2020', 'chirie'),
        creeaza_factura(3, 12, 850, '6/1/2020', 'intretinere'),
        creeaza_factura(4, 13, 550, '6/2/2020', 'gaz'),
        creeaza_factura(5, 14, 250, '26/2/2021', 'apa')
    ]


def get_data_descrescator():
    return [
        creeaza_factura(3, 12, 850, '6/1/2020', 'intretinere'),
        creeaza_factura(2, 11, 700, '1/2/2020', 'chirie'),
        creeaza_factura(4, 13, 550, '6/2/2020', 'gaz'),
        creeaza_factura(1, 10, 500, '16/12/2020', 'caldura'),
        creeaza_factura(5, 14, 250, '26/2/2021', 'apa')
    ]


def test_descrescator():
    facturi = get_data()
    facturi2 = []
    assert ordonare_descrescator(facturi, [], []) == get_data_descrescator()
    assert ordonare_descrescator(get_data_descrescator(), [], []) == get_data_descrescator()
    assert ordonare_descrescator(facturi2, [], []) == []
