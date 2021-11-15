
from Domain.factura import creeaza_factura
from Logic.crud import create
from Logic.crud import read
from Domain.factura import get_id
from Logic.crud import update
from Logic.crud import delete




def get_data():
    return [
        creeaza_factura(1,10,500,'16/12/2020','caldura'),
        creeaza_factura(2,11,700,'1/2/2020','chirie'),
        creeaza_factura(3,12,850,'6/1/2020','intretinere'),
        creeaza_factura(4,13,550,'6/2/2020','gaz'),
        creeaza_factura(5,14,250,'26/2/2021','apa')
    ]
def test_create():
    facturi=get_data()
    undo_list = []
    redo_list = []
    params=(6,40,983,'4/10/2021','intretinere')
    c_new=creeaza_factura(*params)
    new_facturi=create(facturi, *params, undo_list, redo_list)
    assert new_facturi[-1]==c_new
    assert c_new in new_facturi

def test_read():
    facturi=get_data()
    some_c=facturi[2]
    assert read(facturi,get_id(some_c))==some_c
    assert read(facturi, None)==facturi

def test_update():
    facturi=get_data()
    undo_list=[]
    redo_list=[]
    c_updated=creeaza_factura(4,40,564,'29/9/2021','intretinere')
    updated=update(facturi, c_updated,undo_list,redo_list)
    assert c_updated in updated
    assert c_updated not in facturi
    assert len(updated)==len(facturi)

def test_delete():
    facturi=get_data()
    undo_list=[]
    redo_list=[]
    to_delete=3
    c_deleted=read(facturi, to_delete)
    deleted=delete(facturi, to_delete,undo_list,redo_list)
    assert c_deleted not in deleted
    assert c_deleted in facturi
    assert len(deleted)==len(facturi)-1

def test_pentru_crud():
    test_create()
    test_read()
    test_update()
    test_delete()