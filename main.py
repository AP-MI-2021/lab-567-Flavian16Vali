from Tests.test_crud import test_pentru_crud
from UserInterface.console import run_ui

def main():
    facturi=[]
    facturi=run_ui(facturi)

if __name__=='__main__':
    test_pentru_crud()
    main()