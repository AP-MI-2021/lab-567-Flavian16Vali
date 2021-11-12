from Tests.test_adaugare_valoare import test_adaugare_val
from Tests.test_crud import test_pentru_crud
from Tests.test_ordonare_descrescator_facturi import test_descrescator
from UserInterface.command_line_console import run_console_ui
from UserInterface.console import run_ui
from Tests.test_stergere_apartament import test_delete_apartament

def main():
    facturi=[]
    undo_list=[]
    redo_list=[]
    selecteaza_interfata=int(input("Selecteaza '1' pentru interfata producatorului si '2' pentru interfata utilizatorului: "))
    if selecteaza_interfata==1:
        facturi=run_ui(facturi,undo_list,redo_list)
    elif selecteaza_interfata==2:
        facturi=run_console_ui()
    else: print("Optiunea introdusa nu este corecta.")

if __name__=='__main__':
    test_pentru_crud()
    test_delete_apartament()
    test_adaugare_val()
    test_descrescator()
    main()