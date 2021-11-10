from Domain.factura import creeaza_factura
from Logic.descrescator_suma import ordonare_descrescator


def get_data():
    undo_list = []
    redo_list = []
    return [
        creeaza_factura(1,10,500,'16/12/2020','caldura',undo_list,redo_list),
        creeaza_factura(2,11,700,'1/2/2020','chirie',undo_list,redo_list),
        creeaza_factura(3,12,850,'6/1/2020','intretinere',undo_list,redo_list),
        creeaza_factura(4,13,550,'6/2/2020','gaz',undo_list,redo_list),
        creeaza_factura(5,14,250,'26/2/2021','apa',undo_list,redo_list)
    ]
def get_data_descrescator():
    undo_list = []
    redo_list = []
    return [
        creeaza_factura(3,12,850,'6/1/2020','intretinere',undo_list,redo_list),
        creeaza_factura(2,11,700,'1/2/2020','chirie',undo_list,redo_list),
        creeaza_factura(4,13,550,'6/2/2020','gaz',undo_list,redo_list),
        creeaza_factura(1,10,500,'16/12/2020','caldura',undo_list,redo_list),
        creeaza_factura(5,14,250,'26/2/2021','apa',undo_list,redo_list)
    ]

def test_descrescator():
    facturi=get_data()
    undo_list = []
    redo_list = []
    facturi2=[]
    assert ordonare_descrescator(facturi)==get_data_descrescator()
    assert ordonare_descrescator(get_data_descrescator())==get_data_descrescator()
    assert ordonare_descrescator(facturi2)==[]