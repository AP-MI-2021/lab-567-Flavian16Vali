from Tests.test_adaugare_valoare import test_adaugare_val
from Tests.test_crud import test_pentru_crud
from Tests.test_ordonare_descrescator_facturi import test_descrescator
from UserInterface.command_line_console import user_main
from UserInterface.console import run_ui
from Tests.test_stergere_apartament import test_delete_apartament

def main():
    facturi=[]
    facturi=run_ui(facturi)
    #user_main()

if __name__=='__main__':
    test_pentru_crud()
    test_delete_apartament()
    test_adaugare_val()
    test_descrescator()
    main()