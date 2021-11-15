from Tests.test_adaugare_valoare import test_adaugare_val
from Tests.test_crud import test_pentru_crud
from Tests.test_ordonare_descrescator_facturi import test_descrescator
from Tests.test_undo_redo import test_undo_si_redo
from UserInterface.command_line_console import run_console_ui
from UserInterface.console import run_ui
from Tests.test_stergere_apartament import test_delete_apartament
from Logic.crud import create


def main():
    facturi = []
    undo_list = []
    redo_list = []
    selecteaza_interfata = int(
        input("Selecteaza '1' pentru interfata producatorului si '2' pentru interfata utilizatorului: "))
    if selecteaza_interfata == 1:
        facturi = run_ui(facturi, undo_list, redo_list)
    elif selecteaza_interfata == 2:
        facturi = run_console_ui()
    else:
        print("Optiunea introdusa nu este corecta.")


"""def get_data():
    return [
        creeaza_factura(1,10,500,'16/12/2020','caldura'),
        creeaza_factura(2,11,700,'1/2/2020','chirie'),
        creeaza_factura(3,12,850,'6/1/2020','intretinere'),
        creeaza_factura(4,13,550,'6/2/2020','gaz'),
        creeaza_factura(5,14,250,'26/2/2021','apa')
    ]
"""
if __name__ == '__main__':
    test_pentru_crud()
    test_delete_apartament()
    test_adaugare_val()
    test_descrescator()
    test_undo_si_redo()
    facturi = []
    undo_list = []
    redo_list = []
    facturi = create(facturi, 1, 10, 500, '16/12/2020', 'caldura', undo_list, redo_list)
    facturi = create(facturi, 2, 10, 700, '1/12/2020', 'chirie', undo_list, redo_list)
    facturi = create(facturi, 3, 12, 850, '6/1/2020', 'intretinere', undo_list, redo_list)
    facturi = create(facturi, 4, 13, 550, '6/2/2020', 'gaz', undo_list, redo_list)
    facturi = create(facturi, 5, 14, 250, '20/2/2021', 'apa', undo_list, redo_list)
    facturi = create(facturi, 6, 14, 250, '21/2/2021', 'apa', undo_list, redo_list)
    run_ui(facturi, undo_list, redo_list)
    main()
