from Domain.cheltuiala import creeaza_cheltuiala
from Logic.crud import create
from Logic.crud import read
from Domain.cheltuiala import get_nr_ap
from Logic.crud import update
from Logic.crud import delete

def get_data():
    return [
        creeaza_cheltuiala(1,500,'16/12/2020','intretinere'),
        creeaza_cheltuiala(2,700,'1/2/2020','intretinere'),
        creeaza_cheltuiala(3,850,'6/1/2020','intretinere'),
        creeaza_cheltuiala(4,550,'6/2/2020','intretinere'),
        creeaza_cheltuiala(5,250,'26/2/2021','intretinere')
    ]
def test_create():
    cheltuieli=get_data()
    params=(6,983,'4/10/2021','intretinere')
    c_new=creeaza_cheltuiala(*params)
    new_cheltuieli=create(cheltuieli, *params)
    assert new_cheltuieli[-1]==c_new
    assert c_new in new_cheltuieli

def test_read():
    cheltuieli=get_data()
    some_c=cheltuieli[2]
    assert read(cheltuieli,get_nr_ap(some_c))==some_c
    assert read(cheltuieli, None)==cheltuieli

def test_update():
    cheltuieli=get_data()
    c_updated=creeaza_cheltuiala(4,564,'29/9/2021','intretinere')
    updated=update(cheltuieli, c_updated)
    assert c_updated in updated
    assert c_updated not in cheltuieli
    assert len(updated)==len(cheltuieli)

def test_delete():
    cheltuieli=get_data()
    to_delete=3
    c_deleted=read(cheltuieli, to_delete)
    deleted=delete(cheltuieli, to_delete)
    assert c_deleted not in deleted
    assert c_deleted in cheltuieli
    assert len(deleted)==len(cheltuieli)-1

def test_pentru_crud():
    test_create()
    test_read()
    test_update()
    test_delete()