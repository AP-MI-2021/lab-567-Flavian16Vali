from Domain.cheltuiala import creeaza_cheltuiala

def get_data():
    return [
        creeaza_cheltuiala(1,500,16/12/2020,intretinere)
        creeaza_cheltuiala(2,700,1/2/2020,intretinere)
        creeaza_cheltuiala(3,850,6/1/2020,intretinere)
        creeaza_cheltuiala(4,550,6/2/2020,intretinere)
        creeaza_cheltuiala(5,250,26/2/2021,intretinere)
    ]
def test_create():
    cheltuieli=get_data()
    c_new=creeaza_cheltuiala(6,983,4/10/2021,intretinere)