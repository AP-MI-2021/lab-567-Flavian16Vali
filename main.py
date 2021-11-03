from Tests.test_crud import test_pentru_crud
from UserInterface.command_line_console import user_main
from UserInterface.console import run_ui

def main():
    facturi=[]
    facturi=run_ui(facturi)
    user_main()

if __name__=='__main__':
    test_pentru_crud()
    main()